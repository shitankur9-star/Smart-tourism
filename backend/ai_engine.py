


#     # =====================================================
#     # RETURN TOP 5
#     # =====================================================

#     return recommendations[:5]
from math import radians, sin, cos, sqrt, atan2

from sqlalchemy.orm import Session

from models import (
    Destination,
    FootfallData
)


# =========================================================
# VERIFIED STARTING LOCATIONS
# =========================================================
#
# These are recognized locations.
#
# IMPORTANT:
# Do NOT silently accept arbitrary text.
#
# If the user enters something that is not recognized,
# generate_recommendations() will raise ValueError.
#
# Later, you can replace/extend this with a real
# geocoding service.
#
# =========================================================

STARTING_LOCATIONS = {

    # =====================================================
    # KOLKATA
    # =====================================================

    "kolkata": {
        "latitude": 22.5726,
        "longitude": 88.3639
    },

    "new town": {
        "latitude": 22.5958,
        "longitude": 88.4797
    },

    "newtown": {
        "latitude": 22.5958,
        "longitude": 88.4797
    },

    "new town kolkata": {
        "latitude": 22.5958,
        "longitude": 88.4797
    },

    "salt lake": {
        "latitude": 22.5804,
        "longitude": 88.4142
    },

    "salt lake kolkata": {
        "latitude": 22.5804,
        "longitude": 88.4142
    },

    "bidhannagar": {
        "latitude": 22.5841,
        "longitude": 88.4177
    },

    "howrah": {
        "latitude": 22.5958,
        "longitude": 88.2636
    },

    "dum dum": {
        "latitude": 22.6527,
        "longitude": 88.4467
    },

    "dum dum kolkata": {
        "latitude": 22.6527,
        "longitude": 88.4467
    },

    "kolkata airport": {
        "latitude": 22.6547,
        "longitude": 88.4467
    },

    "netaji subhash chandra bose international airport": {
        "latitude": 22.6547,
        "longitude": 88.4467
    },

    "airport kolkata": {
        "latitude": 22.6547,
        "longitude": 88.4467
    },

    "behala": {
        "latitude": 22.4930,
        "longitude": 88.3100
    },

    "garia": {
        "latitude": 22.4627,
        "longitude": 88.3833
    },

    "jadavpur": {
        "latitude": 22.4991,
        "longitude": 88.3714
    },

    "park street": {
        "latitude": 22.5535,
        "longitude": 88.3520
    },

    "esplanade": {
        "latitude": 22.5650,
        "longitude": 88.3510
    },

    # =====================================================
    # NORTH BENGAL
    # =====================================================

    "siliguri": {
        "latitude": 26.7271,
        "longitude": 88.3953
    },

    "siliguri junction": {
        "latitude": 26.7271,
        "longitude": 88.3953
    },

    "njp": {
        "latitude": 26.6828,
        "longitude": 88.4465
    },

    "new jalpaiguri": {
        "latitude": 26.6828,
        "longitude": 88.4465
    },

    "new jalpaiguri station": {
        "latitude": 26.6828,
        "longitude": 88.4465
    },

    "darjeeling": {
        "latitude": 27.0410,
        "longitude": 88.2663
    },

    "kalimpong": {
        "latitude": 27.0667,
        "longitude": 88.4667
    },

    "malda": {
        "latitude": 25.0108,
        "longitude": 88.1411
    },

    # =====================================================
    # SOUTH / CENTRAL WEST BENGAL
    # =====================================================

    "durgapur": {
        "latitude": 23.5204,
        "longitude": 87.3119
    },

    "asansol": {
        "latitude": 23.6739,
        "longitude": 86.9524
    },

    "bardhaman": {
        "latitude": 23.2324,
        "longitude": 87.8615
    },

    "burdwan": {
        "latitude": 23.2324,
        "longitude": 87.8615
    },

    "krishnanagar": {
        "latitude": 23.4058,
        "longitude": 88.4907
    },

    "berhampore": {
        "latitude": 24.0988,
        "longitude": 88.2676
    },

    "baharampur": {
        "latitude": 24.0988,
        "longitude": 88.2676
    },

    # =====================================================
    # ASSAM
    # =====================================================

    "guwahati": {
        "latitude": 26.1445,
        "longitude": 91.7362
    },

    "guwahati airport": {
        "latitude": 26.1061,
        "longitude": 91.5859
    },

    "lokpriya gopinath bordoloi international airport": {
        "latitude": 26.1061,
        "longitude": 91.5859
    },

    # =====================================================
    # MEGHALAYA
    # =====================================================

    "shillong": {
        "latitude": 25.5788,
        "longitude": 91.8933
    }
}


