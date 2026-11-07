from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)

from database import Base

from datetime import datetime


# =========================================================
# TRIP MODEL
# =========================================================

class Trip(Base):

    __tablename__ = "trips"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    category = Column(
        String(100)
    )

    route = Column(
        String(500)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float,
        default=0
    )

    reviews = Column(
        Integer,
        default=0
    )

    price = Column(
        Float
    )

    duration = Column(
        String(100)
    )

    difficulty = Column(
        String(50)
    )

    description = Column(
        Text
    )

    tags = Column(
        String(500)
    )

    recommended_for = Column(
        String(500)
    )

    ai_match = Column(
        Integer,
        default=0
    )


# =========================================================
# USER MODEL
# =========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    profile_image = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# AI DESTINATION MODEL
# =========================================================

class Destination(Base):

    __tablename__ = "destinations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    district = Column(
        String(100)
    )

    category = Column(
        String(150)
    )

    description = Column(
        Text
    )

    best_for = Column(
        String(500)
    )

    tags = Column(
        String(500)
    )

    average_stay = Column(
        Integer,
        default=2
    )

    base_cost_per_person = Column(
        Float,
        default=0
    )

    hotel_cost_per_night = Column(
        Float,
        default=0
    )

    food_cost_per_day = Column(
        Float,
        default=0
    )

    transport_cost = Column(
        Float,
        default=0
    )

    rating = Column(
        Float,
        default=0
    )

    image = Column(
        String(500),
        nullable=True
    )

    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )


# =========================================================
# AI TRANSPORT COST MODEL
# =========================================================

class TravelCost(Base):

    __tablename__ = "travel_costs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    transport_type = Column(
        String(50),
        nullable=False
    )

    estimated_cost = Column(
        Float,
        default=0
    )

    duration_hours = Column(
        Float,
        default=0
    )

    comfort_level = Column(
        String(50)
    )


# =========================================================
# AI FOOTFALL MODEL
# =========================================================

class FootfallData(Base):

    __tablename__ = "footfall_data"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    visit_date = Column(
        DateTime,
        nullable=False
    )

    crowd_level = Column(
        String(50),
        nullable=False
    )

    crowd_score = Column(
        Integer,
        default=50
    )

    estimated_visitors = Column(
        Integer,
        default=0
    )


# =========================================================
# HOTEL MODEL
# =========================================================

class Hotel(Base):

    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    name = Column(
        String(200),
        nullable=False
    )

    location = Column(
        String(200)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float
    )

    price_per_night = Column(
        Float
    )

    room_type = Column(
        String(100)
    )

    facilities = Column(
        Text
    )

    available_rooms = Column(
        Integer,
        default=0
    )

    description = Column(
        Text
    )


# =========================================================
# TRAVELER EXPENSE MODEL
# =========================================================

class TravelerExpense(Base):

    __tablename__ = "traveler_expenses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=True
    )

    destination_name = Column(
        String(100),
        nullable=False
    )

    category = Column(
        String(50),
        nullable=False,
        default="Transport"
    )

    sub_category = Column(
        String(50),
        nullable=False
    )

    item_title = Column(
        String(200),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_method = Column(
        String(50),
        default="UPI / GPay / PhonePe"
    )

    origin_point = Column(
        String(150),
        nullable=True
    )

    destination_point = Column(
        String(150),
        nullable=True
    )

    expense_date = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    number_of_people = Column(
        Integer,
        default=1
    )

    notes = Column(
        Text,
        nullable=True
    )

    receipt_image_url = Column(
        String(500),
        nullable=True
    )

    is_estimated = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# STANDARD RATES BENCHMARK MODEL
# =========================================================

class StandardRate(Base):

    __tablename__ = "standard_rates"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(100),
        nullable=False
    )

    expense_type = Column(
        String(50),
        nullable=False
    )

    route_or_service = Column(
        String(200),
        nullable=False
    )

    estimated_cost = Column(
        Float,
        nullable=False
    )

    cost_unit = Column(
        String(50),
        default="per person"
    )

    notes = Column(
        Text,
        nullable=True
    )


# =========================================================
# PLACE HISTORY & WEATHER MODEL
# =========================================================

class PlaceHistory(Base):

    __tablename__ = "place_histories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination_name = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    district = Column(
        String(100),
        nullable=True
    )

    tagline = Column(
        String(250),
        nullable=True
    )

    name_etymology = Column(
        Text,
        nullable=True
    )

    history_full = Column(
        Text,
        nullable=False
    )

    colonial_era = Column(
        Text,
        nullable=True
    )

    cultural_heritage = Column(
        Text,
        nullable=True
    )

    historical_landmarks = Column(
        Text,
        nullable=True
    )

    current_weather = Column(
        String(100),
        nullable=True
    )

    temperature_range = Column(
        String(50),
        nullable=True
    )

    weather_condition = Column(
        String(100),
        nullable=True
    )

    best_season_to_visit = Column(
        String(200),
        nullable=True
    )

    altitude = Column(
        String(100),
        nullable=True
    )

    local_transport_guide = Column(
        Text,
        nullable=True
    )

    image_url = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# COMMUNITY POST MODEL (TOURIST REVIEWS & LOCAL SUGGESTIONS)
# =========================================================

class CommunityPost(Base):

    __tablename__ = "community_posts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    author_name = Column(
        String(120),
        nullable=False
    )

    author_type = Column(
        String(50),
        nullable=False,
        default="Tourist"
    )

    author_location = Column(
        String(120),
        nullable=True
    )

    destination_name = Column(
        String(150),
        nullable=False
    )

    title = Column(
        String(250),
        nullable=False
    )

    post_type = Column(
        String(50),
        nullable=False,
        default="Tourist Review"
    )

    rating = Column(
        Float,
        default=5.0
    )

    content = Column(
        Text,
        nullable=False
    )

    total_expense = Column(
        Float,
        default=0.0
    )

    expense_breakdown = Column(
        String(500),
        nullable=True
    )

    weather_note = Column(
        String(200),
        nullable=True
    )

    image_url = Column(
        String(500),
        nullable=True
    )

    likes_count = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# COMMUNITY COMMENT MODEL
# =========================================================

class CommunityComment(Base):

    __tablename__ = "community_comments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    post_id = Column(
        Integer,
        ForeignKey("community_posts.id"),
        nullable=False
    )

    author_name = Column(
        String(120),
        nullable=False
    )

    author_type = Column(
        String(50),
        default="Tourist"
    )

    content = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
