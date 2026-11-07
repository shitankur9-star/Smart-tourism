const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");
const navItems = document.querySelectorAll(".nav-link");


// Mobile menu

if (menuBtn && navLinks) {

    menuBtn.addEventListener("click", () => {

        navLinks.classList.toggle("show");

        const icon =
            menuBtn.querySelector("i");


        if (!icon) {
            return;
        }


        if (
            navLinks.classList.contains("show")
        ) {

            icon.classList.remove(
                "fa-bars"
            );

            icon.classList.add(
                "fa-xmark"
            );

        } else {

            icon.classList.remove(
                "fa-xmark"
            );

            icon.classList.add(
                "fa-bars"
            );

        }

    });

}


// Active navigation

navItems.forEach(item => {

    item.addEventListener("click", () => {

        navItems.forEach(nav => {
            nav.classList.remove("active");
        });

        item.classList.add("active");

        // Close mobile menu

        navLinks.classList.remove("show");

        const icon = menuBtn.querySelector("i");

        icon.classList.remove("fa-xmark");
        icon.classList.add("fa-bars");

    });

});


// Navbar scroll effect

window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {

        navbar.style.background = "rgba(10, 20, 30, 0.65)";

        navbar.style.boxShadow =
            "0 10px 40px rgba(0,0,0,0.35)";

    } else {

        navbar.style.background =
            "rgba(255,255,255,0.08)";

        navbar.style.boxShadow =
            "0 8px 32px rgba(0,0,0,0.25)";
    }

});

// Backend API call to fetch the data from the database and display it on the frontend

function initializeTripModal() {
    const viewDetailsBtns = document.querySelectorAll(".view-details");
    const tripModal = document.getElementById("tripModal");
    const closeModal = document.getElementById("closeModal");
    const modalImage = document.getElementById("modalImage");

    if (modalImage) {
        modalImage.addEventListener("error", () => {
            modalImage.src = "assets/img1.jpeg";
        });
    }

    const API_BASE_URL = getApiBaseUrl();

    viewDetailsBtns.forEach(button => {
        button.addEventListener("click", async () => {
            const tripId = button.dataset.tripId || "1";
            const url = `${API_BASE_URL}/api/trips/${tripId}`;

            try {
                console.log("Fetching trip details from", url);
                const response = await fetch(url, {
                    method: "GET",
                    mode: "cors"
                });

                if (!response.ok) {
                    const body = await response.text();
                    throw new Error(`Unable to fetch trip details (${response.status}) - ${body}`);
                }

                const trip = await response.json();
                openTripModal(trip);
            } catch (error) {
                console.error("Trip fetch failed:", error);
                alert(
                    `Unable to load trip details. Backend must be running on ${API_BASE_URL}.\n
Error: ${error.message}`
                );
            }
        });
    });

    if (closeModal) {
        closeModal.addEventListener("click", () => {
            closeTripModal(tripModal);
        });
    }

    if (tripModal) {
        tripModal.addEventListener("click", event => {
            if (event.target === tripModal) {
                closeTripModal(tripModal);
            }
        });
    }

    document.addEventListener("keydown", event => {
        if (event.key === "Escape" && tripModal && tripModal.classList.contains("active")) {
            closeTripModal(tripModal);
        }
    });
}

function closeTripModal(tripModal) {
    if (tripModal) {
        tripModal.classList.remove("active");
    }
}

initializeTripModal();

// Create the modal dynamically

// Instead of hardcoding the modal information, JavaScript will receive it from MySQL.
let currentTripId = null;

function openTripModal(trip) {

    // document.getElementById("modalTitle").textContent =
    //     trip.title;
    // Save the currently opened trip ID
    currentTripId = trip.id;

    console.log("Current trip ID:", currentTripId);

    document.getElementById("modalTitle").textContent =
        trip.title;


    document.getElementById("modalCategory").textContent =
        trip.category;


    document.getElementById("modalRoute").textContent =
        trip.route;


    document.getElementById("modalRating").textContent =
        `⭐ ${trip.rating}/5 (${trip.reviews} reviews)`;


    document.getElementById("modalPrice").textContent =
        `₹${trip.price}`;


    document.getElementById("modalDuration").textContent =
        trip.duration;


    document.getElementById("modalDifficulty").textContent =
        trip.difficulty;


    document.getElementById("modalDescription").textContent =
        trip.description;

    const imageSrc = getTripImage(trip);
    document.getElementById("modalImage").src = imageSrc;

    document.getElementById("modalAI").textContent =
        `${trip.ai_match}% AI Match`;


    document.getElementById("modalRecommended").textContent =
        trip.recommended_for;


    // Create tags

    const tagsContainer =
        document.getElementById("modalTags");


    tagsContainer.innerHTML = "";


    const tags = trip.tags.split(",");


    tags.forEach(tag => {

        const span = document.createElement("span");

        span.className = "tag";

        span.textContent = tag.trim();

        tagsContainer.appendChild(span);

    });


    document
        .getElementById("tripModal")
        .classList.add("active");
}

