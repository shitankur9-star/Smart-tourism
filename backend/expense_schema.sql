-- =========================================================
-- BENGALTRAIL TOURISM - TRAVELER EXPENSE DATABASE SCHEMA
-- North Bengal Tourism Expense Management System
-- Supports: Bus, Train, Toto (E-rickshaw), Food, Homestay,
-- Shared Jeep, Activities, Sightseeing, and Permits
-- =========================================================

CREATE DATABASE IF NOT EXISTS bengaltrail;
USE bengaltrail;

-- ---------------------------------------------------------
-- 1. EXPENSE CATEGORIES TABLE
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS expense_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,          -- 'Transport', 'Homestay / Accommodation', 'Food & Dining', 'Activities', 'Permits', 'Misc'
    icon VARCHAR(50) DEFAULT 'ri-money-dollar-circle-line',
    description VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------
-- 2. STANDARD RATE CARD / BENCHMARK EXPENSES TABLE
-- (Pre-populated reference rates for North Bengal travelers)
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS standard_rates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,          -- e.g. 'Darjeeling', 'Kalimpong', 'Mirik', 'Chatakpur', 'Lataguri'
    expense_type VARCHAR(50) NOT NULL,          -- 'Bus', 'Train', 'Toto', 'Shared Jeep', 'Food', 'Homestay'
    route_or_service VARCHAR(200) NOT NULL,     -- e.g. 'Siliguri to Darjeeling Shared Jeep', 'Siliguri Town Toto Ride'
    estimated_cost DECIMAL(10, 2) NOT NULL,    -- in INR (₹)
    cost_unit VARCHAR(50) DEFAULT 'per person', -- 'per person', 'per night', 'per ride', 'per meal'
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------
-- 3. TRAVELER LOGGED EXPENSES TABLE
-- (Tracks every expense spent by a traveler during their trip)
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS traveler_expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,                           -- Foreign key to users table (if authenticated)
    trip_id INT NULL,                           -- Foreign key to trips table (optional)
    destination_name VARCHAR(100) NOT NULL,     -- e.g. 'Darjeeling', 'Takdah', 'Lamahatta'
    
    -- Expense Details
    category VARCHAR(50) NOT NULL,              -- 'Transport', 'Accommodation', 'Food', 'Activities', 'Permits', 'Miscellaneous'
    sub_category VARCHAR(50) NOT NULL,          -- 'Bus', 'Train', 'Toto', 'Shared Jeep', 'Homestay', 'Hotel', 'Food', 'Safari', etc.
    item_title VARCHAR(200) NOT NULL,           -- Description: 'Toto from NJP station to Junction', 'Homestay in Takdah 2 nights'
    
    amount DECIMAL(10, 2) NOT NULL,            -- Cost in INR (₹)
    payment_method ENUM('Cash', 'UPI / GPay / PhonePe', 'Card', 'Net Banking') DEFAULT 'UPI / GPay / PhonePe',
    
    -- Transit specifics (for Bus/Train/Toto/Jeep)
    origin_point VARCHAR(150) NULL,             -- e.g. 'NJP Station'
    destination_point VARCHAR(150) NULL,        -- e.g. 'Darjeeling Mall'
    
    expense_date DATE NOT NULL,                 -- Date expense was incurred
    expense_time TIME NULL,                     -- Time of expense
    
    number_of_people INT DEFAULT 1,             -- Number of travelers split/covered
    notes TEXT NULL,                            -- Traveler notes: 'Driver contact: 98xxxx, very helpful'
    receipt_image_url VARCHAR(500) NULL,        -- Photo/URL of receipt or ticket
    
    is_estimated BOOLEAN DEFAULT FALSE,         -- TRUE if planned budget, FALSE if actual spent
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------
-- INDEXES FOR FAST QUERYING & REPORTING
-- ---------------------------------------------------------
CREATE INDEX idx_traveler_expenses_user ON traveler_expenses(user_id);
CREATE INDEX idx_traveler_expenses_date ON traveler_expenses(expense_date);
CREATE INDEX idx_traveler_expenses_category ON traveler_expenses(category);
CREATE INDEX idx_traveler_expenses_subcategory ON traveler_expenses(sub_category);