# =========================================================
# VERIFIED DESTINATION COORDINATES
# =========================================================
#
# These are fallback coordinates.
#
# Normally the AI will first use:
#
#     destination.latitude
#     destination.longitude
#
# from MySQL.
#
# If the database contains NULL coordinates because an
# older seed was used, these values prevent the AI from
# breaking.
#
# =========================================================

DESTINATION_COORDINATES = {

    # =====================================================
    # NORTH BENGAL
    # =====================================================

    "darjeeling": {
        "latitude": 27.0410,
        "longitude": 88.2663
    },

    "kalimpong": {
        "latitude": 27.0667,
        "longitude": 88.4667
    },

    "jaldapara": {
        "latitude": 26.6944,
        "longitude": 89.2722
    },

    "buxa": {
        "latitude": 26.7040,
        "longitude": 89.5527
    },

    "mirik": {
        "latitude": 26.8894,
        "longitude": 88.1803
    },

    "chatakpur": {
        "latitude": 26.9300,
        "longitude": 88.3650
    },

    "sandakphu": {
        "latitude": 27.1050,
        "longitude": 88.0040
    },

    "tinchuley": {
        "latitude": 27.1000,
        "longitude": 88.3900
    },

    "lepchajagat": {
        "latitude": 27.0200,
        "longitude": 88.2400
    },

    "pedong": {
        "latitude": 27.1800,
        "longitude": 88.6100
    },

    "samsing": {
        "latitude": 26.8700,
        "longitude": 88.7800
    },

    "neora valley": {
        "latitude": 27.0200,
        "longitude": 88.7000
    },

    # =====================================================
    # MEGHALAYA
    # =====================================================

    "shillong": {
        "latitude": 25.5788,
        "longitude": 91.8933
    },

    "sohra": {
        "latitude": 25.2700,
        "longitude": 91.7300
    },

    "cherrapunji": {
        "latitude": 25.2700,
        "longitude": 91.7300
    },

    "dawki": {
        "latitude": 25.1930,
        "longitude": 92.0250
    },

    "shnongpdeng": {
        "latitude": 25.1800,
        "longitude": 92.0400
    },

    "mawlynnong": {
        "latitude": 25.2100,
        "longitude": 91.9200
    },

    # =====================================================
    # ASSAM
    # =====================================================

    "kaziranga": {
        "latitude": 26.5775,
        "longitude": 93.1711
    },

    "majuli": {
        "latitude": 27.0016,
        "longitude": 94.2243
    },

    "manas": {
        "latitude": 26.6590,
        "longitude": 91.0010
    },

    "guwahati": {
        "latitude": 26.1445,
        "longitude": 91.7362
    }
}


# =========================================================
# TEXT NORMALIZATION
# =========================================================

def normalize_location(location):

    if location is None:
        return ""

    return (
        str(location)
        .strip()
        .lower()
        .replace("  ", " ")
    )


# =========================================================
# TEXT MATCHING
# =========================================================

def text_match(
    user_text,
    destination_text
):

    if not user_text:
        return 0

    if not destination_text:
        return 0

    user_words = set(
        word.strip().lower()
        for word in str(user_text).split(",")
        if word.strip()
    )

    destination_words = set(
        word.strip().lower()
        for word in str(destination_text).split(",")
        if word.strip()
    )

    if not user_words:
        return 0

    matches = user_words.intersection(
        destination_words
    )

    return (
        len(matches) /
        len(user_words)
    ) * 100


# =========================================================
# STARTING LOCATION LOOKUP
# =========================================================

