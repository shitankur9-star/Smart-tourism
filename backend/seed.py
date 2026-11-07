from database import SessionLocal, engine, Base
from models import Trip, Hotel


# =========================================================
# CREATE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# OPEN DATABASE SESSION
# =========================================================

db = SessionLocal()


try:

    # =====================================================
    # ALL TRIPS
    # =====================================================

    trips = [

        # -------------------------------------------------
        # ORIGINAL NORTH BENGAL TRIPS
        # -------------------------------------------------

        Trip(
            title="Hidden Gems Explorer",
            category="North Bengal",
            route="Chatakpur → Takdah → Lamahatta",
            image="/assets/NB-1.jpeg",
            rating=4.5,
            reviews=245,
            price=5000,
            duration="5 Days / 4 Nights",
            difficulty="Easy",
            description=(
                "Explore the hidden beauty of North Bengal through "
                "peaceful mountains, tea gardens, forests and "
                "lesser-known villages."
            ),
            tags="Nature,Photography,Guide",
            recommended_for="Nature Lovers,Couples,Photographers",
            ai_match=96
        ),

        Trip(
            title="Darjeeling",
            category="Tea Gardens",
            route="Kurseong → Mirik → Darjeeling",
            image="/assets/darjeeling.jpeg",
            rating=4.7,
            reviews=182,
            price=4500,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Experience beautiful tea gardens, mountain views "
                "and peaceful trails across North Bengal."
            ),
            tags="Tea Gardens,Nature,Photography",
            recommended_for="Nature Lovers,Photographers,Couples",
            ai_match=94
        ),

        Trip(
            title="Wildlife Escape",
            category="Wildlife",
            route="Jaldapara → Buxa → Jayanti",
            image="/assets/jaldapara.jpeg",
            rating=4.8,
            reviews=156,
            price=6500,
            duration="5 Days / 4 Nights",
            difficulty="Moderate",
            description=(
                "Discover the wildlife and forests of North Bengal "
                "with guided nature experiences."
            ),
            tags="Wildlife,Nature,Adventure",
            recommended_for="Wildlife Lovers,Families",
            ai_match=91
        ),

        # -------------------------------------------------
        # NORTH BENGAL / DOOARS
        # -------------------------------------------------

        Trip(
            title="Dooars Forest Escape",
            category="Wildlife",
            route="Lataguri → Jaldapara → Buxa",
            image="/assets/dooars.png",
            rating=4.7,
            reviews=140,
            price=7200,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Explore the forests, wildlife and rivers of Dooars."
            ),
            tags="Wildlife,Nature,Adventure",
            recommended_for="Nature Lovers,Families,Wildlife Lovers",
            ai_match=92
        ),

        Trip(
            title="Kalimpong Mountain Escape",
            category="Mountains",
            route="Siliguri → Kalimpong → Lava",
            image="/assets/kalimpong.jpeg",
            rating=4.6,
            reviews=118,
            price=6800,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Enjoy peaceful mountain landscapes, monasteries, "
                "pine forests and beautiful Himalayan views."
            ),
            tags="Mountains,Photography,Nature",
            recommended_for="Couples,Photographers,Nature Lovers",
            ai_match=90
        ),

        Trip(
            title="Sandakphu Himalayan Quest",
            category="Trekking",
            route="Maneybhanjan → Tumling → Sandakphu → Srikhola",
            image="/assets/sandakphu.jpeg",
            rating=4.9,
            reviews=324,
            price=9800,
            duration="6 Days / 5 Nights",
            difficulty="Hard",
            description=(
                "Take on one of North Bengal's most spectacular "
                "mountain journeys with dramatic Himalayan landscapes "
                "and panoramic views of Kanchenjunga and the surrounding peaks."
            ),
            tags="Trekking,Mountains,Adventure,Photography",
            recommended_for="Adventure Lovers,Trekkers,Photographers",
            ai_match=97
        ),

        Trip(
            title="Tinchuley Himalayan Hideaway",
            category="Offbeat Mountains",
            route="Siliguri → Tinchuley → Lamahatta → Takdah",
            image="/assets/tinchuley.jpeg",
            rating=4.7,
            reviews=168,
            price=6200,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Escape into the quiet hills of Tinchuley with forest walks, "
                "mountain viewpoints, village life and peaceful Himalayan landscapes."
            ),
            tags="Mountains,Nature,Offbeat,Photography",
            recommended_for="Couples,Nature Lovers,Photographers",
            ai_match=95
        ),

        Trip(
            title="Lepchajagat Forest Retreat",
            category="Forest Retreat",
            route="Siliguri → Lepchajagat → Ghoom → Jorethang",
            image="/assets/lepchajagat.jpeg",
            rating=4.6,
            reviews=143,
            price=5600,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Stay deep within pine forests and discover a quieter side "
                "of Darjeeling surrounded by misty mountains and bird-filled trails."
            ),
            tags="Forest,Nature,Photography,Offbeat",
            recommended_for="Couples,Nature Lovers,Peace Seekers",
            ai_match=93
        ),

        Trip(
            title="Pedong Heritage Trail",
            category="Culture & Mountains",
            route="Siliguri → Pedong → Sillery Gaon → Damsang",
            image="/assets/pedong.jpeg",
            rating=4.5,
            reviews=126,
            price=5900,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Discover peaceful mountain villages, historic trails, "
                "pine forests and panoramic Himalayan viewpoints around Pedong."
            ),
            tags="Culture,Mountains,Nature,Heritage",
            recommended_for="Culture Lovers,Couples,Photographers",
            ai_match=91
        ),

        Trip(
            title="Samsing & Suntalekhola Wilderness",
            category="Wilderness",
            route="Siliguri → Samsing → Suntalekhola → Mouchuki",
            image="/assets/samsing_view.jpeg",
            rating=4.8,
            reviews=187,
            price=6400,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Follow forest trails through Samsing and Suntalekhola, "
                "where tea gardens, mountain streams, hanging bridges and "
                "dense forests create an unforgettable wilderness escape."
            ),
            tags="Wilderness,Trekking,Tea Gardens,Birdwatching",
            recommended_for="Nature Lovers,Adventure Lovers,Birdwatchers",
            ai_match=96
        ),

        Trip(
            title="Neora Valley Wild Trails",
            category="National Park",
            route="Siliguri → Lava → Kolakham → Neora Valley",
            image="/assets/neora_valley_national-park.jpeg",
            rating=4.9,
            reviews=204,
            price=7600,
            duration="5 Days / 4 Nights",
            difficulty="Moderate",
            description=(
                "Explore the mysterious forests surrounding Neora Valley "
                "with misty mountain trails, rare Himalayan wildlife and "
                "untouched natural landscapes."
            ),
            tags="Wildlife,Trekking,Forest,Adventure",
            recommended_for="Wildlife Lovers,Trekkers,Nature Lovers",
            ai_match=98
        ),

        Trip(
            title="Rishyap Stargazing Escape",
            category="Stargazing",
            route="Siliguri → Lava → Rishyap → Lolegaon",
            image="/assets/rishyap.png",
            rating=4.7,
            reviews=139,
            price=5700,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Escape to the quiet Himalayan village of Rishyap for "
                "mountain sunsets, peaceful forests and spectacular night skies."
            ),
            tags="Stargazing,Mountains,Nature,Photography",
            recommended_for="Couples,Photographers,Peace Seekers",
            ai_match=94
        ),

        Trip(
            title="Sillery Gaon Cloud Village",
            category="Offbeat Mountains",
            route="Siliguri → Pedong → Sillery Gaon → Damsang",
            image="/assets/sillery-gaon.jpg",
            rating=4.6,
            reviews=115,
            price=5400,
            duration="3 Days / 2 Nights",
            difficulty="Easy",
            description=(
                "Spend a few peaceful days above the clouds surrounded by "
                "pine forests, quiet village trails and sweeping Himalayan views."
            ),
            tags="Mountains,Offbeat,Photography,Nature",
            recommended_for="Couples,Nature Lovers,Photographers",
            ai_match=92
        ),

        Trip(
            title="Rimbick Valley Explorer",
            category="Mountain Villages",
            route="Darjeeling → Maneybhanjan → Rimbick → Srikhola",
            image="/assets/rimbick.png",
            rating=4.7,
            reviews=132,
            price=6100,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Discover the peaceful mountain villages of Rimbick and "
                "Srikhola through forest paths, riverside landscapes and "
                "traditional Himalayan communities."
            ),
            tags="Mountains,Trekking,Villages,Nature",
            recommended_for="Trekkers,Photographers,Nature Lovers",
            ai_match=93
        ),

        Trip(
            title="Dooars River & Tea Trail",
            category="Nature & Tea",
            route="Samsing → Suntalekhola → Rocky Island → Murti",
            image="/assets/dooars.png",
            rating=4.6,
            reviews=121,
            price=5800,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Experience the greener side of Dooars through tea gardens, "
                "riverside landscapes, forest trails and peaceful mountain villages."
            ),
            tags="Tea Gardens,River,Nature,Photography",
            recommended_for="Families,Couples,Nature Lovers",
            ai_match=90
        ),

        # -------------------------------------------------
        # MEGHALAYA
        # -------------------------------------------------

        Trip(
            title="Meghalaya Cloudscape",
            category="Mountains",
            route="Guwahati → Shillong → Sohra → Laitlum",
            image="/assets/meghalaya_cloudscape.png",
            rating=4.8,
            reviews=286,
            price=7800,
            duration="5 Days / 4 Nights",
            difficulty="Easy",
            description=(
                "Travel through the misty hills of Meghalaya, exploring "
                "Shillong, dramatic cliffs, waterfalls and breathtaking "
                "valley views around Sohra and Laitlum."
            ),
            tags="Mountains,Waterfalls,Nature,Photography",
            recommended_for="Couples,Nature Lovers,Photographers",
            ai_match=95
        ),

        Trip(
            title="Dawki & Living Roots",
            category="Adventure",
            route="Shillong → Mawlynnong → Dawki → Shnongpdeng",
            image="/assets/dawki_river.jpeg",
            rating=4.9,
            reviews=312,
            price=7200,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Discover Meghalaya's living root bridges, crystal-clear "
                "rivers and peaceful border villages while experiencing "
                "the natural beauty of Dawki and Shnongpdeng."
            ),
            tags="Adventure,Nature,River,Photography",
            recommended_for="Adventure Lovers,Couples,Photographers,Friends",
            ai_match=97
        ),

        Trip(
            title="Sohra Waterfall Trail",
            category="Waterfalls",
            route="Shillong → Sohra → Nohkalikai → Mawsmai → Nongriat",
            image="/assets/sohra.jpeg",
            rating=4.8,
            reviews=224,
            price=6900,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Chase spectacular waterfalls, explore limestone caves and "
                "trek through lush forests to discover Meghalaya's legendary "
                "living root bridges."
            ),
            tags="Waterfalls,Trekking,Nature,Adventure",
            recommended_for="Trekkers,Adventure Lovers,Photographers",
            ai_match=94
        ),

        # -------------------------------------------------
        # ASSAM
        # -------------------------------------------------

        Trip(
            title="Kaziranga Wild Trails",
            category="Wildlife",
            route="Guwahati → Kaziranga → Kohora → Brahmaputra",
            image="/assets/kaziranga_national-park.jpeg",
            rating=4.9,
            reviews=341,
            price=8200,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Experience the wilderness of Kaziranga through jungle "
                "safaris, grasslands, wetlands and unforgettable encounters "
                "with Assam's iconic wildlife."
            ),
            tags="Wildlife,Safari,Nature,Photography",
            recommended_for="Wildlife Lovers,Families,Photographers",
            ai_match=98
        ),

        Trip(
            title="Majuli Cultural Journey",
            category="Culture",
            route="Jorhat → Majuli → Kamalabari → Mishing Villages",
            image="/assets/majuli.jpeg",
            rating=4.7,
            reviews=198,
            price=6100,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Discover the cultural heart of Assam through ancient Satras, "
                "river-island landscapes, traditional villages, pottery and "
                "the unique artistic traditions of Majuli."
            ),
            tags="Culture,Nature,Heritage,Photography",
            recommended_for="Culture Lovers,Photographers,Slow Travelers",
            ai_match=93
        ),

        Trip(
            title="Manas Wilderness Expedition",
            category="Wildlife",
            route="Guwahati → Manas → Bansbari → Bhutan Foothills",
            image="/assets/manas.png",
            rating=4.8,
            reviews=167,
            price=7600,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Explore the wild landscapes of Manas National Park, "
                "following forest trails, grasslands and river landscapes "
                "along the foothills of the Bhutan Himalayas."
            ),
            tags="Wildlife,Adventure,Nature,Safari",
            recommended_for="Wildlife Lovers,Adventure Lovers,Photographers",
            ai_match=94
        )
    ]


    # =====================================================
    # INSERT TRIPS WITHOUT DUPLICATES
    # =====================================================

    for trip in trips:

        existing = (
            db.query(Trip)
            .filter(Trip.title == trip.title)
            .first()
        )

        if not existing:
            db.add(trip)

    db.commit()

    print("Trips inserted successfully.")


    # =====================================================
    # GET ALL TRIPS FROM DATABASE
    # =====================================================

    trip_map = {}

    for trip in db.query(Trip).all():
        trip_map[trip.title] = trip


    # =====================================================
    # HOTEL DATA
    # =====================================================

    hotels = [

        # =================================================
        # HIDDEN GEMS EXPLORER
        # =================================================

        Hotel(
            trip_id=trip_map["Hidden Gems Explorer"].id,
            name="Chatakpur Eco Retreat",
            location="Chatakpur",
            image="/images/hotel-chatakpur.jpg",
            rating=4.6,
            price_per_night=2200,
            room_type="Mountain View Cottage",
            facilities="WiFi,Breakfast,Parking,Mountain View,Bonfire",
            available_rooms=6,
            description=(
                "A peaceful mountain retreat surrounded by pine forests "
                "with beautiful Himalayan views."
            )
        ),

        Hotel(
            trip_id=trip_map["Hidden Gems Explorer"].id,
            name="Takdah Heritage Stay",
            location="Takdah",
            image="/images/hotel-takdah.jpg",
            rating=4.5,
            price_per_night=2500,
            room_type="Deluxe Heritage Room",
            facilities="WiFi,Breakfast,Parking,Garden,Bonfire",
            available_rooms=4,
            description=(
                "A charming heritage-style stay surrounded by forests "
                "and peaceful mountain landscapes."
            )
        ),

        Hotel(
            trip_id=trip_map["Hidden Gems Explorer"].id,
            name="Lamahatta Forest Lodge",
            location="Lamahatta",
            image="/images/hotel-lamahatta.jpg",
            rating=4.4,
            price_per_night=2300,
            room_type="Deluxe Cottage",
            facilities="WiFi,Breakfast,Parking,Garden,Room Service",
            available_rooms=5,
            description=(
                "Comfortable cottages located close to the Lamahatta "
                "forest and nature trails."
            )
        ),


        # =================================================
        # TEA GARDEN TRAILS
        # =================================================

        Hotel(
            trip_id=trip_map["Darjeeling"].id,
            name="Kurseong Tea Valley Resort",
            location="Kurseong",
            image="/images/hotel-kurseong.jpg",
            rating=4.6,
            price_per_night=2800,
            room_type="Tea Garden View Room",
            facilities="WiFi,Breakfast,Parking,Restaurant,Garden",
            available_rooms=7,
            description=(
                "A peaceful stay surrounded by lush tea gardens "
                "and misty Himalayan landscapes."
            )
        ),

        Hotel(
            trip_id=trip_map["Darjeeling"].id,
            name="Mirik Lake View Resort",
            location="Mirik",
            image="/images/hotel-mirik.jpg",
            rating=4.5,
            price_per_night=2600,
            room_type="Lake View Deluxe Room",
            facilities="WiFi,Breakfast,Parking,Restaurant,Lake View",
            available_rooms=8,
            description=(
                "Comfortable accommodation near Mirik Lake with "
                "beautiful views and easy access to local attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Darjeeling"].id,
            name="Darjeeling Mountain Retreat",
            location="Darjeeling",
            image="/images/hotel-darjeeling.jpg",
            rating=4.7,
            price_per_night=3200,
            room_type="Premium Mountain View Room",
            facilities="WiFi,Breakfast,Parking,Restaurant,Mountain View",
            available_rooms=5,
            description=(
                "A comfortable mountain stay offering panoramic views "
                "and convenient access to Darjeeling attractions."
            )
        ),


        # =================================================
        # WILDLIFE ESCAPE
        # =================================================

        Hotel(
            trip_id=trip_map["Wildlife Escape"].id,
            name="Jaldapara Jungle Resort",
            location="Madarihat",
            image="/images/hotel-jaldapara.jpg",
            rating=4.7,
            price_per_night=3000,
            room_type="Forest View Cottage",
            facilities="WiFi,Breakfast,Parking,Restaurant,Bonfire",
            available_rooms=6,
            description=(
                "A comfortable jungle retreat near Jaldapara National Park "
                "perfect for wildlife and nature enthusiasts."
            )
        ),

        Hotel(
            trip_id=trip_map["Wildlife Escape"].id,
            name="Buxa Forest Lodge",
            location="Buxa",
            image="/images/hotel-buxa.jpg",
            rating=4.4,
            price_per_night=2200,
            room_type="Forest Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Guide Service",
            available_rooms=5,
            description=(
                "A simple forest stay surrounded by the natural beauty "
                "of Buxa Tiger Reserve."
            )
        ),

        Hotel(
            trip_id=trip_map["Wildlife Escape"].id,
            name="Jayanti Riverside Retreat",
            location="Jayanti",
            image="/images/hotel-jayanti.jpg",
            rating=4.6,
            price_per_night=2400,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,Garden,River View,Bonfire",
            available_rooms=4,
            description=(
                "A peaceful riverside accommodation surrounded by "
                "forests and the hills of Jayanti."
            )
        ),


        # =================================================
        # DOOARS FOREST ESCAPE
        # =================================================

        Hotel(
            trip_id=trip_map["Dooars Forest Escape"].id,
            name="Dooars Retreat",
            location="Lataguri",
            image="/images/hotel1.jpeg",
            rating=4.5,
            price_per_night=2500,
            room_type="Deluxe Room",
            facilities="WiFi,Breakfast,Parking,AC",
            available_rooms=5,
            description=(
                "Comfortable stay surrounded by the forests of Dooars "
                "with easy access to nearby wildlife destinations."
            )
        ),

        Hotel(
            trip_id=trip_map["Dooars Forest Escape"].id,
            name="Forest View Resort",
            location="Lataguri",
            image="/images/hotel2.jpeg",
            rating=4.7,
            price_per_night=3200,
            room_type="Premium Room",
            facilities="WiFi,Pool,Breakfast,Parking",
            available_rooms=3,
            description=(
                "A peaceful resort with beautiful forest views."
            )
        ),

        Hotel(
            trip_id=trip_map["Dooars Forest Escape"].id,
            name="Dooars Riverside Lodge",
            location="Murti",
            image="/images/hotel-murti.jpg",
            rating=4.6,
            price_per_night=2700,
            room_type="River View Cottage",
            facilities="WiFi,Breakfast,Parking,Restaurant,River View",
            available_rooms=7,
            description=(
                "Relax beside the Murti River while enjoying the "
                "green landscapes and forests of Dooars."
            )
        ),


        # =================================================
        # KALIMPONG MOUNTAIN ESCAPE
        # =================================================

        Hotel(
            trip_id=trip_map["Kalimpong Mountain Escape"].id,
            name="Kalimpong Hills Retreat",
            location="Kalimpong",
            image="/images/hotel-kalimpong.jpg",
            rating=4.6,
            price_per_night=2800,
            room_type="Mountain View Deluxe",
            facilities="WiFi,Breakfast,Parking,Restaurant,Mountain View",
            available_rooms=6,
            description=(
                "A peaceful hill retreat offering beautiful mountain "
                "views and easy access to Kalimpong attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Kalimpong Mountain Escape"].id,
            name="Lava Forest Lodge",
            location="Lava",
            image="/images/hotel-lava.jpg",
            rating=4.5,
            price_per_night=2400,
            room_type="Forest Cottage",
            facilities="Breakfast,Parking,Bonfire,Garden,Mountain View",
            available_rooms=5,
            description=(
                "A cozy forest lodge surrounded by pine trees and "
                "misty mountain landscapes."
            )
        ),

        Hotel(
            trip_id=trip_map["Kalimpong Mountain Escape"].id,
            name="Lolegaon Mountain Stay",
            location="Lolegaon",
            image="/images/hotel-lolegaon.jpg",
            rating=4.4,
            price_per_night=2200,
            room_type="Wooden Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Mountain View",
            available_rooms=4,
            description=(
                "A quiet mountain cottage surrounded by forests, "
                "ideal for travelers looking for peace and nature."
            )
        ),


        # =================================================
        # SANDAKPHU HIMALAYAN QUEST
        # =================================================

        Hotel(
            trip_id=trip_map["Sandakphu Himalayan Quest"].id,
            name="Maneybhanjan Trekker's Lodge",
            location="Maneybhanjan",
            image="/images/hotel-maneybhanjan.jpg",
            rating=4.6,
            price_per_night=1800,
            room_type="Trekker Room",
            facilities="Breakfast,Parking,Hot Water,Guide Service",
            available_rooms=8,
            description=(
                "A convenient base for trekkers beginning the "
                "Sandakphu Himalayan trail."
            )
        ),

        Hotel(
            trip_id=trip_map["Sandakphu Himalayan Quest"].id,
            name="Sandakphu Mountain Lodge",
            location="Sandakphu",
            image="/images/hotel-sandakphu.jpg",
            rating=4.3,
            price_per_night=1600,
            room_type="Mountain Lodge Room",
            facilities="Breakfast,Hot Water,Mountain View,Guide Service",
            available_rooms=5,
            description=(
                "A basic mountain lodge offering shelter and "
                "spectacular Himalayan views for trekkers."
            )
        ),

        Hotel(
            trip_id=trip_map["Sandakphu Himalayan Quest"].id,
            name="Srikhola Riverside Stay",
            location="Srikhola",
            image="/images/hotel-srikhola.jpg",
            rating=4.7,
            price_per_night=2000,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,Garden,River View,Bonfire",
            available_rooms=6,
            description=(
                "A peaceful riverside stay surrounded by forests "
                "at the end of the Sandakphu trail."
            )
        ),


        # =================================================
        # TINCHULEY HIMALAYAN HIDEAWAY
        # =================================================

        Hotel(
            trip_id=trip_map["Tinchuley Himalayan Hideaway"].id,
            name="Tinchuley Mountain Homestay",
            location="Tinchuley",
            image="/images/hotel-tinchuley.jpg",
            rating=4.7,
            price_per_night=2200,
            room_type="Mountain View Room",
            facilities="Breakfast,Parking,Garden,Bonfire,Mountain View",
            available_rooms=6,
            description=(
                "A peaceful homestay surrounded by forests, tea gardens "
                "and spectacular Himalayan views."
            )
        ),

        Hotel(
            trip_id=trip_map["Tinchuley Himalayan Hideaway"].id,
            name="Takdah Forest Retreat",
            location="Takdah",
            image="/images/hotel-takdah-retreat.jpg",
            rating=4.6,
            price_per_night=2400,
            room_type="Forest Cottage",
            facilities="WiFi,Breakfast,Parking,Garden,Bonfire",
            available_rooms=5,
            description=(
                "A quiet forest retreat ideal for travelers looking "
                "for an offbeat Himalayan experience."
            )
        ),


        # =================================================
        # LEPCHA JAGAT
        # =================================================

        Hotel(
            trip_id=trip_map["Lepchajagat Forest Retreat"].id,
            name="Lepchajagat Forest Lodge",
            location="Lepchajagat",
            image="/images/hotel-lepchajagat.jpg",
            rating=4.6,
            price_per_night=2300,
            room_type="Forest View Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Birdwatching",
            available_rooms=6,
            description=(
                "A peaceful forest stay surrounded by tall pine trees "
                "and bird-filled mountain trails."
            )
        ),

        Hotel(
            trip_id=trip_map["Lepchajagat Forest Retreat"].id,
            name="Ghoom Mountain Retreat",
            location="Ghoom",
            image="/images/hotel-ghoom.jpg",
            rating=4.5,
            price_per_night=2600,
            room_type="Mountain View Deluxe",
            facilities="WiFi,Breakfast,Parking,Restaurant,Mountain View",
            available_rooms=5,
            description=(
                "A comfortable mountain retreat with convenient access "
                "to Ghoom and Darjeeling."
            )
        ),


        # =================================================
        # PEDONG HERITAGE TRAIL
        # =================================================

        Hotel(
            trip_id=trip_map["Pedong Heritage Trail"].id,
            name="Pedong Heritage Homestay",
            location="Pedong",
            image="/images/hotel-pedong.jpg",
            rating=4.6,
            price_per_night=2100,
            room_type="Heritage Room",
            facilities="Breakfast,Parking,Garden,Local Food,Bonfire",
            available_rooms=5,
            description=(
                "A warm mountain homestay offering local hospitality "
                "and peaceful views of the surrounding hills."
            )
        ),

        Hotel(
            trip_id=trip_map["Pedong Heritage Trail"].id,
            name="Sillery Gaon Eco Stay",
            location="Sillery Gaon",
            image="/images/hotel-sillery.jpg",
            rating=4.5,
            price_per_night=2000,
            room_type="Wooden Cottage",
            facilities="Breakfast,Garden,Bonfire,Mountain View,Parking",
            available_rooms=5,
            description=(
                "A quiet eco stay surrounded by pine forests and "
                "panoramic Himalayan landscapes."
            )
        ),


        # =================================================
        # SAMSING & SUNTALEKHOLA
        # =================================================

        Hotel(
            trip_id=trip_map["Samsing & Suntalekhola Wilderness"].id,
            name="Samsing Forest Retreat",
            location="Samsing",
            image="/images/hotel-samsing.jpg",
            rating=4.7,
            price_per_night=2400,
            room_type="Tea Garden Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Tea Garden View",
            available_rooms=6,
            description=(
                "A peaceful retreat surrounded by tea gardens and "
                "dense forests of the Dooars."
            )
        ),

        Hotel(
            trip_id=trip_map["Samsing & Suntalekhola Wilderness"].id,
            name="Suntalekhola Nature Camp",
            location="Suntalekhola",
            image="/images/hotel-suntalekhola.jpg",
            rating=4.6,
            price_per_night=2200,
            room_type="Forest Cottage",
            facilities="Breakfast,Parking,Bonfire,Guide Service,Forest View",
            available_rooms=6,
            description=(
                "A nature camp close to forest trails and mountain "
                "streams in Suntalekhola."
            )
        ),


        # =================================================
        # NEORA VALLEY
        # =================================================

        Hotel(
            trip_id=trip_map["Neora Valley Wild Trails"].id,
            name="Lava Wilderness Resort",
            location="Lava",
            image="/images/hotel-lava-wilderness.jpg",
            rating=4.7,
            price_per_night=2600,
            room_type="Forest View Room",
            facilities="Breakfast,Parking,Bonfire,Garden,Guide Service",
            available_rooms=6,
            description=(
                "A comfortable forest retreat near Lava, perfect "
                "for exploring the Neora Valley region."
            )
        ),

        Hotel(
            trip_id=trip_map["Neora Valley Wild Trails"].id,
            name="Kolakham Mountain Lodge",
            location="Kolakham",
            image="/images/hotel-kolakham.jpg",
            rating=4.6,
            price_per_night=2500,
            room_type="Mountain Cottage",
            facilities="Breakfast,Parking,Mountain View,Bonfire,Guide Service",
            available_rooms=5,
            description=(
                "A quiet mountain lodge surrounded by forests and "
                "spectacular views of the Himalayan landscape."
            )
        ),


        # =================================================
        # RISHYAP
        # =================================================

        Hotel(
            trip_id=trip_map["Rishyap Stargazing Escape"].id,
            name="Rishyap Star View Retreat",
            location="Rishyap",
            image="/images/hotel-rishyap.jpg",
            rating=4.7,
            price_per_night=2300,
            room_type="Mountain View Cottage",
            facilities="Breakfast,Parking,Bonfire,Mountain View,Stargazing",
            available_rooms=6,
            description=(
                "A peaceful mountain retreat with clear night skies "
                "and beautiful Himalayan views."
            )
        ),

        Hotel(
            trip_id=trip_map["Rishyap Stargazing Escape"].id,
            name="Lava Pine Forest Stay",
            location="Lava",
            image="/images/hotel-lava-pine.jpg",
            rating=4.5,
            price_per_night=2200,
            room_type="Pine Forest Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Mountain View",
            available_rooms=5,
            description=(
                "A cozy forest stay surrounded by pine trees and "
                "misty mountain landscapes."
            )
        ),


        # =================================================
        # SILLERY GAON
        # =================================================

        Hotel(
            trip_id=trip_map["Sillery Gaon Cloud Village"].id,
            name="Sillery Gaon Cloud Retreat",
            location="Sillery Gaon",
            image="/images/hotel-sillery-cloud.jpg",
            rating=4.6,
            price_per_night=2100,
            room_type="Mountain View Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Mountain View",
            available_rooms=6,
            description=(
                "A peaceful stay above the clouds surrounded by "
                "pine forests and Himalayan landscapes."
            )
        ),

        Hotel(
            trip_id=trip_map["Sillery Gaon Cloud Village"].id,
            name="Damsang Forest Homestay",
            location="Damsang",
            image="/images/hotel-damsang.jpg",
            rating=4.5,
            price_per_night=1900,
            room_type="Traditional Homestay",
            facilities="Breakfast,Parking,Garden,Local Food,Bonfire",
            available_rooms=4,
            description=(
                "A traditional mountain homestay surrounded by "
                "quiet forests and village trails."
            )
        ),


        # =================================================
        # RIMBICK
        # =================================================

        Hotel(
            trip_id=trip_map["Rimbick Valley Explorer"].id,
            name="Rimbick Valley Homestay",
            location="Rimbick",
            image="/images/hotel-rimbick.jpg",
            rating=4.7,
            price_per_night=2100,
            room_type="Mountain View Room",
            facilities="Breakfast,Parking,Garden,Local Food,Bonfire",
            available_rooms=6,
            description=(
                "A peaceful homestay surrounded by mountain villages, "
                "forests and beautiful valley landscapes."
            )
        ),

        Hotel(
            trip_id=trip_map["Rimbick Valley Explorer"].id,
            name="Srikhola Riverside Retreat",
            location="Srikhola",
            image="/images/hotel-srikhola-retreat.jpg",
            rating=4.6,
            price_per_night=2200,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,River View,Garden,Bonfire",
            available_rooms=5,
            description=(
                "A relaxing riverside retreat surrounded by forests "
                "and peaceful mountain scenery."
            )
        ),


        # =================================================
        # DOOARS RIVER & TEA TRAIL
        # =================================================

        Hotel(
            trip_id=trip_map["Dooars River & Tea Trail"].id,
            name="Rocky Island Riverside Camp",
            location="Rocky Island",
            image="/images/hotel-rocky-island.jpg",
            rating=4.6,
            price_per_night=2100,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,River View,Bonfire,Camping",
            available_rooms=6,
            description=(
                "A peaceful riverside camp surrounded by forests "
                "and the natural beauty of Dooars."
            )
        ),

        Hotel(
            trip_id=trip_map["Dooars River & Tea Trail"].id,
            name="Murti River Resort",
            location="Murti",
            image="/images/hotel-murti-resort.jpg",
            rating=4.7,
            price_per_night=2800,
            room_type="River View Deluxe",
            facilities="WiFi,Breakfast,Parking,Restaurant,River View",
            available_rooms=7,
            description=(
                "A comfortable riverside resort offering scenic views "
                "and easy access to Dooars attractions."
            )
        ),


        # =================================================
        # MEGHALAYA CLOUDSCAPE
        # =================================================

        Hotel(
            trip_id=trip_map["Meghalaya Cloudscape"].id,
            name="Shillong Hills Retreat",
            location="Shillong",
            image="/images/hotel-shillong.jpg",
            rating=4.6,
            price_per_night=2800,
            room_type="Mountain View Deluxe",
            facilities="WiFi,Breakfast,Parking,Restaurant,Mountain View",
            available_rooms=7,
            description=(
                "A comfortable hill retreat offering peaceful surroundings "
                "and convenient access to Shillong's major attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Meghalaya Cloudscape"].id,
            name="Sohra Valley Lodge",
            location="Sohra",
            image="/images/hotel-sohra.jpg",
            rating=4.7,
            price_per_night=3000,
            room_type="Valley View Cottage",
            facilities="WiFi,Breakfast,Parking,Bonfire,Valley View",
            available_rooms=5,
            description=(
                "A peaceful stay surrounded by misty valleys, waterfalls "
                "and the dramatic landscapes of Sohra."
            )
        ),

        Hotel(
            trip_id=trip_map["Meghalaya Cloudscape"].id,
            name="Laitlum Mountain Stay",
            location="Laitlum",
            image="/images/hotel-laitlum.jpg",
            rating=4.5,
            price_per_night=2600,
            room_type="Valley View Cottage",
            facilities="Breakfast,Parking,Garden,Bonfire,Valley View",
            available_rooms=4,
            description=(
                "A quiet mountain stay offering beautiful valley views "
                "and a peaceful escape from the city."
            )
        ),


        # =================================================
        # DAWKI & LIVING ROOTS
        # =================================================

        Hotel(
            trip_id=trip_map["Dawki & Living Roots"].id,
            name="Shnongpdeng Riverside Camp",
            location="Shnongpdeng",
            image="/images/hotel-shnongpdeng.jpg",
            rating=4.7,
            price_per_night=2200,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,River View,Boating,Bonfire",
            available_rooms=8,
            description=(
                "A riverside stay beside the peaceful waters of "
                "Shnongpdeng, perfect for nature and adventure travelers."
            )
        ),

        Hotel(
            trip_id=trip_map["Dawki & Living Roots"].id,
            name="Dawki Valley Retreat",
            location="Dawki",
            image="/images/hotel-dawki.jpg",
            rating=4.6,
            price_per_night=2500,
            room_type="Deluxe Valley Room",
            facilities="WiFi,Breakfast,Parking,Garden,Restaurant",
            available_rooms=6,
            description=(
                "A comfortable retreat close to Dawki's famous river "
                "and surrounding attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Dawki & Living Roots"].id,
            name="Mawlynnong Nature Stay",
            location="Mawlynnong",
            image="/images/hotel-mawlynnong.jpg",
            rating=4.5,
            price_per_night=2300,
            room_type="Eco Cottage",
            facilities="Breakfast,Garden,Parking,Local Food,Nature Walk",
            available_rooms=5,
            description=(
                "An eco-friendly stay surrounded by greenery and "
                "the peaceful village landscape of Mawlynnong."
            )
        ),


        # =================================================
        # SOHRA WATERFALL TRAIL
        # =================================================

        Hotel(
            trip_id=trip_map["Sohra Waterfall Trail"].id,
            name="Sohra Misty Heights",
            location="Sohra",
            image="/images/hotel-sohra-heights.jpg",
            rating=4.6,
            price_per_night=2400,
            room_type="Mountain View Room",
            facilities="WiFi,Breakfast,Parking,Restaurant,Bonfire",
            available_rooms=6,
            description=(
                "A cozy mountain stay surrounded by misty hills "
                "and the natural landscapes of Sohra."
            )
        ),

        Hotel(
            trip_id=trip_map["Sohra Waterfall Trail"].id,
            name="Nongriat Forest Homestay",
            location="Nongriat",
            image="/images/hotel-nongriat.jpg",
            rating=4.5,
            price_per_night=1800,
            room_type="Traditional Homestay",
            facilities="Breakfast,Local Food,Guide Service,Garden",
            available_rooms=4,
            description=(
                "A simple traditional stay offering an immersive experience "
                "close to the famous living root bridges."
            )
        ),


        # =================================================
        # KAZIRANGA WILD TRAILS
        # =================================================

        Hotel(
            trip_id=trip_map["Kaziranga Wild Trails"].id,
            name="Kaziranga Jungle Retreat",
            location="Kohora",
            image="/images/hotel-kaziranga.jpg",
            rating=4.8,
            price_per_night=3200,
            room_type="Forest View Cottage",
            facilities="WiFi,Breakfast,Parking,Restaurant,Bonfire,Safari Desk",
            available_rooms=8,
            description=(
                "A peaceful jungle retreat near Kaziranga's main safari "
                "zone, ideal for wildlife enthusiasts."
            )
        ),

        Hotel(
            trip_id=trip_map["Kaziranga Wild Trails"].id,
            name="Rhino Valley Resort",
            location="Kohora",
            image="/images/hotel-rhino-valley.jpg",
            rating=4.7,
            price_per_night=2900,
            room_type="Deluxe Cottage",
            facilities="WiFi,Breakfast,Parking,Restaurant,Garden,Safari Desk",
            available_rooms=7,
            description=(
                "A comfortable wildlife-themed resort offering easy access "
                "to Kaziranga's surrounding attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Kaziranga Wild Trails"].id,
            name="Kaziranga Riverside Lodge",
            location="Bokakhat",
            image="/images/hotel-kaziranga-river.jpg",
            rating=4.6,
            price_per_night=2700,
            room_type="Riverside Cottage",
            facilities="WiFi,Breakfast,Parking,Restaurant,River View",
            available_rooms=6,
            description=(
                "A peaceful lodge offering comfortable accommodation "
                "near the landscapes surrounding Kaziranga."
            )
        ),


        # =================================================
        # MAJULI CULTURAL JOURNEY
        # =================================================

        Hotel(
            trip_id=trip_map["Majuli Cultural Journey"].id,
            name="Majuli Bamboo Retreat",
            location="Majuli",
            image="/images/hotel-majuli.jpg",
            rating=4.6,
            price_per_night=2200,
            room_type="Bamboo Cottage",
            facilities="Breakfast,Parking,Garden,Local Food,Bicycle",
            available_rooms=6,
            description=(
                "A peaceful bamboo cottage surrounded by the natural "
                "landscape and cultural life of Majuli."
            )
        ),

        Hotel(
            trip_id=trip_map["Majuli Cultural Journey"].id,
            name="Mishing Heritage Homestay",
            location="Majuli",
            image="/images/hotel-mishing.jpg",
            rating=4.7,
            price_per_night=1900,
            room_type="Traditional Cottage",
            facilities="Breakfast,Local Food,Garden,Cultural Experience",
            available_rooms=5,
            description=(
                "Experience traditional island hospitality while staying "
                "close to local villages and cultural attractions."
            )
        ),

        Hotel(
            trip_id=trip_map["Majuli Cultural Journey"].id,
            name="Kamalabari Riverside Stay",
            location="Kamalabari",
            image="/images/hotel-kamalabari.jpg",
            rating=4.5,
            price_per_night=2100,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,Garden,River View,Bicycle",
            available_rooms=5,
            description=(
                "A peaceful island stay near Kamalabari with easy access "
                "to Majuli's cultural and natural attractions."
            )
        ),


        # =================================================
        # MANAS WILDERNESS EXPEDITION
        # =================================================

        Hotel(
            trip_id=trip_map["Manas Wilderness Expedition"].id,
            name="Manas Jungle Camp",
            location="Bansbari",
            image="/images/hotel-manas.jpg",
            rating=4.7,
            price_per_night=2800,
            room_type="Forest Cottage",
            facilities="Breakfast,Parking,Restaurant,Bonfire,Safari Desk",
            available_rooms=7,
            description=(
                "A peaceful jungle camp located close to Manas National "
                "Park and the surrounding forest."
            )
        ),

        Hotel(
            trip_id=trip_map["Manas Wilderness Expedition"].id,
            name="Manas Riverside Retreat",
            location="Bansbari",
            image="/images/hotel-manas-river.jpg",
            rating=4.6,
            price_per_night=2600,
            room_type="Riverside Cottage",
            facilities="Breakfast,Parking,River View,Restaurant,Guide Service",
            available_rooms=6,
            description=(
                "A quiet riverside retreat offering comfortable accommodation "
                "for travelers exploring the Manas wilderness."
            )
        )

    ]


    # =====================================================
    # INSERT HOTELS WITHOUT DUPLICATES
    # =====================================================

    for hotel in hotels:

        existing = (
            db.query(Hotel)
            .filter(
                Hotel.name == hotel.name,
                Hotel.trip_id == hotel.trip_id
            )
            .first()
        )

        if not existing:
            db.add(hotel)

    db.commit()


    # =====================================================
    # FINAL SUMMARY
    # =====================================================

    total_trips = db.query(Trip).count()
    total_hotels = db.query(Hotel).count()

    print("------------------------------------------")
    print("SEED COMPLETED SUCCESSFULLY")
    print("------------------------------------------")
    print(f"Total trips  : {total_trips}")
    print(f"Total hotels : {total_hotels}")
    print("------------------------------------------")


except Exception as error:

    db.rollback()

    print("------------------------------------------")
    print("SEED FAILED")
    print("------------------------------------------")
    print(error)
    print("------------------------------------------")

    raise


finally:

    db.close()