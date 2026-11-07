from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# =========================================================
# TRIP RESPONSE
# =========================================================

class TripResponse(BaseModel):

    id: int

    title: str

    category: Optional[str] = None

    route: Optional[str] = None

    image: Optional[str] = None

    rating: float

    reviews: int

    price: Optional[float] = None

    duration: Optional[str] = None

    difficulty: Optional[str] = None

    description: Optional[str] = None

    tags: Optional[str] = None

    recommended_for: Optional[str] = None

    ai_match: int

    class Config:
        from_attributes = True


# =========================================================
# SIGN UP
# =========================================================

class UserSignup(BaseModel):

    full_name: str

    email: EmailStr

    password: str


# =========================================================
# LOGIN
# =========================================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str


# =========================================================
# USER RESPONSE
# =========================================================

class UserResponse(BaseModel):

    id: int

    full_name: str

    email: str

    profile_image: Optional[str] = None

    created_at: datetime

    class Config:
        from_attributes = True


# =========================================================
# AUTH RESPONSE
# =========================================================

class AuthResponse(BaseModel):

    access_token: str

    token_type: str


# =========================================================
# AI TRIP PLANNER REQUEST
# =========================================================
#
# IMPORTANT:
#
# starting_location
#     = human-readable selected location
#
# starting_latitude
# starting_longitude
#     = exact coordinates returned by the
#       location verification system
#
# The AI engine should use the coordinates
# for distance and travel-cost calculation.
#
# =========================================================

class AITripRequest(BaseModel):

    # -----------------------------------------------------
    # STARTING LOCATION
    # -----------------------------------------------------

    starting_location: str = Field(

        ...,

        min_length=2,

        description=(
            "Verified starting location selected "
            "by the user."
        )
    )


    # -----------------------------------------------------
    # STARTING LOCATION COORDINATES
    # -----------------------------------------------------

    starting_latitude: float = Field(

        ...,

        ge=6.0,

        le=37.5,

        description=(
            "Latitude of the verified starting "
            "location in India."
        )
    )


    starting_longitude: float = Field(

        ...,

        ge=68.0,

        le=98.0,

        description=(
            "Longitude of the verified starting "
            "location in India."
        )
    )


    # -----------------------------------------------------
    # TRAVEL DATE
    # -----------------------------------------------------

    travel_date: str = Field(

        ...,

        min_length=8,

        description=(
            "Travel date in YYYY-MM-DD format."
        )
    )


    # -----------------------------------------------------
    # NUMBER OF PEOPLE
    # -----------------------------------------------------

    people: int = Field(

        ...,

        ge=1,

        le=100,

        description=(
            "Number of people travelling."
        )
    )


    # -----------------------------------------------------
    # TOTAL BUDGET
    # -----------------------------------------------------

    budget: float = Field(

        ...,

        gt=0,

        description=(
            "Maximum total trip budget in INR."
        )
    )


    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

    experience: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred travel experience."
        )
    )


    # -----------------------------------------------------
    # TRIP DURATION
    # -----------------------------------------------------

    duration: int = Field(

        ...,

        ge=1,

        le=60,

        description=(
            "Trip duration in days."
        )
    )


    # -----------------------------------------------------
    # TRANSPORT
    # -----------------------------------------------------

    transport: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred transport type."
        )
    )


    # -----------------------------------------------------
    # WEATHER PREFERENCE
    # -----------------------------------------------------

    weather_preference: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred weather condition."
        )
    )


    # -----------------------------------------------------
    # FOOTFALL PREFERENCE
    # -----------------------------------------------------

    footfall_preference: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred destination crowd level."
        )
    )


# =========================================================
# AI TRIP RESULT
# =========================================================

class AITripResponse(BaseModel):

    recommendations: list


# =========================================================
# TRAVELER EXPENSE SCHEMAS
# =========================================================

class ExpenseCreate(BaseModel):

    destination_name: str
    category: Optional[str] = "Transport"
    sub_category: str
    item_title: str
    amount: float
    payment_method: Optional[str] = "UPI / GPay / PhonePe"
    origin_point: Optional[str] = None
    destination_point: Optional[str] = None
    expense_date: Optional[datetime] = None
    number_of_people: Optional[int] = 1
    notes: Optional[str] = None
    trip_id: Optional[int] = None


class ExpenseResponse(BaseModel):

    id: int
    user_id: Optional[int] = None
    trip_id: Optional[int] = None
    destination_name: str
    category: str
    sub_category: str
    item_title: str
    amount: float
    payment_method: str
    origin_point: Optional[str] = None
    destination_point: Optional[str] = None
    expense_date: datetime
    number_of_people: int
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ExpenseSummaryResponse(BaseModel):

    total_amount: float
    transport_total: float
    homestay_total: float
    food_total: float
    other_total: float
    breakdown_by_subcategory: dict
    count: int


# =========================================================
# PLACE HISTORY & WEATHER SCHEMAS
# =========================================================

class PlaceHistoryResponse(BaseModel):

    id: int
    destination_name: str
    district: Optional[str] = None
    tagline: Optional[str] = None
    name_etymology: Optional[str] = None
    history_full: str
    colonial_era: Optional[str] = None
    cultural_heritage: Optional[str] = None
    historical_landmarks: Optional[str] = None
    current_weather: Optional[str] = None
    temperature_range: Optional[str] = None
    weather_condition: Optional[str] = None
    best_season_to_visit: Optional[str] = None
    altitude: Optional[str] = None
    local_transport_guide: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        from_attributes = True


# =========================================================
# COMMUNITY POST SCHEMAS
# =========================================================

class CommunityPostCreate(BaseModel):

    author_name: str
    author_type: Optional[str] = "Tourist"
    author_location: Optional[str] = None
    destination_name: str
    title: str
    post_type: Optional[str] = "Tourist Review"
    rating: Optional[float] = 5.0
    content: str
    total_expense: Optional[float] = 0.0
    expense_breakdown: Optional[str] = None
    weather_note: Optional[str] = None
    image_url: Optional[str] = None


class CommunityCommentCreate(BaseModel):

    author_name: str
    author_type: Optional[str] = "Tourist"
    content: str


class CommunityCommentResponse(BaseModel):

    id: int
    post_id: int
    author_name: str
    author_type: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class CommunityPostResponse(BaseModel):

    id: int
    user_id: Optional[int] = None
    author_name: str
    author_type: str
    author_location: Optional[str] = None
    destination_name: str
    title: str
    post_type: str
    rating: float
    content: str
    total_expense: float
    expense_breakdown: Optional[str] = None
    weather_note: Optional[str] = None
    image_url: Optional[str] = None
    likes_count: int
    created_at: datetime
    comments: Optional[list[CommunityCommentResponse]] = []

    class Config:
        from_attributes = True