def get_starting_coordinates(
    starting_location
):

    if not starting_location:
        return None

    # -----------------------------------------------------
    # Future-compatible:
    #
    # If main.py eventually sends:
    #
    # {
    #     "latitude": 22.5,
    #     "longitude": 88.3
    # }
    #
    # we can directly use it.
    # -----------------------------------------------------

    if isinstance(starting_location, dict):

        latitude = starting_location.get(
            "latitude"
        )

        longitude = starting_location.get(
            "longitude"
        )

        if (
            latitude is not None
            and longitude is not None
        ):
            return {
                "latitude": float(latitude),
                "longitude": float(longitude)
            }

    # -----------------------------------------------------
    # Normal string lookup
    # -----------------------------------------------------

    location = normalize_location(
        starting_location
    )

    return STARTING_LOCATIONS.get(
        location
    )


# =========================================================
# DESTINATION COORDINATE LOOKUP
# =========================================================

def get_destination_coordinates(
    destination
):

    # -----------------------------------------------------
    # 1. Prefer database coordinates
    # -----------------------------------------------------

    if (
        destination.latitude is not None
        and
        destination.longitude is not None
    ):

        return {
            "latitude": float(
                destination.latitude
            ),
            "longitude": float(
                destination.longitude
            )
        }

    # -----------------------------------------------------
    # 2. Use fallback coordinates
    # -----------------------------------------------------

    destination_name = normalize_location(
        destination.name
    )

    coordinates = DESTINATION_COORDINATES.get(
        destination_name
    )

    if coordinates:
        return coordinates

    # -----------------------------------------------------
    # 3. Unknown destination
    # -----------------------------------------------------

    return None


# =========================================================
# DISTANCE CALCULATION
# =========================================================

def calculate_distance(
    lat1,
    lon1,
    lat2,
    lon2
):

    earth_radius_km = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        +
        cos(lat1)
        *
        cos(lat2)
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return earth_radius_km * c


# =========================================================
# LOCATION SCORE
# =========================================================
#
# Location score is now based primarily on actual distance.
#
# This is better than:
#
# Kolkata = 60
# Siliguri = 65
#
# because:
#
# New Town → Darjeeling
#
# and
#
# Howrah → Darjeeling
#
# will naturally have different distances.
#
# =========================================================

def calculate_location_score(
    distance_km
):

    if distance_km is None:
        return 50

    # Very close
    if distance_km <= 50:
        return 100

    # Nearby
    if distance_km <= 150:
        return 95

    if distance_km <= 250:
        return 90

    if distance_km <= 400:
        return 80

    if distance_km <= 600:
        return 70

    if distance_km <= 900:
        return 60

    if distance_km <= 1200:
        return 50

    return 40


# =========================================================
# TRAVEL COST CALCULATION
# =========================================================
#
# Uses:
#
# starting coordinates
#          +
# destination coordinates
#          +
# selected transport
#
# to calculate an estimated one-way transport cost.
#
# =========================================================

