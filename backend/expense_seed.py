from database import SessionLocal, engine, Base
from models import StandardRate, TravelerExpense
from datetime import datetime

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    # -----------------------------------------------------
    # SEED STANDARD RATES
    # -----------------------------------------------------
    existing_rates = db.query(StandardRate).count()
    if existing_rates == 0:
        rates = [
            # TOTO
            StandardRate(destination="Siliguri", expense_type="Toto", route_or_service="NJP Railway Station to Siliguri Town / Junction", estimated_cost=120.0, cost_unit="per ride (reserve)", notes="Shared toto is ₹20-₹25 per person"),
            StandardRate(destination="Siliguri", expense_type="Toto", route_or_service="Siliguri Junction to Court More / Hong Kong Market", estimated_cost=20.0, cost_unit="per person", notes="Shared toto rate within town"),
            StandardRate(destination="Cooch Behar", expense_type="Toto", route_or_service="Cooch Behar Railway Station to Cooch Behar Palace", estimated_cost=100.0, cost_unit="per ride (reserve)", notes="Shared toto is ₹15-₹20 per seat"),
            StandardRate(destination="Alipurduar", expense_type="Toto", route_or_service="New Alipurduar Junction to Bus Stand / Town", estimated_cost=15.0, cost_unit="per person", notes="Standard shared fare"),
            StandardRate(destination="Malbazar", expense_type="Toto", route_or_service="Malbazar Station to Dooars Bus Stand", estimated_cost=30.0, cost_unit="per ride", notes="Local short transit"),
            
            # BUS
            StandardRate(destination="Darjeeling", expense_type="Bus", route_or_service="Siliguri (Tenzing Norgay Bus Stand) to Darjeeling", estimated_cost=120.0, cost_unit="per person", notes="NBSTC Government Bus, duration ~3.5-4 hrs"),
            StandardRate(destination="Kalimpong", expense_type="Bus", route_or_service="Siliguri to Kalimpong via Teesta Bazar", estimated_cost=110.0, cost_unit="per person", notes="NBSTC / Private Bus, duration ~3 hrs"),
            StandardRate(destination="Mirik", expense_type="Bus", route_or_service="Siliguri to Mirik Lake", estimated_cost=90.0, cost_unit="per person", notes="Local bus route through tea gardens"),
            StandardRate(destination="Jaldapara", expense_type="Bus", route_or_service="Siliguri to Madarihat (Jaldapara Sanctuary)", estimated_cost=160.0, cost_unit="per person", notes="Regular NBSTC Dooars service"),

            # TRAIN
            StandardRate(destination="Darjeeling", expense_type="Train", route_or_service="DHR Toy Train Joyride (Darjeeling to Ghum & back)", estimated_cost=1500.0, cost_unit="per person", notes="Heritage Steam Joyride, Diesel is ~₹1000"),
            StandardRate(destination="Darjeeling", expense_type="Train", route_or_service="DHR Toy Train Regular (NJP to Darjeeling full route)", estimated_cost=1420.0, cost_unit="per person", notes="Scenic mountain railway"),
            StandardRate(destination="Dooars", expense_type="Train", route_or_service="Vistadome Express (NJP to Alipurduar via Dooars)", estimated_cost=770.0, cost_unit="per person", notes="Scenic glass dome coach"),

            # SHARED JEEP
            StandardRate(destination="Darjeeling", expense_type="Shared Jeep", route_or_service="Siliguri (Junction Jeep Stand) to Darjeeling Clubside", estimated_cost=300.0, cost_unit="per person", notes="Bolero/Sumo shared seat. Reserved taxi is ₹2800-₹3500"),
            StandardRate(destination="Kalimpong", expense_type="Shared Jeep", route_or_service="Siliguri Junction to Kalimpong Jeep Stand", estimated_cost=250.0, cost_unit="per person", notes="Shared seat"),
            StandardRate(destination="Kurseong", expense_type="Shared Jeep", route_or_service="Siliguri to Kurseong Tourist Hub", estimated_cost=180.0, cost_unit="per person", notes="Shared vehicle"),

            # HOMESTAY
            StandardRate(destination="Chatakpur", expense_type="Homestay", route_or_service="Village Eco-Homestay with organic meals", estimated_cost=1500.0, cost_unit="per person/night", notes="Includes warm hospitality & 4 meals"),
            StandardRate(destination="Takdah", expense_type="Homestay", route_or_service="Colonial Tea Heritage Homestay with all meals", estimated_cost=1400.0, cost_unit="per person/night", notes="Tea garden village stay"),
            StandardRate(destination="Lamahatta", expense_type="Homestay", route_or_service="Pine Forest Village Homestay with meals", estimated_cost=1300.0, cost_unit="per person/night", notes="Near Lamahatta Eco Park"),
            StandardRate(destination="Sittong", expense_type="Homestay", route_or_service="Orange Valley Homestay with organic food", estimated_cost=1200.0, cost_unit="per person/night", notes="Famous orange village"),

            # FOOD
            StandardRate(destination="Darjeeling", expense_type="Food", route_or_service="Darjeeling Momos (Steamed Veg/Chicken 8 pcs)", estimated_cost=100.0, cost_unit="per plate", notes="Mall Road & local street cafe rate"),
            StandardRate(destination="Darjeeling", expense_type="Food", route_or_service="Thukpa (Tibetan Noodle Soup)", estimated_cost=120.0, cost_unit="per bowl", notes="Fresh mountain broth noodle soup"),
            StandardRate(destination="Siliguri", expense_type="Food", route_or_service="Authentic Bengali Fish / Thali Lunch", estimated_cost=180.0, cost_unit="per thali", notes="Rice, dal, sabzi, fish curry, papad"),
        ]
        db.bulk_save_objects(rates)
        db.commit()
        print("Standard benchmark rates seeded successfully.")

    # -----------------------------------------------------
    # SEED INITIAL SAMPLE EXPENSES
    # -----------------------------------------------------
    existing_expenses = db.query(TravelerExpense).count()
    if existing_expenses == 0:
        expenses = [
            TravelerExpense(destination_name="Siliguri", category="Transport", sub_category="Toto", item_title="Toto from NJP station gate to Siliguri Junction Jeep Stand", amount=120.0, payment_method="Cash", origin_point="NJP Railway Station", destination_point="Siliguri Junction", expense_date=datetime(2026, 11, 1, 8, 30), number_of_people=2, notes="Reserved toto for 2 passengers"),
            TravelerExpense(destination_name="Darjeeling", category="Transport", sub_category="Shared Jeep", item_title="Shared Bolero jeep to Darjeeling Clubside", amount=600.0, payment_method="Cash", origin_point="Siliguri Junction", destination_point="Darjeeling Clubside", expense_date=datetime(2026, 11, 1, 9, 15), number_of_people=2, notes="₹300 per seat x 2 passengers"),
            TravelerExpense(destination_name="Darjeeling", category="Food & Dining", sub_category="Food", item_title="Hot steamed momos & tea at Mall Road", amount=240.0, payment_method="UPI / GPay / PhonePe", origin_point="Mall Road", destination_point="Mall Road", expense_date=datetime(2026, 11, 1, 14, 0), number_of_people=2, notes="Lunch"),
            TravelerExpense(destination_name="Takdah", category="Homestay & Lodging", sub_category="Homestay", item_title="Takdah Heritage Homestay (Night 1) with meals", amount=2800.0, payment_method="UPI / GPay / PhonePe", origin_point="Takdah Cantonment", destination_point="Takdah Cantonment", expense_date=datetime(2026, 11, 1, 19, 30), number_of_people=2, notes="₹1400 per head including organic dinner & breakfast"),
            TravelerExpense(destination_name="Darjeeling", category="Transport", sub_category="Train", item_title="DHR Himalayan Toy Train Steam Joyride", amount=3000.0, payment_method="Card", origin_point="Darjeeling Station", destination_point="Ghum Station", expense_date=datetime(2026, 11, 2, 10, 0), number_of_people=2, notes="Steam engine joyride tickets"),
            TravelerExpense(destination_name="Darjeeling", category="Transport", sub_category="Bus", item_title="NBSTC Local Bus from Ghoom to Kurseong", amount=70.0, payment_method="Cash", origin_point="Ghoom", destination_point="Kurseong", expense_date=datetime(2026, 11, 2, 15, 30), number_of_people=2, notes="₹35 per ticket x 2"),
        ]
        db.bulk_save_objects(expenses)
        db.commit()
        print("Sample traveler expenses seeded successfully.")

except Exception as err:
    db.rollback()
    print("Error during seed:", err)
finally:
    db.close()
