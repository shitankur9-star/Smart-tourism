-- =========================================================
-- BENGALTRAIL TOURISM - COMMUNITY, PLACE HISTORY & WEATHER SCHEMA
-- North Bengal Tourism Community Platform
-- Supports:
-- 1. Tourist reviews, ratings, and real expense breakdowns
-- 2. Local suggestions, hidden gems, and local travel tips
-- 3. Live destination weather, temperature & seasonal advice
-- 4. Full authentic history, etymology & landmarks of North Bengal
-- =========================================================

USE bengaltrail;

-- ---------------------------------------------------------
-- 1. PLACE HISTORIES & WEATHER TABLE
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS place_histories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(150) NOT NULL UNIQUE,
    district VARCHAR(100) NULL,
    tagline VARCHAR(250) NULL,
    name_etymology TEXT NULL,
    history_full TEXT NOT NULL,
    colonial_era TEXT NULL,
    cultural_heritage TEXT NULL,
    historical_landmarks TEXT NULL,
    current_weather VARCHAR(100) NULL,
    temperature_range VARCHAR(50) NULL,
    weather_condition VARCHAR(100) NULL,
    best_season_to_visit VARCHAR(200) NULL,
    altitude VARCHAR(100) NULL,
    local_transport_guide TEXT NULL,
    image_url VARCHAR(500) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------
-- 2. COMMUNITY POSTS (TOURIST REVIEWS & LOCAL SUGGESTIONS)
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS community_posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    author_name VARCHAR(120) NOT NULL,
    author_type ENUM('Tourist', 'Local Resident') DEFAULT 'Tourist',
    author_location VARCHAR(120) NULL,
    destination_name VARCHAR(150) NOT NULL,
    title VARCHAR(250) NOT NULL,
    post_type ENUM('Tourist Review', 'Local Suggestion', 'Hidden Gem', 'Budget Tip') DEFAULT 'Tourist Review',
    rating FLOAT DEFAULT 5.0,
    content TEXT NOT NULL,
    total_expense DECIMAL(10, 2) DEFAULT 0.00,
    expense_breakdown VARCHAR(500) NULL,
    weather_note VARCHAR(200) NULL,
    image_url VARCHAR(500) NULL,
    likes_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------
-- 3. COMMUNITY COMMENTS (DISCUSSIONS BETWEEN TOURISTS & LOCALS)
-- ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS community_comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    author_name VARCHAR(120) NOT NULL,
    author_type ENUM('Tourist', 'Local Resident') DEFAULT 'Tourist',
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES community_posts(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- INDEXES
CREATE INDEX idx_community_dest ON community_posts(destination_name);
CREATE INDEX idx_community_author_type ON community_posts(author_type);
CREATE INDEX idx_community_post_type ON community_posts(post_type);
