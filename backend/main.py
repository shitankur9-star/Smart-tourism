import os
import uuid
from pathlib import Path
from datetime import datetime, timedelta
from urllib.parse import quote_plus
from urllib.request import Request, urlopen
import json

from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Header,
    UploadFile,
    File,
    Query,
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from jose import jwt, JWTError
import bcrypt

from database import engine, get_db, Base
from models import (
    Trip,
    User,
    Destination,
    TravelCost,
    FootfallData,
    Hotel,
    TravelerExpense,
    StandardRate,
    PlaceHistory,
    CommunityPost,
    CommunityComment,
)
from ai_engine import generate_recommendations
from schemas import (
    TripResponse,
    UserSignup,
    UserLogin,
    UserResponse,
    AuthResponse,
    AITripRequest,
    AITripResponse,
    ExpenseCreate,
    ExpenseResponse,
    ExpenseSummaryResponse,
    PlaceHistoryResponse,
    CommunityPostCreate,
    CommunityPostResponse,
    CommunityCommentCreate,
    CommunityCommentResponse,
)
from crud import (
    get_trip,
    get_all_trips,
    get_user_by_email,
    get_user_by_id,
    create_user,
    create_traveler_expense,
    get_traveler_expenses,
    delete_traveler_expense,
    get_expense_summary,
    get_all_place_histories,
    get_place_history_by_name,
    create_community_post,
    get_community_posts,
    like_community_post,
    add_community_comment,
)

load_dotenv()

# =========================================================
# DATABASE
# =========================================================

Base.metadata.create_all(bind=engine)

# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="BengalTrail API",
    description="Backend API for BengalTrail tourism platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# JWT
# =========================================================

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "bengaltrail_super_secret_jwt_key_2026_secure")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

# =========================================================
# PASSWORDS
# =========================================================

def hash_password(password: str):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


# =========================================================
# JWT TOKEN
# =========================================================

def create_access_token(user_id: int):
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


# =========================================================
# CURRENT USER
# =========================================================