def calculate_travel_cost(
    starting_location,
    destination,
    transport
):

    # -----------------------------------------------------
    # STARTING LOCATION
    # -----------------------------------------------------

    start = get_starting_coordinates(
        starting_location
    )

    if not start:

        raise ValueError(
            "Starting location is not recognized. "
            "Please select a valid location such as "
            "Kolkata, New Town, Salt Lake, Howrah, "
            "Siliguri, Asansol, Durgapur, Malda or "
            "another supported location."
        )

    # -----------------------------------------------------
    # DESTINATION LOCATION
    # -----------------------------------------------------

    destination_coordinates = (
        get_destination_coordinates(
            destination
        )
    )

    if not destination_coordinates:

        raise ValueError(
            "Destination coordinates are missing for "
            f"{destination.name}. "
            "Please update the destination coordinates "
            "in ai_seed.py."
        )

    # -----------------------------------------------------
    # DISTANCE
    # -----------------------------------------------------

    distance = calculate_distance(
        start["latitude"],
        start["longitude"],
        destination_coordinates[
            "latitude"
        ],
        destination_coordinates[
            "longitude"
        ]
    )

    # -----------------------------------------------------
    # TRANSPORT RATES
    # -----------------------------------------------------
    #
    # Prototype estimated rates.
    #
    # These are not live ticket prices.
    #
    # -----------------------------------------------------

    rates = {

        "bus": {
            "base": 80,
            "per_km": 2.2
        },

        "train": {
            "base": 100,
            "per_km": 1.8
        },

        "shared car": {
            "base": 150,
            "per_km": 3.5
        },

        "private car": {
            "base": 500,
            "per_km": 12.0
        }
    }

    transport_key = (
        normalize_location(
            transport
        )
        if transport
        else "bus"
    )

    # -----------------------------------------------------
    # Transport aliases
    # -----------------------------------------------------

    transport_aliases = {

        "shared taxi":
            "shared car",

        "shared cab":
            "shared car",

        "cab":
            "private car",

        "car":
            "private car",

        "private cab":
            "private car"
    }

    transport_key = transport_aliases.get(
        transport_key,
        transport_key
    )

    # -----------------------------------------------------
    # Unknown transport
    # -----------------------------------------------------

    if transport_key not in rates:

        raise ValueError(
            "Unsupported transport type. "
            "Please choose Bus, Train, Shared Car "
            "or Private Car."
        )

    rate = rates[
        transport_key
    ]

    # -----------------------------------------------------
    # ONE-WAY ESTIMATED COST
    # -----------------------------------------------------

    cost = (
        rate["base"]
        +
        distance * rate["per_km"]
    )

    # -----------------------------------------------------
    # Round to nearest ₹10
    # -----------------------------------------------------

    cost = (
        round(cost / 10)
        * 10
    )

    return {

        "distance_km":
            round(distance, 1),

        "cost_per_person":
            round(cost)
    }


# =========================================================
# BUDGET CALCULATION
# =========================================================

def calculate_budget(
    destination,
    transport_cost,
    people,
    duration
):

    # -----------------------------------------------------
    # Protect against invalid values
    # -----------------------------------------------------

    people = max(
        int(people or 1),
        1
    )

    duration = max(
        int(duration or 1),
        1
    )

    # -----------------------------------------------------
    # Hotel
    # -----------------------------------------------------

    hotel_cost = (
        (destination.hotel_cost_per_night or 0)
        *
        duration
    )

    # -----------------------------------------------------
    # Food
    # -----------------------------------------------------

    food_cost = (
        (destination.food_cost_per_day or 0)
        *
        duration
        *
        people
    )

    # -----------------------------------------------------
    # Activities
    # -----------------------------------------------------

    activity_cost = (
        (destination.base_cost_per_person or 0)
        *
        people
    )

    # -----------------------------------------------------
    # Transport
    # -----------------------------------------------------

    transport_total = (
        (transport_cost or 0)
        *
        people
    )

    # -----------------------------------------------------
    # Total
    # -----------------------------------------------------

    total = (
        hotel_cost
        +
        food_cost
        +
        activity_cost
        +
        transport_total
    )

    return {

        "total":
            round(total),

        "hotel":
            round(hotel_cost),

        "food":
            round(food_cost),

        "activities":
            round(activity_cost),

        "transport":
            round(transport_total)
    }


# =========================================================
# BUDGET SCORE
# =========================================================

def calculate_budget_score(
    total_budget,
    user_budget
):

    if not user_budget:
        return 50

    user_budget = float(
        user_budget
    )

    if user_budget <= 0:
        return 50

    # -----------------------------------------------------
    # Within budget
    # -----------------------------------------------------

    if total_budget <= user_budget:

        difference = (
            user_budget -
            total_budget
        )

        percentage_saved = (
            difference /
            user_budget
        ) * 100

        score = (
            100 -
            percentage_saved * 0.35
        )

        return round(
            max(
                65,
                min(
                    100,
                    score
                )
            )
        )

    # -----------------------------------------------------
    # Over budget
    # -----------------------------------------------------

    over_budget = (
        total_budget -
        user_budget
    )

    over_percentage = (
        over_budget /
        user_budget
    ) * 100

    score = (
        100 -
        over_percentage * 1.5
    )

    return round(
        max(
            0,
            min(
                100,
                score
            )
        )
    )


# =========================================================
# FOOTFALL SCORE
# =========================================================