-- =========================================================
-- INITIAL SEED DATA: CATEGORIES
-- =========================================================
INSERT IGNORE INTO expense_categories (id, name, icon, description) VALUES
(1, 'Transport', 'ri-bus-line', 'Bus, Train, Toto, Shared Jeep, and Private Cabs'),
(2, 'Homestay & Lodging', 'ri-home-4-line', 'Homestays, Eco-resorts, and Hotels'),
(3, 'Food & Dining', 'ri-restaurant-2-line', 'Meals, snacks, local food, cafe, and tea'),
(4, 'Sightseeing & Safari', 'ri-compass-3-line', 'Entry fees, national park jeep safaris, ropeway, viewpoint tickets'),
(5, 'Permits & Guides', 'ri-file-shield-line', 'Singalila park permit, local guide charges, border clearance'),
(6, 'Miscellaneous', 'ri-shopping-bag-3-line', 'Souvenirs, Darjeeling tea packets, tips, emergency medicine');


-- =========================================================
-- INITIAL SEED DATA: NORTH BENGAL BENCHMARK RATES
-- (Real-world rates for reference & automated cost estimation)
-- =========================================================
INSERT INTO standard_rates (destination, expense_type, route_or_service, estimated_cost, cost_unit, notes) VALUES
-- TOTO (E-Rickshaw) Rates
('Siliguri', 'Toto', 'NJP Railway Station to Siliguri Town / Junction', 120.00, 'per ride (reserve)', 'Shared toto is ₹20-₹25 per person'),
('Siliguri', 'Toto', 'Siliguri Junction to Court More / Hong Kong Market', 20.00, 'per person', 'Shared toto rate within town'),
('Cooch Behar', 'Toto', 'Cooch Behar Railway Station to Cooch Behar Palace', 100.00, 'per ride (reserve)', 'Shared toto is ₹15-₹20 per seat'),
('Alipurduar', 'Toto', 'New Alipurduar Junction to Bus Stand / Town', 15.00, 'per person', 'Standard shared fare'),
('Malbazar', 'Toto', 'Malbazar Station to Dooars Bus Stand', 30.00, 'per ride', 'Local short transit'),

-- BUS Rates (NBSTC / Private)
('Darjeeling', 'Bus', 'Siliguri (Tenzing Norgay Bus Stand) to Darjeeling', 120.00, 'per person', 'NBSTC Government Bus, duration ~3.5-4 hrs'),
('Kalimpong', 'Bus', 'Siliguri to Kalimpong via Teesta Bazar', 110.00, 'per person', 'NBSTC / Private Bus, duration ~3 hrs'),
('Mirik', 'Bus', 'Siliguri to Mirik Lake', 90.00, 'per person', 'Local bus route through tea gardens'),
('Jaldapara', 'Bus', 'Siliguri to Madarihat (Jaldapara Sanctuary)', 160.00, 'per person', 'Regular NBSTC Dooars service'),
('Alipurduar', 'Bus', 'Siliguri to Alipurduar Junction', 190.00, 'per person', 'Express NBSTC bus'),

-- TRAIN Rates
('Darjeeling', 'Train', 'DHR Toy Train Joyride (Darjeeling to Ghum & back, Steam engine)', 1500.00, 'per person', 'Heritage Toy Train, diesel engine is ~₹1000'),
('Darjeeling', 'Train', 'DHR Toy Train Regular (NJP to Darjeeling full route)', 1420.00, 'per person', 'Scenic mountain railway, takes ~7 hrs'),
('Dooars', 'Train', 'Vistadome Express (NJP to Alipurduar via Sevoke & Dooars forest)', 770.00, 'per person', 'Scenic glass dome coach through Mahananda & Buxa forests'),

-- SHARED JEEP / TAXI Rates
('Darjeeling', 'Shared Jeep', 'Siliguri (Junction Jeep Stand) to Darjeeling Clubside', 300.00, 'per person', 'Bolero/Sumo shared seat. Reserved taxi is ₹2800-₹3500'),
('Kalimpong', 'Shared Jeep', 'Siliguri Junction to Kalimpong Jeep Stand', 250.00, 'per person', 'Shared seat. Reserved is ~₹2500'),
('Kurseong', 'Shared Jeep', 'Siliguri to Kurseong Tourist Hub', 180.00, 'per person', 'Shared vehicle'),
('Gangtok', 'Shared Jeep', 'Siliguri (SNT Bus Stand) to Gangtok Deorali', 400.00, 'per person', 'Shared seat'),