def get_current_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authentication required",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication format",
        )

    parts = authorization.split(" ", 1)

    if len(parts) != 2 or not parts[1]:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication format",
        )

    token = parts[1]

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        user_id = int(user_id)

    except (JWTError, ValueError, TypeError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/frontend/mainpage.html")


@app.get("/mainpage")
def mainpage():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/frontend/mainpage.html")


@app.get("/expenses")
def expenses_page():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/frontend/expenses.html")


@app.get("/community")
def community_page():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/frontend/community.html")




# =========================================================
# TRIPS
# =========================================================

@app.get(
    "/api/trips",
    response_model=list[TripResponse],
)
def get_trips(
    db: Session = Depends(get_db),
):
    return get_all_trips(db)


# =========================================================
# SINGLE TRIP
# =========================================================

@app.get(
    "/api/trips/{trip_id}",
    response_model=TripResponse,
)
def get_trip_details(
    trip_id: int,
    db: Session = Depends(get_db),
):
    trip = get_trip(db, trip_id)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    return trip


# =========================================================
# HOTELS FOR A TRIP
# =========================================================

@app.get("/api/trips/{trip_id}/hotels")
def get_trip_hotels(
    trip_id: int,
    db: Session = Depends(get_db),
):
    trip = (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    hotels = (
        db.query(Hotel)
        .filter(Hotel.trip_id == trip_id)
        .all()
    )

    return hotels


# =========================================================
# LOCATION SEARCH / VERIFICATION
#
# This is the missing endpoint in your current main.py.
#
# Frontend:
# GET /api/location/search?q=New%20Town%20Kolkata
#
# The endpoint:
# 1. Searches real locations
# 2. Restricts results to India
# 3. Rejects nonsense such as "cffweferw"
# 4. Returns exact latitude/longitude
# 5. Lets the user select the exact locality
#
# =========================================================

@app.get("/api/location/search")
def search_location(
    q: str = Query(..., min_length=3, max_length=150),
):
    query = q.strip()

    if len(query) < 3:
        raise HTTPException(
            status_code=422,
            detail="Please enter at least 3 characters.",
        )

    # Nominatim is used only for prototype location
    # verification/geocoding.
    #
    # countrycodes=in ensures that arbitrary places
    # outside India are not returned.

    params = (
        "q=" + quote_plus(query)
        + "&format=jsonv2"
        + "&addressdetails=1"
        + "&limit=5"
        + "&countrycodes=in"
        + "&accept-language=en"
    )

    url = (
        "https://nominatim.openstreetmap.org/search?"
        + params
    )

    request = Request(
        url,
        headers={
            "User-Agent": (
                "BengalTrailPrototype/1.0 "
                "(travel-planner-local-development)"
            ),
        },
    )

    try:
        with urlopen(
            request,
            timeout=10,
        ) as response:
            raw_data = response.read().decode(
                "utf-8"
            )

        places = json.loads(raw_data)

    except Exception as error:
        print(
            "Location search error:",
            repr(error),
        )

        raise HTTPException(
            status_code=503,
            detail=(
                "Location verification service is "
                "temporarily unavailable. Please try again."
            ),
        )

    results = []

    # Broad result types are kept but marked so the
    # frontend can tell the user to prefer an exact
    # locality/area for large cities.

    broad_types = {
        "city",
        "town",
        "municipality",
        "county",
        "state",
        "region",
    }

    preferred_types = {
        "suburb",
        "neighbourhood",
        "village",
        "hamlet",
        "quarter",
        "residential",
        "locality",
        "station",
        "aerodrome",
    }

    for place in places:
        try:
            latitude = float(place["lat"])
            longitude = float(place["lon"])
        except (
            KeyError,
            TypeError,
            ValueError,
        ):
            continue

        address = place.get("address") or {}

        country_code = (
            address.get("country_code")
            or ""
        ).lower()

        if country_code != "in":
            continue

        place_type = (
            place.get("type")
            or ""
        ).lower()

        precision = (
            "exact"
            if place_type in preferred_types
            else "broad"
            if place_type in broad_types
            else "standard"
        )

        results.append({
            "display_name": place.get(
                "display_name",
                query,
            ),
            "latitude": latitude,
            "longitude": longitude,
            "type": place_type,
            "precision": precision,
            "city": (
                address.get("city")
                or address.get("town")
                or address.get("municipality")
                or address.get("village")
                or ""
            ),
            "state": (
                address.get("state")
                or ""
            ),
            "country": (
                address.get("country")
                or "India"
            ),
        })

    if not results:
        raise HTTPException(
            status_code=404,
            detail=(
                "No matching Indian location was found. "
                "Try a more specific place such as "
                "'Salt Lake Kolkata', 'New Town Kolkata', "
                "'NJP', 'Siliguri', or another locality."
            ),
        )

    # Exact localities first, broad city-level results later.
    results.sort(
        key=lambda item: (
            0 if item["precision"] == "exact" else
            1 if item["precision"] == "standard" else
            2
        )
    )

    return {
        "query": query,
        "results": results[:5],
    }


# =========================================================
# AI TRIP PLANNER
# =========================================================

@app.post(
    "/api/ai/plan",
    response_model=AITripResponse,
)
def ai_trip_planner(
    request: AITripRequest,
    db: Session = Depends(get_db),
):
    try:
        # -------------------------------------------------
        # Validate date
        # -------------------------------------------------

        try:
            visit_date = datetime.strptime(
                request.travel_date,
                "%Y-%m-%d",
            )
        except ValueError:
            raise HTTPException(
                status_code=422,
                detail=(
                    "Travel date must be in "
                    "YYYY-MM-DD format."
                ),
            )

        # -------------------------------------------------
        # Coordinates are mandatory.
        #
        # They come from /api/location/search after the
        # user selects a verified location.
        # -------------------------------------------------

        starting_latitude = float(
            request.starting_latitude
        )

        starting_longitude = float(
            request.starting_longitude
        )

        # India bounds
        if not (
            6.0
            <= starting_latitude
            <= 37.5
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid starting latitude.",
            )

        if not (
            68.0
            <= starting_longitude
            <= 98.0
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid starting longitude.",
            )

        # -------------------------------------------------
        # IMPORTANT:
        # Pass coordinates directly into ai_engine.
        #
        # ai_engine.py already supports this dictionary
        # format.
        # -------------------------------------------------

        starting_location = {
            "name": request.starting_location,
            "latitude": starting_latitude,
            "longitude": starting_longitude,
        }

        print(
            "\n========================================"
        )
        print("AI TRIP PLANNER REQUEST")
        print(
            "Starting:",
            request.starting_location,
        )
        print(
            "Latitude:",
            starting_latitude,
        )
        print(
            "Longitude:",
            starting_longitude,
        )
        print(
            "Date:",
            request.travel_date,
        )
        print(
            "People:",
            request.people,
        )
        print(
            "Budget:",
            request.budget,
        )
        print(
            "Experience:",
            request.experience,
        )
        print(
            "Duration:",
            request.duration,
        )
        print(
            "Transport:",
            request.transport,
        )
        print(
            "Weather:",
            request.weather_preference,
        )
        print(
            "Footfall:",
            request.footfall_preference,
        )
        print(
            "========================================\n"
        )

        # -------------------------------------------------
        # Generate recommendations
        # -------------------------------------------------

        recommendations = generate_recommendations(
            db=db,
            starting_location=starting_location,
            experience=request.experience,
            budget=request.budget,
            people=request.people,
            duration=request.duration,
            transport=request.transport,
            visit_date=visit_date,
            weather_preference=request.weather_preference,
            footfall_preference=request.footfall_preference,
        )

        if recommendations is None:
            recommendations = []

        print(
            "AI recommendations generated:",
            len(recommendations),
        )

        return {
            "recommendations": recommendations
        }

    except HTTPException:
        raise

    except ValueError as error:
        print(
            "\nAI PLANNER VALIDATION ERROR:",
            repr(error),
            "\n",
        )

        raise HTTPException(
            status_code=422,
            detail=str(error),
        )

    except Exception as error:
        # Keep the real error visible in the terminal.
        print(
            "\n========================================"
        )
        print("AI PLANNER ERROR")
        print(
            "TYPE:",
            type(error).__name__,
        )
        print(
            "ERROR:",
            repr(error),
        )
        print(
            "========================================\n"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "AI planner failed: "
                f"{str(error)}"
            ),
        )


# =========================================================
# SIGN UP
# =========================================================

@app.post(
    "/api/signup",
    response_model=AuthResponse,
)
def signup(
    user_data: UserSignup,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(
        db,
        user_data.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    if len(user_data.password) < 6:
        raise HTTPException(
            status_code=400,
            detail=(
                "Password must be at least "
                "6 characters"
            ),
        )

    password_hash = hash_password(
        user_data.password
    )

    user = create_user(
        db=db,
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=password_hash,
    )

    token = create_access_token(
        user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


# =========================================================
# LOGIN
# =========================================================

@app.post(
    "/api/login",
    response_model=AuthResponse,
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = get_user_by_email(
        db,
        user_data.email,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


# =========================================================
# CHECK AUTH
# =========================================================

@app.get("/api/check-auth")
def check_auth(
    current_user: User = Depends(
        get_current_user
    ),
):
    return {
        "logged_in": True,
        "user": {
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email,
        },
    }


# =========================================================
# PROFILE
# =========================================================

@app.get(
    "/api/profile",
    response_model=UserResponse,
)
def get_profile(
    current_user: User = Depends(
        get_current_user
    ),
):
    return current_user


# =========================================================
# LOGOUT
# =========================================================

@app.post("/api/logout")
def logout():
    return {
        "success": True,
        "message": "Logged out successfully",
    }


# =========================================================
# UPLOADS
# =========================================================

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

app.mount(
    "/uploads",
    StaticFiles(
        directory="uploads"
    ),
    name="uploads",
)


# =========================================================
# FRONTEND STATIC DIRECTORY
# =========================================================

FRONTEND_DIR = (
    Path(__file__).resolve().parent.parent
    / "frontend"
)

if FRONTEND_DIR.exists():
    app.mount(
        "/frontend",
        StaticFiles(
            directory=FRONTEND_DIR
        ),
        name="frontend",
    )

    ASSETS_DIR = FRONTEND_DIR / "assets"
    if ASSETS_DIR.exists():
        app.mount(
            "/assets",
            StaticFiles(
                directory=ASSETS_DIR
            ),
            name="assets",
        )


# =========================================================
# PROFILE PHOTO
# =========================================================

@app.post("/api/profile/photo")
async def upload_profile_photo(
    file: UploadFile = File(...),
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):
    allowed_types = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=(
                "Only JPG, PNG and WEBP "
                "images are allowed"
            ),
        )

    contents = await file.read()

    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=(
                "Image must be smaller "
                "than 5 MB"
            ),
        )

    extension = allowed_types[
        file.content_type
    ]

    filename = (
        f"user_{current_user.id}_"
        f"{uuid.uuid4().hex}"
        f"{extension}"
    )

    file_path = (
        UPLOAD_DIR / filename
    )

    with open(
        file_path,
        "wb",
    ) as buffer:
        buffer.write(contents)

    current_user.profile_image = (
        f"/uploads/{filename}"
    )

    db.commit()
    db.refresh(current_user)

    return {
        "success": True,
        "message": (
            "Profile photo uploaded successfully"
        ),
        "profile_image":
            current_user.profile_image,
    }


# =========================================================
# TRAVELER EXPENSE API ENDPOINTS
# =========================================================

@app.post(
    "/api/expenses",
    response_model=ExpenseResponse,
    status_code=201,
)
def add_expense(
    expense: ExpenseCreate,
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Log an expense spent by a traveler (Bus, Train, Toto, Homestay, Food, etc.).
    Associates with user if Authorization token is provided.
    """
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
        except JWTError:
            pass

    created = create_traveler_expense(
        db=db,
        expense_data=expense.model_dump(),
        user_id=user_id,
    )
    return created


@app.get(
    "/api/expenses",
    response_model=list[ExpenseResponse],
)
def list_expenses(
    sub_category: str = Query(None, description="Filter by Bus, Train, Toto, Homestay, Food"),
    destination: str = Query(None, description="Filter by destination"),
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Get all logged expenses with optional filtering.
    """
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
        except JWTError:
            pass

    return get_traveler_expenses(
        db=db,
        user_id=user_id,
        sub_category=sub_category,
        destination=destination,
    )


@app.get(
    "/api/expenses/summary",
    response_model=ExpenseSummaryResponse,
)
def get_expenses_summary(
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Get aggregated summary: total spend, transit total, homestay total, food total, and subcategory breakdown.
    """
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
        except JWTError:
            pass

    return get_expense_summary(db=db, user_id=user_id)


@app.delete(
    "/api/expenses/{expense_id}",
)
def remove_expense(
    expense_id: int,
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Delete an expense entry.
    """
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
        except JWTError:
            pass

    deleted = delete_traveler_expense(db, expense_id=expense_id, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"success": True, "message": "Expense deleted successfully"}


@app.get(
    "/api/rates",
)
def get_standard_rates(
    destination: str = Query(None),
    expense_type: str = Query(None),
    db: Session = Depends(get_db),
):
    """
    Returns reference rate card for North Bengal travel (Toto, Bus, Train, Homestay, Food benchmark fares).
    """
    query = db.query(StandardRate)
    if destination:
        query = query.filter(StandardRate.destination.ilike(f"%{destination}%"))
    if expense_type:
        query = query.filter(StandardRate.expense_type.ilike(f"%{expense_type}%"))
    rates = query.all()
    return rates


# =========================================================
# PLACE HISTORY & WEATHER ENDPOINTS
# =========================================================

@app.get(
    "/api/places/history",
    response_model=list[PlaceHistoryResponse],
)
def list_place_histories(
    query: str = Query(None, description="Search by place or district"),
    db: Session = Depends(get_db),
):
    """
    Get comprehensive history, heritage, weather, altitude, and transport guide for North Bengal places.
    """
    return get_all_place_histories(db, query=query)


@app.get(
    "/api/places/history/{destination_name}",
    response_model=PlaceHistoryResponse,
)
def get_single_place_history(
    destination_name: str,
    db: Session = Depends(get_db),
):
    """
    Get full history, origin of name, landmarks, and current weather for a specific destination.
    """
    record = get_place_history_by_name(db, destination_name=destination_name)
    if not record:
        raise HTTPException(status_code=404, detail="Destination history not found")
    return record


# =========================================================
# COMMUNITY PLATFORM ENDPOINTS (TOURIST REVIEWS & LOCAL GEMS)
# =========================================================

@app.get(
    "/api/community/posts",
    response_model=list[CommunityPostResponse],
)
def list_community_posts(
    author_type: str = Query(None, description="Filter: 'Tourist' or 'Local Resident' or 'All'"),
    destination: str = Query(None, description="Filter by destination"),
    post_type: str = Query(None, description="Filter: 'Tourist Review', 'Local Suggestion', 'Hidden Gem'"),
    db: Session = Depends(get_db),
):
    """
    List community reviews and suggestions shared by tourists and local residents,
    including expense breakdowns and weather notes.
    """
    return get_community_posts(
        db=db,
        author_type=author_type,
        destination_name=destination,
        post_type=post_type,
    )


@app.post(
    "/api/community/posts",
    response_model=CommunityPostResponse,
    status_code=201,
)
def create_new_community_post(
    post: CommunityPostCreate,
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Create a new community post:
    - Tourists can share their reviews, photos, ratings, and actual trip expenses.
    - Local residents can share hidden tourist places, secret viewpoints, tips, and expected expenses.
    """
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
        except JWTError:
            pass

    created = create_community_post(
        db=db,
        post_data=post.model_dump(),
        user_id=user_id,
    )
    return {
        "id": created.id,
        "user_id": created.user_id,
        "author_name": created.author_name,
        "author_type": created.author_type,
        "author_location": created.author_location,
        "destination_name": created.destination_name,
        "title": created.title,
        "post_type": created.post_type,
        "rating": created.rating,
        "content": created.content,
        "total_expense": created.total_expense,
        "expense_breakdown": created.expense_breakdown,
        "weather_note": created.weather_note,
        "image_url": created.image_url,
        "likes_count": created.likes_count,
        "created_at": created.created_at,
        "comments": []
    }


@app.post(
    "/api/community/posts/{post_id}/like",
)
def like_post(
    post_id: int,
    db: Session = Depends(get_db),
):
    """
    Upvote / like a community post.
    """
    likes = like_community_post(db, post_id=post_id)
    if likes is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"success": True, "likes_count": likes}


@app.post(
    "/api/community/posts/{post_id}/comments",
    response_model=CommunityCommentResponse,
    status_code=201,
)
def add_comment(
    post_id: int,
    comment: CommunityCommentCreate,
    db: Session = Depends(get_db),
):
    """
    Add a comment / reply to a community post (tourists asking locals questions, or locals giving tips).
    """
    return add_community_comment(
        db=db,
        post_id=post_id,
        author_name=comment.author_name,
        author_type=comment.author_type,
        content=comment.content,
    )