def calculate_footfall_score(
    crowd_score,
    preference
):

    if not preference:
        return 50

    preference = (
        str(preference)
        .strip()
        .lower()
    )

    crowd_score = (
        crowd_score
        if crowd_score is not None
        else 50
    )

    if preference == "low":

        return max(
            0,
            100 - crowd_score
        )

    if preference == "medium":

        distance = abs(
            50 - crowd_score
        )

        return max(
            0,
            100 - distance
        )

    if preference == "high":

        return crowd_score

    return 50


# =========================================================
# WEATHER SCORE
# =========================================================

def calculate_weather_score(
    weather_preference,
    destination
):

    if not weather_preference:
        return 50

    preference = (
        str(weather_preference)
        .strip()
        .lower()
    )

    category = (
        destination.category.lower()
        if destination.category
        else ""
    )

    tags = (
        destination.tags.lower()
        if destination.tags
        else ""
    )

    if preference == "cool":

        if (
            "mountain" in category
            or
            "mountain" in tags
            or
            "forest" in tags
        ):
            return 95

        return 60

    if preference == "warm":

        if (
            "lake" in category
            or
            "wildlife" in category
        ):
            return 75

        return 60

    if preference == "pleasant":
        return 85

    if preference == "any":
        return 70

    return 50


# =========================================================
# TRANSPORT SCORE
# =========================================================

def calculate_transport_score(
    transport
):

    if not transport:
        return 50

    supported = [
        "bus",
        "train",
        "shared car",
        "private car"
    ]

    transport_key = normalize_location(
        transport
    )

    aliases = {

        "shared taxi":
            "shared car",

        "shared cab":
            "shared car",

        "cab":
            "private car",

        "car":
            "private car"
    }

    transport_key = aliases.get(
        transport_key,
        transport_key
    )

    if transport_key in supported:
        return 100

    return 50


# =========================================================
# AI MATCH
# =========================================================

def calculate_match(
    destination,
    experience,
    budget_score,
    footfall_score,
    transport_score,
    weather_score,
    location_score
):

    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

    experience_score = text_match(
        experience,
        destination.best_for
    )

    tag_score = text_match(
        experience,
        destination.tags
    )

    experience_final = (
        experience_score * 0.70
        +
        tag_score * 0.30
    )

    # -----------------------------------------------------
    # FINAL WEIGHTING
    # -----------------------------------------------------
    #
    # Experience 30%
    # Budget     25%
    # Footfall   15%
    # Transport  10%
    # Weather     8%
    # Location    7%
    # Rating      5%
    #
    # -----------------------------------------------------

    final_score = (

        experience_final
        * 0.30

        +

        budget_score
        * 0.25

        +

        footfall_score
        * 0.15

        +

        transport_score
        * 0.10

        +

        weather_score
        * 0.08

        +

        location_score
        * 0.07

        +

        (
            (
                destination.rating
                or 0
            )
            /
            5
            *
            100
        )
        * 0.05
    )

    return round(
        max(
            0,
            min(
                100,
                final_score
            )
        )
    )


# =========================================================
# MAIN RECOMMENDATION FUNCTION
# =========================================================

