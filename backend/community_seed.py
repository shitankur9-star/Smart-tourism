from database import SessionLocal, engine, Base
from models import PlaceHistory, CommunityPost, CommunityComment
from datetime import datetime

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    # =====================================================
    # 1. SEED RICH PLACE HISTORIES & WEATHER
    # =====================================================
    existing_histories = db.query(PlaceHistory).count()
    if existing_histories == 0:
        places = [
            # DARJEELING
            PlaceHistory(
                destination_name="Darjeeling",
                district="Darjeeling",
                tagline="Queen of the Hills & Home of the World's Finest Champagne of Teas",
                name_etymology="Derived from the Tibetan words 'Dorje' (meaning the mythical thunderbolt sceptre of Indra/vajra) and 'Ling' (meaning place or land) — literally 'The Land of the Thunderbolt'.",
                history_full=(
                    "Originally a small village under the Kingdom of Sikkim, Darjeeling was identified in 1828 by British officers Captain Lloyd and J.W. Grant as an ideal location for a sanatorium for British troops. "
                    "In 1835, the Chogyal (King) of Sikkim ceded the uninhabited hill territory to the British East India Company under a deed of grant. "
                    "In 1841, Dr. Archibald Campbell, the first superintendent of Darjeeling, brought Chinese tea seeds from Kumaon and planted them at Beechwood, initiating the commercial cultivation of what became known worldwide as 'The Champagne of Teas'. "
                    "By the 1850s, tea plantations expanded rapidly across the hillsides, bringing migrant Nepali, Lepcha, and Bhutia workers who shaped the vibrant cosmopolitan hill culture. "
                    "In 1881, visionary engineer Franklin Prestage completed the legendary Darjeeling Himalayan Railway (DHR), an 88-kilometer two-foot narrow-gauge mountain railway with loops and zig-zags that ascended over 2,000 meters. The DHR was declared a UNESCO World Heritage Site in 1999."
                ),
                colonial_era="British sanitarium established in 1835. Historic stone bungalows, clock towers, Planters' Club (1868), St. Paul's School (1864), and Glenary's bakery (1913).",
                cultural_heritage="A rich blend of Gorkha (Nepali), Tibetan Buddhist, Lepcha, and Bhutia traditions. Famous for colorful Losar (Tibetan New Year), Dashain, Tihar festivals, and sacred Buddhist butter sculptures at Bhutia Busty & Ghoom Monasteries.",
                historical_landmarks="Darjeeling Himalayan Railway (1881), Tiger Hill, Ghoom Monastery (1875), Himalayan Mountaineering Institute (founded 1954 by Tenzing Norgay), Observatory Hill & Mahakal Temple, Glenary's.",
                current_weather="12°C - 17°C, Misty & Pleasant Breeze",
                temperature_range="Summer: 10°C - 19°C | Winter: 1°C - 9°C",
                weather_condition="Partly Cloudy with Drifting Mountain Mist",
                best_season_to_visit="October to May (crystal clear Kanchenjunga panoramas); March-April (blooming Rhododendrons and Magnolias).",
                altitude="2,042 meters (6,700 feet)",
                local_transport_guide="Shared Bolero/Sumo from Siliguri Junction ₹300-₹350; NBSTC Mountain Bus ₹120; DHR Steam Joyride ₹1500; Local town walking & Mall Road promenade.",
                image_url="/assets/NB-1.jpeg"
            ),

            # KALIMPONG
            PlaceHistory(
                destination_name="Kalimpong",
                district="Kalimpong",
                tagline="Historic Gateway to Tibet & Land of Exotic Himalayan Orchids",
                name_etymology="Derived from the indigenous Lepcha name 'Kalenpung' meaning 'Ridge where we play', or Tibetan 'Kalim-pong' meaning 'Black Spur'.",
                history_full=(
                    "For centuries, Kalimpong was ruled by the Chogyals of Sikkim until 1706, when it was invaded and annexed by the Kingdom of Bhutan. "
                    "Following the Anglo-Bhutanese War in 1864-1865, the British East India Company secured the region through the historic Treaty of Sinchula. "
                    "Due to its prime geographical gateway near the Jelep La pass, Kalimpong transformed into the bustling terminus of the trans-Himalayan trade corridor between British India and Tibet. "
                    "Caravans loaded with Tibetan wool, yak tails, and silk arrived through the mountain passes until the Sino-Indian border closure in 1962. "
                    "Scottish missionaries established Dr. Graham's Homes in 1900 on a 500-acre self-contained educational township. "
                    "Rabindranath Tagore spent multiple birthdays here at Gauripur House, where he famously broadcast his poem 'Janmadin' via all-India telephone radio in 1940."
                ),
                colonial_era="Morgan House (British colonial estate built in 1930s by jute baron George Morgan), Crockety Bungalow, and Dr. Graham's Homes (1900).",
                cultural_heritage="Harmonious tapestry of Lepcha (the original inhabitants), Nepali, Tibetan, and Bhutanese communities. World-renowned for indigenous gladioli and orchid nurseries exporting worldwide.",
                historical_landmarks="Morgan House, Deolo Hill (1704 m), Zang Dhok Palri Phodang (Durpin Monastery, consecrated by the 14th Dalai Lama in 1976), Pine View Orchid Nursery, Gauripur House.",
                current_weather="16°C - 23°C, Sunny & Mild",
                temperature_range="Summer: 15°C - 26°C | Winter: 7°C - 15°C",
                weather_condition="Clear Blue Skies with Mild Valley Wind",
                best_season_to_visit="September to December & March to June.",
                altitude="1,247 meters (4,091 feet)",
                local_transport_guide="Shared Jeep from Siliguri Junction ₹250 (3 hours); NBSTC Bus ₹110; Local shared taxi across town ₹20-₹30.",
                image_url="/assets/NB-2.jpeg"
            ),

            # KURSEONG
            PlaceHistory(
                destination_name="Kurseong",
                district="Darjeeling",
                tagline="Land of the White Orchids & World's Oldest Tea Heritage",
                name_etymology="Derived from the Lepcha word 'Kharsang' which translates to 'The Land of the White Orchids' because of the wild orchids that blanket the hillsides.",
                history_full=(
                    "Kurseong was ceded by the Kingdom of Sikkim to British India in 1835. The British immediately recognized its temperate climate—milder than Darjeeling—as ideal for recuperating soldiers and established sanatoriums and prestigious boarding schools. "
                    "In 1859, the pioneering Makaibari Tea Estate was founded here by Captain Samler, becoming the world's first registered tea estate and factory. "
                    "When the Darjeeling Himalayan Railway was constructed, Kurseong became a vital central railway junction and maintenance hub where the tracks uniquely weave straight through the bustling main street. "
                    "Sister Nivedita lived and meditated here, and Rabindranath Tagore stayed at Giddapahar to write parts of 'Gitanjali'."
                ),
                colonial_era="Goethals Memorial School (1907), Dow Hill Heritage School (1879), and the Chimney at Dow Hill (a historic smoke-tower erected in 1839).",
                cultural_heritage="Lepcha and Nepali tea garden folklore, organic biodynamic tea culture, and sacred mountain viewpoints.",
                historical_landmarks="Makaibari Tea Estate (1859), Eagle's Crag Viewpoint, Dow Hill Forest & Heritage Museum, Chimney (1839), DHR Kurseong Station.",
                current_weather="14°C - 19°C, Fresh Mountain Air",
                temperature_range="Summer: 14°C - 21°C | Winter: 4°C - 12°C",
                weather_condition="Gentle Mist with Occasional Sunshine",
                best_season_to_visit="March to May and September to November.",
                altitude="1,458 meters (4,783 feet)",
                local_transport_guide="Shared Jeep from Siliguri Junction ₹180 (1.5 hours); Toy Train passes through city center; Shared hops in town ₹15-₹25.",
                image_url="/assets/NB-3.jpeg"
            ),

            # COOCH BEHAR
            PlaceHistory(
                destination_name="Cooch Behar",
                district="Cooch Behar",
                tagline="Royal City of the Koch Dynasty & The Italian Renaissance Palace of Bengal",
                name_etymology="From 'Koch' (the indigenous Rajbanshi ruling clan) and 'Bihar/Behar' (Sanskrit for journey or abode) — 'The Abode of the Koch People'.",
                history_full=(
                    "Cooch Behar was the seat of the mighty Koch Dynasty founded in 1515 by Maharaja Viswa Singha. Under his son Maharaja Nara Narayan and the invincible general Chilarai, the kingdom reached the pinnacle of military power, diplomacy, and scholarship across Assam and Bengal. "
                    "In 1887, enlightened ruler Maharaja Nripendra Narayan commissioned the construction of the Victor Jubilee Palace (Cooch Behar Palace). Designed in Italian Renaissance architecture and modeled faithfully on London's Buckingham Palace, it features magnificent Corinthian columns, grand arches, and a breathtaking central dome. "
                    "The celebrated Maharani Gayatri Devi of Jaipur, admired worldwide for her poise and democratic advocacy, was born here as the Princess of Cooch Behar. "
                    "The princely kingdom formally acceded to the Union of India in August 1949 and was integrated as a district of West Bengal in 1950."
                ),
                colonial_era="Victor Jubilee Palace (1887), British treaty residences, Sagardighi heritage administrative quarter.",
                cultural_heritage="Rajbanshi language and traditions, classical Bhawaiya folk music, ancient Madan Mohan temple rituals, and the historic Ras Mela carnival held annually since 1812.",
                historical_landmarks="Cooch Behar Palace, Madan Mohan Temple (1889), Sagardighi Royal Lake, Baneswar Shiva Temple (sacred ancient pond with Mohan tortoises), Gosanimari Fort ruins.",
                current_weather="24°C - 30°C, Pleasant Autumn Sunshine",
                temperature_range="Summer: 25°C - 34°C | Winter: 10°C - 22°C",
                weather_condition="Clear Sunny Skies",
                best_season_to_visit="October to March (cool weather, illuminated palaces, and the vibrant Ras Mela festival).",
                altitude="48 meters (157 feet)",
                local_transport_guide="Toto (E-rickshaw) is the king of travel here! ₹15-₹20 per shared hop across town, or ₹100 reserve; Trains arrive at New Cooch Behar (NCB).",
                image_url="/assets/NB-5.jpeg"
            ),

            # BUXA & JAYANTI
            PlaceHistory(
                destination_name="Buxa",
                district="Alipurduar",
                tagline="Ancient Mountain Citadel & Historic Freedom Struggle Detention Camp",
                name_etymology="Derived from 'Buxa Duar' (Door/Gateway), one of the historically guarded 18 mountain passes connecting the plains of Bengal to the Kingdom of Bhutan.",
                history_full=(
                    "Buxa Fort is one of the most enigmatic mountain fortresses in Eastern India, perched on a steep spur guarding the ancient silk route between Tibet, Bhutan, and Cooch Behar. "
                    "Controlled originally by the King of Bhutan, the fort was captured by the British in 1865 following the Bhutan War. "
                    "In the 1930s, the British transformed Buxa Fort into a dreaded, high-security penal detention camp. "
                    "Hundreds of India's prominent freedom fighters, revolutionaries, and political prisoners associated with Netaji Subhash Chandra Bose and revolutionary societies were incarcerated here behind thick stone walls and dense malaria-infested wilderness. "
                    "Rabindranath Tagore penned letters and poems to the imprisoned revolutionaries, and Mahatma Gandhi advocated for their release. In 1959, following the Tibetan uprising, thousands of Tibetan monks sought refuge at Buxa Fort, establishing monastic colleges before relocating to Bylakuppe."
                ),
                colonial_era="Buxa Fort stone detention cells, colonial stone pathways, and the Santalabari military outpost.",
                cultural_heritage="Indigenous Rava, Mech, and Dukpa hill communities living along the pristine Jayanti River bed and mountain ridgelines.",
                historical_landmarks="Buxa Fort (accessible via 3 km scenic trek from Santalabari), Jayanti River Bed, Mahakal Cave, Pokhari Hill (sacred catfish pond), Buxa Tiger Reserve.",
                current_weather="20°C - 27°C, Forest Canopy Breeze",
                temperature_range="Summer: 20°C - 31°C | Winter: 10°C - 21°C",
                weather_condition="Sunny with Humid Forest Canopy",
                best_season_to_visit="November to April (safaris and trekking trails are dry; park closed in monsoon).",
                altitude="867 meters (2,844 feet at the Fort)",
                local_transport_guide="Train to Alipurduar Junction; Shared Jeep/Auto to Rajabhatkhawa & Santalabari ₹60-₹100; Trek 3 km to Buxa Fort; Toto within Alipurduar ₹15-₹20.",
                image_url="/assets/buxa.jpeg"
            ),

            # TAKDAH & LAMAHATTA
            PlaceHistory(
                destination_name="Takdah",
                district="Darjeeling",
                tagline="British Cantonment of Colonial Stone Bungalows & Enchanted Pine Trails",
                name_etymology="'Takdah' is an indigenous Lepcha word meaning 'mist' or 'hidden clouds'. 'Lamahatta' means 'Hermitage of the Buddhist Monks' (Lama = monk, Hatta = hut/dwelling).",
                history_full=(
                    "In the early 1900s during the British Raj, Takdah was chosen as a strategic military cantonment for British Indian Army officers. "
                    "Between 1905 and 1915, British engineers erected more than 15 classic stone bungalows with high gabled roofs, stone fireplaces, and European rose gardens, known as 'Rani Kothi' and 'Club Bungalows'. "
                    "When the cantonment was decommissioned post-independence, the quiet tea garden village preserved the architectural treasures, which are now lovingly run as heritage eco-homestays. "
                    "Nearby Lamahatta was developed in 2012 as an eco-tourism park by local villagers, showcasing ancient Buddhist lakes, colorful prayer flags, and soaring dhupi pine forests."
                ),
                colonial_era="Colonial Stone Bungalows No. 12, 16, and the Old British Club house nestled among Rangli Rangliot and Teesta Valley tea estates.",
                cultural_heritage="Warm Nepali and Lepcha hospitality, traditional organic farming, Tibetan prayer flags, and indigenous orchid cultivation.",
                historical_landmarks="British Colonial Bungalow Heritage, Takdah Orchid Sanctuary, Lamahatta Eco Park, Sacred Pokhari Lake, Rangli Rangliot Tea Estate.",
                current_weather="13°C - 18°C, Poetic Mist",
                temperature_range="Summer: 12°C - 20°C | Winter: 3°C - 11°C",
                weather_condition="Enveloped in Romantic Mountain Mist",
                best_season_to_visit="October to May for mountain views and blooming wild orchids.",
                altitude="1,800 meters (5,900 feet)",
                local_transport_guide="Shared Bolero from Siliguri Junction or Darjeeling to Takdah ₹150-₹200; Homestays cost ₹1200-₹1500 per person including all 4 meals.",
                image_url="/assets/NB-4.jpeg"
            ),

            # MIRIK
            PlaceHistory(
                destination_name="Mirik",
                district="Darjeeling",
                tagline="Serene Sumendu Lake Nestled in Cardamom & Tea Hills",
                name_etymology="Derived from the Lepcha name 'Mir-Yok' which translates to 'Place burnt by fire', referring to an ancient local clearing.",
                history_full=(
                    "Historically, Mirik was a peaceful village along the cardamom and orange trade route bordering Nepal. "
                    "In 1974, the West Bengal Tourism Department recognized its potential and transformed the central marshland into the iconic 1.25 km long Sumendu Lake, fringed with weeping willows and pine forests. "
                    "The graceful 80-foot arched rainbow footbridge ('Indreni Bridge') was built to link the eastern bank flower gardens with the western pine trails. "
                    "Mirik is surrounded by the celebrated Thurbo Tea Estate, one of the most sprawling and picturesque estates in the eastern Himalayas."
                ),
                colonial_era="Colonial tea garden superintendent bungalows at Thurbo and historic Nepal-border trade routes.",
                cultural_heritage="Lepcha and Nepali cultural harmony, Tibetan Buddhism at Bokar Monastery, and orange orchard traditions.",
                historical_landmarks="Sumendu Lake & Indreni Bridge, Tingling Tea View Point, Bokar Buddhist Monastery, Swiss Cottage, Pashupati Nagar (Indo-Nepal border).",
                current_weather="15°C - 21°C, Refreshing Lake Breeze",
                temperature_range="Summer: 15°C - 24°C | Winter: 5°C - 14°C",
                weather_condition="Mild Sunshine with Cool Lake Breeze",
                best_season_to_visit="September to December and March to June.",
                altitude="1,495 meters (4,905 feet)",
                local_transport_guide="Direct NBSTC Bus from Siliguri ₹90 (2.5 hrs); Shared Jeep ₹150; Lake paddle boat ₹100; Horse riding ₹150.",
                image_url="/assets/mirik.jpeg"
            ),

            # CHATAKPUR
            PlaceHistory(
                destination_name="Chatakpur",
                district="Darjeeling",
                tagline="High-Altitude Eco-Village Sanctuary Facing the Kanchenjunga",
                name_etymology="Named after the elusive 'Chatak' bird (Jacobin cuckoo) of local mythology that drinks solely pristine raindrops falling from the skies.",
                history_full=(
                    "Hidden deep within the Senchal Wildlife Sanctuary—established in 1915 as one of India's earliest wildlife sanctuaries—Chatakpur was a quiet settlement of forest wardens and indigenous hill farmers. "
                    "In the 2000s, the West Bengal Forest Department collaborated with the 20 resident families to pioneer an organic, plastic-free eco-tourism model. "
                    "Positioned at an extraordinary elevation of nearly 7,900 feet, Chatakpur offers completely unhindered 360-degree sunrise vistas of the Kanchenjunga range in tranquil silence, untouched by vehicular traffic."
                ),
                colonial_era="Part of the 1915 Senchal Forest Sanctuary timber conservation zone protecting water catchment reservoirs for Darjeeling.",
                cultural_heritage="100% organic hill farming, traditional wooden cottage architecture, sacred Buddhist water pond veneration, and rich Sherpa & Nepali culture.",
                historical_landmarks="Chatakpur Sunrise Watchtower, Senchal Wildlife Sanctuary trail, Sacred Pokhari, Ancient Oak and Rhododendron canopy.",
                current_weather="8°C - 15°C, Crisp Alpine Cold",
                temperature_range="Summer: 8°C - 16°C | Winter: -1°C - 7°C",
                weather_condition="Crisp Alpine Cold with Clear Mountain Skies",
                best_season_to_visit="October to May (breathtaking morning snow peaks and Rhododendron blooms).",
                altitude="2,392 meters (7,887 feet)",
                local_transport_guide="4WD Bolero required from Dilaram / Sonada (₹1800-₹2200 reserved); Homestay ₹1500/night with organic meals.",
                image_url="/assets/chatpukur.jpeg"
            ),

            # JALDAPARA & LATAGURI (DOOARS)
            PlaceHistory(
                destination_name="Jaldapara",
                district="Alipurduar",
                tagline="Gateway to Bhutan & The Historic Fortress of the One-Horned Rhinoceros",
                name_etymology="'Dooars' originates from the Bengali and Assamese word 'Dwar' (Door/Gateway) to Bhutan. 'Jaldapara' translates to the settlement beside the flowing waters (Torsa River).",
                history_full=(
                    "Jaldapara was established as a wildlife sanctuary in 1941 to save the endangered Greater One-Horned Rhinoceros from extinction due to rampant poaching. "
                    "Upgraded to a National Park in 2012, its vast alluvial elephant-grass meadows and riverine sal forests hold the second largest population of one-horned rhinos in India after Kaziranga. "
                    "Nearby Totopara is the exclusive homeland of the Toto tribe—one of the smallest, most endangered indigenous tribal groups in the entire world, possessing their own distinct spoken language and heritage."
                ),
                colonial_era="Hollong Forest Lodge built during British forestry administration, and historic river crossings of the Bengal Dooars Railway.",
                cultural_heritage="Rava, Mech, and Toto tribal folklore, forest rituals, traditional bamboo craft, and elephant-keeper (Mahout) lineages.",
                historical_landmarks="Hollong Elephant Safari, Jaldapara Rhino Watchtower, Totopara Village, Chilapata Forest ruins (Nalraja Garh 5th century fort), Gorumara Rhino point.",
                current_weather="22°C - 29°C, Tropical Sunshine",
                temperature_range="Summer: 22°C - 33°C | Winter: 11°C - 23°C",
                weather_condition="Warm Sunshine with Forest Humidity",
                best_season_to_visit="October to May (park closed during monsoon June 15 to Sept 15).",
                altitude="61 meters (200 feet)",
                local_transport_guide="NBSTC Bus from Siliguri to Madarihat ₹160; Jeep Safari ₹2200/vehicle; Shared Toto across town ₹20-₹30.",
                image_url="/assets/kaziranga_national-park.jpeg"
            ),
        ]
        db.bulk_save_objects(places)
        db.commit()
        print("Rich North Bengal place histories & weather seeded successfully.")

    # =====================================================
    # 2. SEED COMMUNITY POSTS (TOURISTS & LOCAL RESIDENTS)
    # =====================================================
    existing_posts = db.query(CommunityPost).count()
    if existing_posts == 0:
        posts = [
            CommunityPost(
                author_name="Passang Tamang",
                author_type="Local Resident",
                author_location="Takdah Tea Village Local Guide",
                destination_name="Takdah",
                title="Secret Waterfall & Colonial Tea Trail in Takdah - Avoid Crowds!",
                post_type="Hidden Gem",
                rating=5.0,
                content=(
                    "Namaste travelers! As a resident of Takdah, I see most tourists only staying in crowded Darjeeling town. "
                    "If you take a shared jeep from Siliguri Junction to Takdah (₹200), you can stay in real 100-year-old British stone bungalows for just ₹1300 a night with all 4 homemade organic meals included. "
                    "Right behind the Takdah orchid center, there is a hidden 20-minute trail leading down to a crystal clear forest waterfall where practically no tourists go. "
                    "Ask any local for 'Chhange Fall'. Please remember to bring back all plastic waste!"
                ),
                total_expense=1450.0,
                expense_breakdown="Shared Jeep: ₹200 | Homestay with all meals: ₹1300 | Local Toto to orchid center: ₹40",
                weather_note="Misty & crisp, 14°C. Carry a warm fleece jacket.",
                image_url="/assets/NB-4.jpeg",
                likes_count=38,
                created_at=datetime(2026, 11, 2, 9, 30)
            ),

            CommunityPost(
                author_name="Ananya Sen",
                author_type="Tourist",
                author_location="Kolkata Solo Traveler",
                destination_name="Darjeeling",
                title="Our 3-Day Budget Trip to Darjeeling & Ghum - Full Real Expense Breakdown",
                post_type="Tourist Review",
                rating=4.9,
                content=(
                    "We did a 3-day Darjeeling trip on a tight student budget and it was phenomenal! "
                    "Key money-saving tip: DO NOT book private cabs from NJP station. Walk 100 meters out to the main gate, take a ₹20 Toto to Siliguri Junction Jeep Stand, and hop into a shared Bolero for ₹300. You save nearly ₹3000 right there! "
                    "We stayed near Ghoom in a friendly homestay where we watched the DHR Toy Train chug by from the dining window. "
                    "Food: Kunga's beef/chicken momos and steaming thukpa are totally worth the hype."
                ),
                total_expense=3150.0,
                expense_breakdown="NJP Toto: ₹20 | Shared Jeep to Darjeeling: ₹300 | Homestay 2 nights: ₹2200 | Momos & Tea: ₹350 | Local Shared hops: ₹80",
                weather_note="Morning sunshine (16°C), cold foggy evenings (8°C). Clear Kanchenjunga view at dawn!",
                image_url="/assets/NB-1.jpeg",
                likes_count=54,
                created_at=datetime(2026, 11, 3, 11, 15)
            ),

            CommunityPost(
                author_name="Bikram Roy",
                author_type="Local Resident",
                author_location="Cooch Behar Historian & Resident",
                destination_name="Cooch Behar",
                title="Best Way to Tour Cooch Behar Royal Palace & Rasikbil Lake by Toto",
                post_type="Local Suggestion",
                rating=5.0,
                content=(
                    "Welcome to our royal city! I have lived in Cooch Behar for 45 years. You do not need expensive tour operators here. "
                    "When you get down at New Cooch Behar station, hire a local electric Toto. For ₹350, the driver will take you on a complete historical loop: "
                    "1. The Victor Jubilee Palace (entry ₹25, looks like Buckingham Palace). "
                    "2. Madan Mohan Bari where traditional evening aarti is majestic. "
                    "3. Sagardighi royal lake promenade. "
                    "Make sure to stop at New Cinema More for authentic Rajbanshi Chire-Doi and warm Pantua sweets for just ₹40!"
                ),
                total_expense=540.0,
                expense_breakdown="Toto reserved whole day: ₹350 | Palace Entry: ₹25 | Authentic Bengali Fish Thali: ₹125 | Traditional Sweets: ₹40",
                weather_note="Pleasant golden sunshine, 25°C. Great for walking around lakes.",
                image_url="/assets/NB-5.jpeg",
                likes_count=42,
                created_at=datetime(2026, 11, 4, 14, 0)
            ),

            CommunityPost(
                author_name="David Miller",
                author_type="Tourist",
                author_location="Trekker from Edinburgh",
                destination_name="Buxa",
                title="Trekking to Buxa Fort - The Historic Detention Camp in the Jungle",
                post_type="Tourist Review",
                rating=4.8,
                content=(
                    "The hike up to Buxa Fort from Santalabari was one of the most poignant experiences of my travels in India. "
                    "Standing inside the stone prison cells where Indian freedom fighters were jailed by the British in the 1930s gives you chills. "
                    "The trail is 3 km through dense Himalayan foothills filled with butterflies and hornbills. "
                    "We hired an indigenous Rava guide named Subal from Santalabari village who told us unforgettable historical folklore. "
                    "Total cost for the entire day was under ₹1200!"
                ),
                total_expense=1180.0,
                expense_breakdown="Train from NJP to Alipurduar: ₹140 | Shared jeep to Santalabari: ₹60 | Forest permit & guide fee: ₹280 | Village lunch: ₹100 | Night homestay: ₹600",
                weather_note="Warm afternoon (25°C), cool evening breeze (17°C).",
                image_url="/assets/buxa.jpeg",
                likes_count=29,
                created_at=datetime(2026, 11, 5, 16, 20)
            ),

            CommunityPost(
                author_name="Dechen Bhutia",
                author_type="Local Resident",
                author_location="Mirik Homestay Host",
                destination_name="Mirik",
                title="Morning Lake Walk, Thurbo Tea Garden Sunrise & Authentic Tingling View",
                post_type="Local Suggestion",
                rating=4.9,
                content=(
                    "Tip from a Mirik local: Never visit on Sunday afternoons when noisy crowds arrive from Siliguri. "
                    "Come on a weekday morning! Take the early 7 AM NBSTC bus from Tenzing Norgay bus stand in Siliguri for just ₹90. "
                    "Walk across the Indreni bridge around Sumendu lake when the morning mist rolls over the pine trees. "
                    "Then take a ₹20 shared cab up to Tingling View Point for a 360-degree view of the emerald Thurbo tea gardens with Kanchenjunga standing tall behind."
                ),
                total_expense=340.0,
                expense_breakdown="NBSTC Bus fare: ₹90 | Shared cab to Tingling: ₹20 | Lake paddle boat: ₹100 | Steamed momos & ginger tea: ₹130",
                weather_note="Crisp 17°C mountain air. Perfect for morning photography.",
                image_url="/assets/mirik.jpeg",
                likes_count=33,
                created_at=datetime(2026, 11, 6, 8, 45)
            ),
        ]
        db.bulk_save_objects(posts)
        db.commit()
        print("Community posts seeded successfully.")

        # Seed comments on the first post
        post1 = db.query(CommunityPost).first()
        if post1:
            comments = [
                CommunityComment(
                    post_id=post1.id,
                    author_name="Rahul Mukherjee",
                    author_type="Tourist",
                    content="Thanks Passang! Can we get a shared jeep to Takdah after 3 PM from Siliguri Junction, or should we reach earlier?",
                    created_at=datetime(2026, 11, 2, 11, 0)
                ),
                CommunityComment(
                    post_id=post1.id,
                    author_name="Passang Tamang",
                    author_type="Local Resident",
                    content="Hello Rahul! Shared jeeps to Takdah usually leave between 7:30 AM and 1:30 PM. If you arrive after 2 PM, take a Darjeeling-bound jeep to Jorebungalow (₹250), and from there take a local taxi to Takdah for ₹200.",
                    created_at=datetime(2026, 11, 2, 11, 25)
                ),
            ]
            db.bulk_save_objects(comments)
            db.commit()
            print("Community comments seeded successfully.")

except Exception as err:
    db.rollback()
    print("Error during seed:", err)
finally:
    db.close()