// ======================================================
// MODAL BOOK NOW
// ======================================================

const modalBookNowBtn =
    document.getElementById("modalBookNowBtn");

if (modalBookNowBtn) {

    modalBookNowBtn.addEventListener(
        "click",
        function () {

            if (!currentTripId) {

                console.error(
                    "Current trip ID is missing."
                );

                return;
            }

            console.log(
                "Opening hotels for trip:",
                currentTripId
            );

            window.location.href =
                `hotels.html?trip_id=${currentTripId}`;

        }
    );
}

// const FALLBACK_API_URL = "http://127.0.0.1:8000";

// const API_URL = window.location.protocol.startsWith("http")
//     ? `${window.location.protocol}//${window.location.hostname}${window.location.port ? ":" + window.location.port : ""}`
//     : FALLBACK_API_URL;

// const FRONTEND_BASE_URL = `${API_URL}/frontend`;

function getApiBaseUrl() {
    const origin = window.location.origin;
    return origin && origin !== "null" ? origin : "http://127.0.0.1:8000";
}

const API_URL = getApiBaseUrl();

// const FRONTEND_BASE_URL = `${API_URL}/frontend`;
const FRONTEND_BASE_URL =
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
        ? "/frontend"
        : "";

// Add click event listener to the "HOME" button //
const homeLink = document.getElementById("home");

if (homeLink) {
  homeLink.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = `${FRONTEND_BASE_URL}/mainpage.html`;
  });
}

// ==========================================
// TRIPS PAGE PROFILE BUTTON
// ==========================================

const tripProfileBtn =
    document.getElementById("tripProfileBtn");


if (tripProfileBtn) {

    tripProfileBtn.addEventListener(
        "click",
        async function () {

            // Get saved login token
            const token =
                localStorage.getItem(
                    "bengaltrail_token"
                );


            // ==================================
            // USER NOT LOGGED IN
            // ==================================

            if (!token) {

                window.location.href =
                    `${FRONTEND_BASE_URL}/auth.html`;

                return;
            }


            // ==================================
            // CHECK TOKEN WITH BACKEND
            // ==================================

            try {

                const response =
                    await fetch(
                        "http://127.0.0.1:8000/api/check-auth",
                        {
                            method: "GET",

                            headers: {
                                "Authorization":
                                    `Bearer ${token}`
                            }
                        }
                    );


                // ==================================
                // USER IS LOGGED IN
                // ==================================

                if (response.ok) {

                    window.location.href =
                        `${FRONTEND_BASE_URL}/profile.html`;

                    return;
                }


                // ==================================
                // TOKEN IS INVALID
                // ==================================

                localStorage.removeItem(
                    "bengaltrail_token"
                );

                window.location.href =
                    `${FRONTEND_BASE_URL}/auth.html`;


            } catch (error) {

                console.error(
                    "Authentication error:",
                    error
                );

            }

        }
    );

}

// ======================================================
// BENGALTRAIL - DYNAMIC TRIP CARDS
// ======================================================

const DYNAMIC_TRIPS_API =
    "http://127.0.0.1:8000/api/trips";

let allDynamicTrips = [];

// ------------------------------------------------------
// START
// ------------------------------------------------------

function startDynamicTrips() {

    const container =
        document.getElementById(
            "dynamicTripsContainer"
        );


    if (!container) {

        console.log(
            "Dynamic trips container not found."
        );

        return;
    }


    loadDynamicTrips();

}



// ------------------------------------------------------
// LOAD TRIPS FROM FASTAPI
// ------------------------------------------------------