def generate_recommendations(
    db: Session,
    starting_location,
    experience,
    budget,
    people,
    duration,
    transport,
    visit_date,
    weather_preference,
    footfall_preference
):

    # =====================================================
    # VALIDATE STARTING LOCATION BEFORE DOING ANYTHING
    # =====================================================

    start_coordinates = (
        get_starting_coordinates(
            starting_location
        )
    )

    if not start_coordinates:

        raise ValueError(
            f"Starting location "
            f"'{starting_location}' "
            "is not recognized. "
            "Please enter a valid supported "
            "location."
        )

    # =====================================================
    # GET ALL DESTINATIONS
    # =====================================================

    destinations = (
        db.query(Destination)
        .all()
    )

    if not destinations:

        raise ValueError(
            "No destinations are available "
            "in the database."
        )

    recommendations = []

    # =====================================================
    # ANALYZE EACH DESTINATION
    # =====================================================

    for destination in destinations:

        # -------------------------------------------------
        # DESTINATION COORDINATES
        # -------------------------------------------------

        destination_coordinates = (
            get_destination_coordinates(
                destination
            )
        )

        if not destination_coordinates:

            # Do not crash the complete AI planner.
            #
            # Simply skip destinations that have no
            # coordinates and are not in our fallback map.

            print(
                "Skipping destination because "
                "coordinates are missing:",
                destination.name
            )

            continue

        # -------------------------------------------------
        # TRAVEL
        # -------------------------------------------------

        travel_information = (
            calculate_travel_cost(
                starting_location,
                destination,
                transport
            )
        )

        transport_cost = (
            travel_information[
                "cost_per_person"
            ]
        )

        distance_km = (
            travel_information[
                "distance_km"
            ]
        )

        # -------------------------------------------------
        # BUDGET
        # -------------------------------------------------

        budget_breakdown = (
            calculate_budget(
                destination,
                transport_cost,
                people,
                duration
            )
        )

        total_budget = (
            budget_breakdown[
                "total"
            ]
        )

        budget_score = (
            calculate_budget_score(
                total_budget,
                budget
            )
        )

        # -------------------------------------------------
        # FOOTFALL
        # -------------------------------------------------

        footfall = None

        if visit_date:

            footfall = (
                db.query(
                    FootfallData
                )
                .filter(
                    FootfallData.destination
                    ==
                    destination.name
                )
                .filter(
                    FootfallData.visit_date
                    ==
                    visit_date
                )
                .first()
            )

        if footfall:

            crowd_score = (
                footfall.crowd_score
            )

            crowd_level = (
                footfall.crowd_level
            )

        else:

            crowd_score = 50
            crowd_level = "Unknown"

        footfall_score = (
            calculate_footfall_score(
                crowd_score,
                footfall_preference
            )
        )

        # -------------------------------------------------
        # WEATHER
        # -------------------------------------------------

        weather_score = (
            calculate_weather_score(
                weather_preference,
                destination
            )
        )

        # -------------------------------------------------
        # LOCATION
        # -------------------------------------------------
        #
        # Unlike the old implementation, this uses the
        # actual calculated distance.
        #
        # So:
        #
        # New Town → Darjeeling
        #
        # and
        #
        # Howrah → Darjeeling
        #
        # don't receive the same location score.
        #
        # -------------------------------------------------

        location_score = (
            calculate_location_score(
                distance_km
            )
        )

        # -------------------------------------------------
        # TRANSPORT
        # -------------------------------------------------

        transport_score = (
            calculate_transport_score(
                transport
            )
        )

        # -------------------------------------------------
        # FINAL AI SCORE
        # -------------------------------------------------

        match_score = calculate_match(
            destination,
            experience,
            budget_score,
            footfall_score,
            transport_score,
            weather_score,
            location_score
        )

        # -------------------------------------------------
        # STORE RESULT
        # -------------------------------------------------

        recommendations.append({

            "destination":
                destination.name,

            "district":
                destination.district,

            "category":
                destination.category,

            "description":
                destination.description,

            "rating":
                destination.rating,

            "image":
                destination.image,

            "ai_match":
                match_score,

            "estimated_budget":
                total_budget,

            "transport":
                transport,

            "distance_km":
                distance_km,

            "transport_cost":
                budget_breakdown[
                    "transport"
                ],

            "hotel_cost":
                budget_breakdown[
                    "hotel"
                ],

            "food_cost":
                budget_breakdown[
                    "food"
                ],

            "activity_cost":
                budget_breakdown[
                    "activities"
                ],

            "crowd_level":
                crowd_level,

            "crowd_score":
                crowd_score,

            "duration":
                duration,

            "experience_score":
                round(
                    text_match(
                        experience,
                        destination.best_for
                    )
                ),

            "budget_score":
                budget_score,

            "footfall_score":
                footfall_score,

            "weather_score":
                weather_score,

            "location_score":
                location_score
        })

    # =====================================================
    # CHECK RESULTS
    # =====================================================

    if not recommendations:

        raise ValueError(
            "No destinations with valid coordinates "
            "are available."
        )

    # =====================================================
    # SORT
    # =====================================================

    recommendations.sort(
        key=lambda item:
            item["ai_match"],
        reverse=True
    )

    # =====================================================
    # RETURN TOP 5
    # =====================================================

    return recommendations[:5]