-- HOMESTAYS (Per person per night with 3-4 meals included)
('Chatakpur', 'Homestay', 'Village Eco-Homestay with organic meals (Breakfast + Lunch + Dinner)', 1500.00, 'per person/night', 'Includes warm hospitality, traditional food, and Kanchenjunga view'),
('Takdah', 'Homestay', 'Colonial Tea Heritage Homestay with all meals', 1400.00, 'per person/night', 'Quiet tea garden village stay with authentic local Nepali dishes'),
('Lamahatta', 'Homestay', 'Pine Forest Village Homestay with meals', 1300.00, 'per person/night', 'Located walking distance from Lamahatta Eco Park'),
('Sittong', 'Homestay', 'Orange Valley Homestay (Sittong / Ahaldara)', 1200.00, 'per person/night', 'Famous for orange orchards and organic meals'),
('Lepchajagat', 'Homestay', 'Pine Ridge Homestay with meal package', 1400.00, 'per person/night', 'Silent pine forest stay near Ghoom'),
('Rishyap', 'Homestay', 'Lava-Rishyap Himalayan View Homestay', 1300.00, 'per person/night', 'Scenic mountain view'),

-- FOOD & DINING
('Darjeeling', 'Food', 'Darjeeling Momos (Steamed Veg/Chicken, 8 pcs)', 100.00, 'per plate', 'Famous Mall Road / Kunga / roadside rate: ₹80-₹120'),
('Darjeeling', 'Food', 'Thukpa (Tibetan Noodle Soup)', 120.00, 'per bowl', 'Hot local noodle soup with fresh broth'),
('Siliguri', 'Food', 'Authentic Bengali Fish / Thali Lunch', 180.00, 'per thali', 'Steamed rice, dal, sabzi, fish curry, chutney, papad'),
('Darjeeling', 'Food', 'English Breakfast / Coffee & Pastry at Glenary\'s', 350.00, 'per person', 'Classic heritage cafe at Nehru Road');


-- =========================================================
-- SAMPLE TRAVELER EXPENSES
-- (Demonstrates what logged traveler data looks like)
-- =========================================================
INSERT INTO traveler_expenses 
(user_id, destination_name, category, sub_category, item_title, amount, payment_method, origin_point, destination_point, expense_date, expense_time, number_of_people, notes) 
VALUES
(NULL, 'Siliguri', 'Transport', 'Toto', 'Toto from NJP station gate to Siliguri Junction Jeep Stand', 120.00, 'Cash', 'NJP Railway Station', 'Siliguri Junction', '2026-11-01', '08:30:00', 2, 'Reserved toto for 2 luggage bags'),
(NULL, 'Darjeeling', 'Transport', 'Shared Jeep', 'Shared Bolero jeep from Siliguri Junction to Darjeeling Clubside', 600.00, 'Cash', 'Siliguri Junction', 'Darjeeling Clubside', '2026-11-01', '09:15:00', 2, '₹300 per seat x 2 passengers'),
(NULL, 'Darjeeling', 'Food & Dining', 'Food', 'Hot Chicken Momos and Darjeeling First Flush Tea at Mall Road', 240.00, 'UPI / GPay / PhonePe', 'Mall Road', 'Mall Road', '2026-11-01', '14:00:00', 2, 'Delicious local lunch'),
(NULL, 'Takdah', 'Homestay & Lodging', 'Homestay', 'Takdah Heritage Homestay (Night 1) with Dinner & Breakfast', 2800.00, 'UPI / GPay / PhonePe', 'Takdah Cantonment', 'Takdah Cantonment', '2026-11-01', '19:30:00', 2, '₹1400 per person including organic homemade meals'),
(NULL, 'Darjeeling', 'Transport', 'Train', 'DHR Himalayan Toy Train Steam Joyride (Ghum Safari)', 3000.00, 'Card', 'Darjeeling Station', 'Ghum Station', '2026-11-02', '10:00:00', 2, 'Heritage steam joyride booking tickets'),
(NULL, 'Darjeeling', 'Transport', 'Bus', 'NBSTC Local Bus from Ghoom to Kurseong', 70.00, 'Cash', 'Ghoom', 'Kurseong', '2026-11-02', '15:30:00', 2, '₹35 per ticket x 2');