async function loadDynamicTrips() {

    const container =
        document.getElementById(
            "dynamicTripsContainer"
        );


    if (!container) {
        return;
    }


    console.log(
        "Loading dynamic trips..."
    );


    try {

        const response =
            await fetch(
                DYNAMIC_TRIPS_API,
                {
                    method: "GET"
                }
            );


        console.log(
            "Trips API status:",
            response.status
        );


        if (!response.ok) {

            throw new Error(
                `Trips API returned ${response.status}`
            );

        }


        const trips =
            await response.json();


        console.log(
            "Trips received:",
            trips
        );


        if (
            !Array.isArray(trips)
        ) {

            throw new Error(
                "Invalid trips response"
            );

        }


        // ==========================================
        // SAVE ALL TRIPS FOR SEARCH
        // ==========================================

        allDynamicTrips =
            trips;


        // ==========================================
        // DISPLAY ALL TRIPS
        // ==========================================

        renderDynamicTrips(
            trips
        );


    } catch (error) {

        console.error(
            "Dynamic trips error:",
            error
        );


        container.innerHTML = `

            <div class="dynamic-trips-empty">

                <i
                    class="fa-solid fa-triangle-exclamation"
                ></i>

                <h3>
                    Unable to load destinations
                </h3>

                <p>
                    ${error.message}
                </p>

            </div>

        `;

    }

}



// ------------------------------------------------------
// CREATE DYNAMIC CARDS
// ------------------------------------------------------



function renderDynamicTrips(trips) {

    const container =
        document.getElementById(
            "dynamicTripsContainer"
        );


    if (!container) {
        return;
    }


    // Remove loading message

    container.innerHTML = "";


    // No database trips

    if (!trips || trips.length === 0) {

        container.innerHTML = `

            <div class="dynamic-trips-empty">

                <i
                    class="fa-solid fa-map-location-dot"
                ></i>

                <h3>
                    No additional destinations
                </h3>

                <p>
                    More destinations will be
                    available soon.
                </p>

            </div>

        `;

        return;
    }


    // --------------------------------------------------
    // CREATE CARDS
    // --------------------------------------------------

    trips.forEach(
        (trip) => {

            const card =
                document.createElement(
                    "article"
                );


            card.className =
                "dynamic-trip-card";


            // ------------------------------------------
            // IMAGE
            // ------------------------------------------

            const image =
                getTripImage(
                    trip
                );


            // ------------------------------------------
            // TAGS
            // ------------------------------------------

            const tags =
                getTripTags(
                    trip.tags
                );


            // ------------------------------------------
            // CARD HTML
            // ------------------------------------------

            card.innerHTML = `

                <div
                    class="dynamic-trip-image"
                >

                    <img
                        src="${image}"
                        alt="${
                            trip.title ||
                            "BengalTrail destination"
                        }"
                        loading="lazy"
                        onerror="
                            this.onerror = null;
                            this.src = 'assets/img1.jpeg';
                        "
                    >

                </div>


                <div
                    class="dynamic-trip-content"
                >

                    <span
                        class="dynamic-trip-category"
                    >

                        ${
                            trip.category ||
                            "Travel"
                        }

                    </span>


                    <h3>

                        ${
                            trip.title ||
                            "Untitled Trip"
                        }

                    </h3>


                    <p
                        class="dynamic-trip-route"
                    >

                        ${
                            trip.route ||
                            "Explore Bengal"
                        }

                    </p>


                    <div
                        class="dynamic-trip-info"
                    >

                        <span>
                            ⭐ ${
                                trip.rating ??
                                "N/A"
                            }
                        </span>


                        <span>
                            ₹${
                                trip.price ??
                                "N/A"
                            }
                        </span>


                        <span>
                            ${
                                trip.duration ||
                                "N/A"
                            }
                        </span>

                    </div>


                    <p
                        class="dynamic-trip-description"
                    >

                        ${
                            trip.description ||
                            "Discover this beautiful destination in Bengal."
                        }

                    </p>


                    <div
                        class="dynamic-trip-tags"
                    >

                        ${
                            tags.map(
                                tag => `

                                    <span>
                                        ${tag}
                                    </span>

                                `
                            ).join("")
                        }

                    </div>


                    <button
                        type="button"
                        class="dynamic-view-details"
                        data-trip-id="${trip.id}"
                    >

                        View Details

                    </button>

                </div>

            `;


            // Add card to container

            container.appendChild(
                card
            );

        }
    );


    console.log(
        `Created ${trips.length} dynamic trip cards.`
    );

}



// ------------------------------------------------------
// GET IMAGE
// ------------------------------------------------------

function getTripImage(trip) {

    const fallbackImage = "assets/img1.jpeg";

    if (!trip) {
        return fallbackImage;
    }

    const rawImage = 
        trip.image ||
        trip.cover_image ||
        trip.thumbnail ||
        "";

    if (!rawImage) {
        return fallbackImage;
    }

    if (
        rawImage.startsWith("http://") ||
        rawImage.startsWith("https://") ||
        rawImage.startsWith("data:")
    ) {
        return rawImage;
    }

    if (
        rawImage.startsWith("/uploads/") ||
        rawImage.startsWith("uploads/")
    ) {
        return rawImage.startsWith("/")
            ? rawImage
            : `/${rawImage}`;
    }

    if (
        rawImage.startsWith("/assets/") ||
        rawImage.startsWith("assets/")
    ) {
        return rawImage.startsWith("/")
            ? rawImage.replace(/^\/+/, "")
            : rawImage;
    }

    if (
        rawImage.startsWith("/frontend/") ||
        rawImage.startsWith("frontend/")
    ) {
        return rawImage.startsWith("/")
            ? rawImage.replace(/^\/frontend\//, "frontend/")
            : rawImage.replace(/^frontend\//, "frontend/");
    }

    return rawImage;

}



// ------------------------------------------------------
// GET TAGS
// ------------------------------------------------------

function getTripTags(tags) {

    if (!tags) {

        return [
            "Travel"
        ];

    }


    if (
        Array.isArray(tags)
    ) {

        return tags;

    }


    return String(tags)
        .split(",")
        .map(
            tag =>
                tag.trim()
        )
        .filter(Boolean);

}



// ------------------------------------------------------
// DYNAMIC CARD VIEW DETAILS
// ------------------------------------------------------

document.addEventListener(
    "click",
    async function (event) {

        const button =
            event.target.closest(
                ".dynamic-view-details"
            );


        if (!button) {
            return;
        }


        const tripId =
            button.dataset.tripId;


        if (!tripId) {
            return;
        }


        try {

            console.log(
                "Loading trip:",
                tripId
            );


            const response =
                await fetch(
                    `http://127.0.0.1:8000/api/trips/${tripId}`
                );


            if (!response.ok) {

                throw new Error(
                    `Trip request failed: ${response.status}`
                );

            }


            const trip =
                await response.json();


            openTripModal(
                trip
            );


        } catch (error) {

            console.error(
                "Trip details error:",
                error
            );


            alert(
                "Unable to load trip details."
            );

        }

    }
);



// ------------------------------------------------------
// START AFTER HTML LOADS
// ------------------------------------------------------

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "BengalTrail trip page loaded."
        );


        startDynamicTrips();

    }
);

// ======================================================
// TRIP SEARCH
// ======================================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const searchInput =
            document.getElementById(
                "tripSearchInput"
            );


        const searchButton =
            document.getElementById(
                "tripSearchBtn"
            );


        if (
            !searchInput ||
            !searchButton
        ) {

            return;

        }


        // Search button

        searchButton.addEventListener(
            "click",
            function () {

                performTripSearch(
                    searchInput.value
                );

            }
        );


        // Search when pressing Enter

        searchInput.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key === "Enter"
                ) {

                    performTripSearch(
                        searchInput.value
                    );

                }

            }
        );

    }
);

function performTripSearch(searchTerm) {

    const search =
        String(searchTerm || "")
            .trim()
            .toLowerCase();


    console.log(
        "Searching for:",
        search
    );


    console.log(
        "Available trips:",
        allDynamicTrips
    );


    // ==========================================
    // EMPTY SEARCH
    // ==========================================

    if (!search) {

        renderDynamicTrips(
            allDynamicTrips
        );

        return;

    }


    // ==========================================
    // FILTER TRIPS
    // ==========================================

    const filteredTrips =
        allDynamicTrips.filter(
            function (trip) {

                const searchableText = [

                    trip.title,

                    trip.category,

                    trip.route,

                    trip.description,

                    trip.tags,

                    trip.recommended_for,

                    trip.duration,

                    trip.difficulty,

                    trip.price

                ]
                    .filter(
                        value =>
                            value !== null &&
                            value !== undefined
                    )
                    .join(" ")
                    .toLowerCase();


                return searchableText.includes(
                    search
                );

            }
        );


    console.log(
        "Matching trips:",
        filteredTrips
    );


    // ==========================================
    // DISPLAY RESULTS
    // ==========================================

    renderDynamicTrips(
        filteredTrips
    );

}

