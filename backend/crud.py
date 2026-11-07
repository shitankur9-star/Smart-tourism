from sqlalchemy.orm import Session
from datetime import datetime
from models import (
    Trip,
    User,
    TravelerExpense,
    StandardRate,
    PlaceHistory,
    CommunityPost,
    CommunityComment,
)



# ==========================================
# TRIP FUNCTIONS
# ==========================================

def get_trip(db: Session, trip_id: int):

    return (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )


def get_all_trips(db: Session):

    return (
        db.query(Trip)
        .order_by(Trip.id)
        .all()
    )


# ==========================================
# USER FUNCTIONS
# ==========================================

def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_user_by_id(
    db: Session,
    user_id: int
):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password_hash: str
):

    user = User(
        full_name=full_name,
        email=email,
        password_hash=password_hash
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


# ==========================================
# EXPENSE FUNCTIONS
# ==========================================

def create_traveler_expense(
    db: Session,
    expense_data: dict,
    user_id: int = None
):
    expense = TravelerExpense(
        user_id=user_id,
        trip_id=expense_data.get("trip_id"),
        destination_name=expense_data.get("destination_name"),
        category=expense_data.get("category", "Transport"),
        sub_category=expense_data.get("sub_category"),
        item_title=expense_data.get("item_title"),
        amount=expense_data.get("amount"),
        payment_method=expense_data.get("payment_method", "UPI / GPay / PhonePe"),
        origin_point=expense_data.get("origin_point"),
        destination_point=expense_data.get("destination_point"),
        expense_date=expense_data.get("expense_date") or datetime.utcnow(),
        number_of_people=expense_data.get("number_of_people", 1),
        notes=expense_data.get("notes")
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def get_traveler_expenses(
    db: Session,
    user_id: int = None,
    sub_category: str = None,
    destination: str = None
):
    query = db.query(TravelerExpense)
    if user_id is not None:
        query = query.filter(TravelerExpense.user_id == user_id)
    if sub_category:
        query = query.filter(TravelerExpense.sub_category.ilike(f"%{sub_category}%"))
    if destination:
        query = query.filter(TravelerExpense.destination_name.ilike(f"%{destination}%"))
    return query.order_by(TravelerExpense.expense_date.desc()).all()


def delete_traveler_expense(
    db: Session,
    expense_id: int,
    user_id: int = None
):
    query = db.query(TravelerExpense).filter(TravelerExpense.id == expense_id)
    if user_id is not None:
        query = query.filter(TravelerExpense.user_id == user_id)
    expense = query.first()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False


def get_expense_summary(db: Session, user_id: int = None):
    expenses = get_traveler_expenses(db, user_id=user_id)
    total = sum(e.amount for e in expenses)
    transport_subcats = {"Toto", "Bus", "Train", "Shared Jeep", "Taxi", "Cab"}
    homestay_subcats = {"Homestay", "Hotel", "Resort", "Lodge"}
    food_subcats = {"Food", "Meal", "Restaurant", "Snacks", "Tea"}

    transport_total = sum(e.amount for e in expenses if e.sub_category in transport_subcats or e.category == "Transport")
    homestay_total = sum(e.amount for e in expenses if e.sub_category in homestay_subcats or e.category in {"Homestay & Lodging", "Accommodation"})
    food_total = sum(e.amount for e in expenses if e.sub_category in food_subcats or e.category == "Food & Dining")
    other_total = total - (transport_total + homestay_total + food_total)

    breakdown = {}
    for e in expenses:
        sub = e.sub_category or "Other"
        breakdown[sub] = breakdown.get(sub, 0.0) + float(e.amount)

    return {
        "total_amount": round(total, 2),
        "transport_total": round(transport_total, 2),
        "homestay_total": round(homestay_total, 2),
        "food_total": round(food_total, 2),
        "other_total": round(max(0, other_total), 2),
        "breakdown_by_subcategory": breakdown,
        "count": len(expenses)
    }


# ==========================================
# PLACE HISTORY & WEATHER FUNCTIONS
# ==========================================

def get_all_place_histories(db: Session, query: str = None):
    q = db.query(PlaceHistory)
    if query:
        q = q.filter(
            PlaceHistory.destination_name.ilike(f"%{query}%") |
            PlaceHistory.district.ilike(f"%{query}%")
        )
    return q.order_by(PlaceHistory.destination_name).all()


def get_place_history_by_name(db: Session, destination_name: str):
    return (
        db.query(PlaceHistory)
        .filter(PlaceHistory.destination_name.ilike(destination_name))
        .first()
    )


# ==========================================
# COMMUNITY FUNCTIONS
# ==========================================

def create_community_post(
    db: Session,
    post_data: dict,
    user_id: int = None
):
    post = CommunityPost(
        user_id=user_id,
        author_name=post_data.get("author_name"),
        author_type=post_data.get("author_type", "Tourist"),
        author_location=post_data.get("author_location"),
        destination_name=post_data.get("destination_name"),
        title=post_data.get("title"),
        post_type=post_data.get("post_type", "Tourist Review"),
        rating=post_data.get("rating", 5.0),
        content=post_data.get("content"),
        total_expense=post_data.get("total_expense", 0.0),
        expense_breakdown=post_data.get("expense_breakdown"),
        weather_note=post_data.get("weather_note"),
        image_url=post_data.get("image_url")
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_community_posts(
    db: Session,
    author_type: str = None,
    destination_name: str = None,
    post_type: str = None,
    limit: int = 50
):
    query = db.query(CommunityPost)
    if author_type and author_type.lower() != "all":
        query = query.filter(CommunityPost.author_type.ilike(author_type))
    if destination_name:
        query = query.filter(CommunityPost.destination_name.ilike(f"%{destination_name}%"))
    if post_type:
        query = query.filter(CommunityPost.post_type.ilike(post_type))

    posts = query.order_by(CommunityPost.created_at.desc()).limit(limit).all()

    # Attach comments to each post
    result = []
    for p in posts:
        comments = (
            db.query(CommunityComment)
            .filter(CommunityComment.post_id == p.id)
            .order_by(CommunityComment.created_at.asc())
            .all()
        )
        post_dict = {
            "id": p.id,
            "user_id": p.user_id,
            "author_name": p.author_name,
            "author_type": p.author_type,
            "author_location": p.author_location,
            "destination_name": p.destination_name,
            "title": p.title,
            "post_type": p.post_type,
            "rating": p.rating,
            "content": p.content,
            "total_expense": p.total_expense,
            "expense_breakdown": p.expense_breakdown,
            "weather_note": p.weather_note,
            "image_url": p.image_url,
            "likes_count": p.likes_count,
            "created_at": p.created_at,
            "comments": comments
        }
        result.append(post_dict)
    return result


def like_community_post(db: Session, post_id: int):
    post = db.query(CommunityPost).filter(CommunityPost.id == post_id).first()
    if post:
        post.likes_count = (post.likes_count or 0) + 1
        db.commit()
        db.refresh(post)
        return post.likes_count
    return None


def add_community_comment(
    db: Session,
    post_id: int,
    author_name: str,
    content: str,
    author_type: str = "Tourist"
):
    comment = CommunityComment(
        post_id=post_id,
        author_name=author_name,
        author_type=author_type,
        content=content
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment



