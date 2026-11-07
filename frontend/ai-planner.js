function getImageSource(imageValue) {
    if (!imageValue) {
        return "assets/img1.jpeg";
    }

    if (
        imageValue.startsWith("http://") ||
        imageValue.startsWith("https://") ||
        imageValue.startsWith("data:")
    ) {
        return imageValue;
    }

    if (
        imageValue.startsWith("/assets/") ||
        imageValue.startsWith("assets/") ||
        imageValue.startsWith("/uploads/") ||
        imageValue.startsWith("uploads/")
    ) {
        return imageValue.startsWith("/")
            ? imageValue
            : `/${imageValue}`;
    }

    return imageValue;
}

// const API_URL =
//     "http://127.0.0.1:8000";


// const form =
//     document.getElementById(
//         "aiPlannerForm"
//     );


// const loading =
//     document.getElementById(
//         "loading"
//     );


// const resultsSection =
//     document.getElementById(
//         "resultsSection"
//     );


// const resultsContainer =
//     document.getElementById(
//         "resultsContainer"
//     );


// const generateBtn =
//     document.getElementById(
//         "generateBtn"
//     );



// form.addEventListener(
//     "submit",
//     async function (event) {

//         event.preventDefault();


//         // =========================================
//         // GET USER INPUT
//         // =========================================

//         const startingLocation =
//             document.getElementById(
//                 "startingLocation"
//             ).value.trim();


//         const travelDate =
//             document.getElementById(
//                 "travelDate"
//             ).value;


//         const people =
//             Number(
//                 document.getElementById(
//                     "people"
//                 ).value
//             );


//         const budget =
//             Number(
//                 document.getElementById(
//                     "budget"
//                 ).value
//             );


//         const experience =
//             document.getElementById(
//                 "experience"
//             ).value;


//         const duration =
//             Number(
//                 document.getElementById(
//                     "duration"
//                 ).value
//             );


//         const transport =
//             document.getElementById(
//                 "transport"
//             ).value;


//         const weatherPreference =
//             document.getElementById(
//                 "weatherPreference"
//             ).value;


//         const footfallPreference =
//             document.getElementById(
//                 "footfallPreference"
//             ).value;



//         // =========================================
//         // SHOW LOADING
//         // =========================================

//         loading.classList.remove(
//             "hidden"
//         );

//         resultsSection.classList.add(
//             "hidden"
//         );

//         resultsContainer.innerHTML = "";

//         generateBtn.disabled = true;



//         try {

//             // =========================================
//             // SEND TO FASTAPI
//             // =========================================

//             const response =
//                 await fetch(
//                     `${API_URL}/api/ai/plan`,
//                     {

//                         method: "POST",

//                         headers: {
//                             "Content-Type":
//                                 "application/json"
//                         },

//                         body:
//                             JSON.stringify({

//                                 starting_location:
//                                     startingLocation,

//                                 travel_date:
//                                     travelDate,

//                                 people:
//                                     people,

//                                 budget:
//                                     budget,

//                                 experience:
//                                     experience,

//                                 duration:
//                                     duration,

//                                 transport:
//                                     transport,

//                                 weather_preference:
//                                     weatherPreference,

//                                 footfall_preference:
//                                     footfallPreference

//                             })

//                     }
//                 );



//             const data =
//                 await response.json();


//             if (!response.ok) {

//                 throw new Error(
//                     data.detail ||
//                     "AI planner failed"
//                 );

//             }


//             // =========================================
//             // DISPLAY RESULTS
//             // =========================================

//             displayResults(
//                 data.recommendations
//             );


//         } catch (error) {

//             console.error(
//                 "AI planner error:",
//                 error
//             );


//             alert(
//                 error.message ||
//                 "Unable to generate recommendations."
//             );

//         } finally {

//             loading.classList.add(
//                 "hidden"
//             );

//             generateBtn.disabled =
//                 false;

//         }

//     }
// );



// // =========================================
// // DISPLAY RESULTS
// // =========================================

// function displayResults(
//     recommendations
// ) {

//     resultsContainer.innerHTML = "";


//     if (
//         !recommendations ||
//         recommendations.length === 0
//     ) {

//         resultsContainer.innerHTML = `

//             <p>
//                 No suitable destinations
//                 were found.
//             </p>

//         `;

//         resultsSection.classList.remove(
//             "hidden"
//         );

//         return;
//     }


//     recommendations.forEach(
//         (place, index) => {

//             const image =
//                 place.image ||
//                 "assets/img1.jpeg";


//             const card =
//                 document.createElement(
//                     "article"
//                 );


//             card.className =
//                 "result-card";


//             card.innerHTML = `

//                 <img
//                     class="result-image"
//                     src="${image}"
//                     alt="${place.destination}"
//                 >


//                 <div class="result-content">

//                     <span class="match">

//                         ${place.ai_match}% AI MATCH

//                     </span>


//                     <h3>
//                         ${index + 1}.
//                         ${place.destination}
//                     </h3>


//                     <p class="category">

//                         ${place.category}

//                     </p>


//                     <p class="result-description">

//                         ${place.description}

//                     </p>


//                     <div class="result-stats">


//                         <div class="stat">

//                             <small>
//                                 Estimated Budget
//                             </small>

//                             <strong>
//                                 ₹${Math.round(
//                                     place.estimated_budget
//                                 )}
//                             </strong>

//                         </div>


//                         <div class="stat">

//                             <small>
//                                 Rating
//                             </small>

//                             <strong>
//                                 ⭐ ${place.rating}
//                             </strong>

//                         </div>


//                         <div class="stat">

//                             <small>
//                                 Transport
//                             </small>

//                             <strong>
//                                 ${place.transport}
//                             </strong>

//                         </div>


//                         <div class="stat">

//                             <small>
//                                 Crowd
//                             </small>

//                             <strong>
//                                 ${place.crowd_level}
//                             </strong>

//                         </div>

                        



//                     </div>

//                     <button class="result-book-now-btn">
//                             Book Now
//                     </button>

//                 </div>

//             `;


//             resultsContainer.appendChild(
//                 card
//             );

//         }
//     );


//     resultsSection.classList.remove(
//         "hidden"
//     );


//     resultsSection.scrollIntoView({
//         behavior: "smooth"
//     });

// }

// ============================================================
// BENGALTRAIL - AI TRIP PLANNER
// ============================================================
//
// This file handles:
//
// 1. Starting-location verification
// 2. AI trip-plan generation
// 3. Displaying AI recommendations
// 4. Book Now button
// 5. Matching AI destination with database Trip
// 6. Checking hotels for the selected Trip
// 7. Opening hotels.html with the correct trip_id
//
// ============================================================


// ============================================================
// API
// ============================================================

const API_URL =
    "http://127.0.0.1:8000";


// ============================================================
// MAIN ELEMENTS
// ============================================================

const form =
    document.getElementById(
        "aiPlannerForm"
    );

const loading =
    document.getElementById(
        "loading"
    );

const resultsSection =
    document.getElementById(
        "resultsSection"
    );

const resultsContainer =
    document.getElementById(
        "resultsContainer"
    );

const generateBtn =
    document.getElementById(
        "generateBtn"
    );


// ============================================================
// LOCATION ELEMENTS
// ============================================================

const startingLocationInput =
    document.getElementById(
        "startingLocation"
    );

const verifyLocationBtn =
    document.getElementById(
        "verifyLocationBtn"
    );

const locationStatus =
    document.getElementById(
        "locationStatus"
    );

const locationResults =
    document.getElementById(
        "locationResults"
    );

const startingLatitude =
    document.getElementById(
        "startingLatitude"
    );

const startingLongitude =
    document.getElementById(
        "startingLongitude"
    );

const verifiedLocation =
    document.getElementById(
        "verifiedLocation"
    );


// ============================================================
// LOCATION STATE
// ============================================================

let selectedLocation = null;


// ============================================================
// BASIC ELEMENT CHECK
// ============================================================

if (!form) {
    console.error(
        "AI Planner Error: #aiPlannerForm was not found."
    );
}

if (!resultsContainer) {
    console.error(
        "AI Planner Error: #resultsContainer was not found."
    );
}


// ============================================================
// CLEAR VERIFIED LOCATION WHEN USER EDITS INPUT
// ============================================================

if (startingLocationInput) {

    startingLocationInput.addEventListener(
        "input",
        function () {

            selectedLocation = null;

            if (startingLatitude) {
                startingLatitude.value = "";
            }

            if (startingLongitude) {
                startingLongitude.value = "";
            }

            if (verifiedLocation) {
                verifiedLocation.value = "";
            }

            if (locationResults) {

                locationResults.innerHTML =
                    "";

                locationResults.classList.add(
                    "hidden"
                );
            }

            if (locationStatus) {

                locationStatus.textContent =
                    "Location changed. Please verify the new location.";

                locationStatus.className =
                    "location-status info";
            }
        }
    );
}


// ============================================================
// VERIFY LOCATION
// ============================================================

if (verifyLocationBtn) {

    verifyLocationBtn.addEventListener(
        "click",
        async function () {

            const query =
                startingLocationInput
                    ? startingLocationInput.value.trim()
                    : "";


            // ------------------------------------------------
            // BASIC VALIDATION
            // ------------------------------------------------

            if (query.length < 3) {

                if (locationStatus) {

                    locationStatus.textContent =
                        "Please enter at least 3 characters.";

                    locationStatus.className =
                        "location-status error";
                }

                return;
            }


            // ------------------------------------------------
            // LOADING
            // ------------------------------------------------

            verifyLocationBtn.disabled =
                true;


            if (locationStatus) {

                locationStatus.textContent =
                    "Checking location...";

                locationStatus.className =
                    "location-status info";
            }


            if (locationResults) {

                locationResults.innerHTML =
                    "";

                locationResults.classList.add(
                    "hidden"
                );
            }


            // ------------------------------------------------
            // API REQUEST
            // ------------------------------------------------

            try {

                const response =
                    await fetch(
                        `${API_URL}/api/location/search?q=${encodeURIComponent(query)}`
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Location could not be found."
                    );
                }


                // ------------------------------------------------
                // CHECK RESULTS
                // ------------------------------------------------

                if (
                    !data.results ||
                    data.results.length === 0
                ) {

                    throw new Error(
                        "No matching Indian location found."
                    );
                }


                // ------------------------------------------------
                // DISPLAY LOCATION OPTIONS
                // ------------------------------------------------

                if (locationResults) {

                    locationResults.innerHTML =
                        "";


                    data.results.forEach(
                        function (place) {

                            const option =
                                document.createElement(
                                    "button"
                                );


                            option.type =
                                "button";


                            option.className =
                                "location-option";


                            option.innerHTML = `
                                <strong>
                                    <i class="ri-map-pin-line"></i>
                                    Select this location
                                </strong>

                                <span>
                                    ${escapeHTML(
                                        place.display_name
                                    )}
                                </span>
                            `;


                            option.addEventListener(
                                "click",
                                function () {

                                    selectLocation(
                                        place
                                    );

                                }
                            );


                            locationResults.appendChild(
                                option
                            );

                        }
                    );


                    locationResults.classList.remove(
                        "hidden"
                    );
                }


                if (locationStatus) {

                    locationStatus.textContent =
                        "Select the exact place you mean:";

                    locationStatus.className =
                        "location-status info";
                }


            } catch (error) {

                console.error(
                    "Location verification error:",
                    error
                );


                if (locationStatus) {

                    locationStatus.textContent =
                        error.message ||
                        "Unable to verify location.";

                    locationStatus.className =
                        "location-status error";
                }

            } finally {

                verifyLocationBtn.disabled =
                    false;
            }

        }
    );
}


// ============================================================
// SELECT LOCATION
// ============================================================

function selectLocation(place) {

    selectedLocation =
        place;


    // --------------------------------------------------------
    // SAVE VERIFIED DATA
    // --------------------------------------------------------

    if (startingLocationInput) {

        startingLocationInput.value =
            place.display_name;
    }


    if (startingLatitude) {

        startingLatitude.value =
            place.latitude;
    }


    if (startingLongitude) {

        startingLongitude.value =
            place.longitude;
    }


    if (verifiedLocation) {

        verifiedLocation.value =
            place.display_name;
    }


    // --------------------------------------------------------
    // HIDE LOCATION OPTIONS
    // --------------------------------------------------------

    if (locationResults) {

        locationResults.innerHTML =
            "";

        locationResults.classList.add(
            "hidden"
        );
    }


    // --------------------------------------------------------
    // SUCCESS MESSAGE
    // --------------------------------------------------------

    if (locationStatus) {

        locationStatus.textContent =
            "✓ Location verified successfully.";

        locationStatus.className =
            "location-status success";
    }
}


// ============================================================
// FORM SUBMIT
// ============================================================

if (form) {

    form.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();


            // =================================================
            // LOCATION MUST BE VERIFIED
            // =================================================

            if (
                !selectedLocation ||
                !startingLatitude ||
                !startingLongitude ||
                !startingLatitude.value ||
                !startingLongitude.value
            ) {

                if (locationStatus) {

                    locationStatus.textContent =
                        "Please verify and select your exact starting location first.";

                    locationStatus.className =
                        "location-status error";
                }


                if (startingLocationInput) {

                    startingLocationInput.focus();
                }


                return;
            }


            // =================================================
            // GET USER INPUT
            // =================================================

            const startingLocation =
                verifiedLocation
                    ? verifiedLocation.value.trim()
                    : startingLocationInput.value.trim();


            const latitude =
                Number(
                    startingLatitude.value
                );


            const longitude =
                Number(
                    startingLongitude.value
                );


            const travelDate =
                getValue(
                    "travelDate"
                );


            const people =
                Number(
                    getValue(
                        "people"
                    )
                );


            const budget =
                Number(
                    getValue(
                        "budget"
                    )
                );


            const experience =
                getValue(
                    "experience"
                );


            const duration =
                Number(
                    getValue(
                        "duration"
                    )
                );


            const transport =
                getValue(
                    "transport"
                );


            const weatherPreference =
                getValue(
                    "weatherPreference"
                );


            const footfallPreference =
                getValue(
                    "footfallPreference"
                );


            // =================================================
            // BASIC FORM VALIDATION
            // =================================================

            if (!travelDate) {

                alert(
                    "Please select a travel date."
                );

                return;
            }


            if (
                !people ||
                people < 1
            ) {

                alert(
                    "Please enter a valid number of people."
                );

                return;
            }


            if (
                !budget ||
                budget <= 0
            ) {

                alert(
                    "Please enter a valid budget."
                );

                return;
            }


            if (
                !duration ||
                duration <= 0
            ) {

                alert(
                    "Please enter a valid trip duration."
                );

                return;
            }


            // =================================================
            // SHOW LOADING
            // =================================================

            if (loading) {

                loading.classList.remove(
                    "hidden"
                );
            }


            if (resultsSection) {

                resultsSection.classList.add(
                    "hidden"
                );
            }


            if (resultsContainer) {

                resultsContainer.innerHTML =
                    "";
            }


            if (generateBtn) {

                generateBtn.disabled =
                    true;
            }


            // =================================================
            // SEND REQUEST TO FASTAPI
            // =================================================

            try {

                console.log(
                    "Generating AI trip plan..."
                );


                const requestBody = {

                    starting_location:
                        startingLocation,

                    starting_latitude:
                        latitude,

                    starting_longitude:
                        longitude,

                    travel_date:
                        travelDate,

                    people:
                        people,

                    budget:
                        budget,

                    experience:
                        experience,

                    duration:
                        duration,

                    transport:
                        transport,

                    weather_preference:
                        weatherPreference,

                    footfall_preference:
                        footfallPreference
                };


                console.log(
                    "AI Planner Request:",
                    requestBody
                );


                const response =
                    await fetch(
                        `${API_URL}/api/ai/plan`,
                        {

                            method:
                                "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify(
                                    requestBody
                                )
                        }
                    );


                const data =
                    await response.json();


                console.log(
                    "AI Planner Response:",
                    data
                );


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "AI planner failed."
                    );
                }


                // =================================================
                // DISPLAY RESULTS
                // =================================================

                displayResults(
                    data.recommendations
                );


            } catch (error) {

                console.error(
                    "AI planner error:",
                    error
                );


                alert(
                    error.message ||
                    "Unable to generate recommendations."
                );


            } finally {

                if (loading) {

                    loading.classList.add(
                        "hidden"
                    );
                }


                if (generateBtn) {

                    generateBtn.disabled =
                        false;
                }

            }

        }
    );
}


// ============================================================
// DISPLAY RESULTS
// ============================================================

function displayResults(
    recommendations
) {

    if (!resultsContainer) {
        return;
    }


    resultsContainer.innerHTML =
        "";


    // ========================================================
    // NO RESULTS
    // ========================================================

    if (
        !recommendations ||
        !Array.isArray(
            recommendations
        ) ||
        recommendations.length === 0
    ) {

        resultsContainer.innerHTML = `
            <div class="no-results">
                <p>
                    No suitable destinations were found.
                </p>
            </div>
        `;


        if (resultsSection) {

            resultsSection.classList.remove(
                "hidden"
            );
        }


        return;
    }


    // ========================================================
    // CREATE RESULT CARDS
    // ========================================================

    recommendations.forEach(
        function (
            place,
            index
        ) {

            const image =
                getImageSource(
                    place.image
                );


            const card =
                document.createElement(
                    "article"
                );


            card.className =
                "result-card";


            card.innerHTML = `

                <img
                    class="result-image"
                    src="${escapeHTML(image)}"
                    alt="${escapeHTML(
                        place.destination ||
                        "Travel destination"
                    )}"
                    onerror="this.onerror=null;this.src='assets/img1.jpeg';"
                >

                <div class="result-content">

                    <span class="match">
                        ${Number(
                            place.ai_match || 0
                        )}%
                        AI MATCH
                    </span>


                    <h3>
                        ${index + 1}.
                        ${escapeHTML(
                            place.destination ||
                            "Unknown destination"
                        )}
                    </h3>


                    <p class="category">
                        ${escapeHTML(
                            place.category ||
                            ""
                        )}
                    </p>


                    <p class="result-description">
                        ${escapeHTML(
                            place.description ||
                            ""
                        )}
                    </p>


                    <div class="result-stats">

                        <div class="stat">

                            <small>
                                Estimated Budget
                            </small>

                            <strong>
                                ₹${Math.round(
                                    Number(
                                        place.estimated_budget ||
                                        0
                                    )
                                )}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Distance
                            </small>

                            <strong>
                                ${Number(
                                    place.distance_km ||
                                    0
                                ).toFixed(1)}
                                km
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Transport
                            </small>

                            <strong>
                                ${escapeHTML(
                                    place.transport ||
                                    "N/A"
                                )}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Transport Cost
                            </small>

                            <strong>
                                ₹${Math.round(
                                    Number(
                                        place.transport_cost ||
                                        0
                                    )
                                )}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Rating
                            </small>

                            <strong>
                                ⭐ ${escapeHTML(
                                    place.rating ??
                                    "N/A"
                                )}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Crowd
                            </small>

                            <strong>
                                ${escapeHTML(
                                    place.crowd_level ||
                                    "Unknown"
                                )}
                            </strong>

                        </div>

                    </div>


                    <button
                        class="result-book-now-btn"
                        type="button"
                    >
                        Book Now
                    </button>

                </div>
            `;


            // =================================================
            // STORE AI DATA ON BUTTON
            // =================================================

            const bookButton =
                card.querySelector(
                    ".result-book-now-btn"
                );


            if (bookButton) {

                bookButton.addEventListener(
                    "click",
                    function () {

                        handleBookNow(
                            place
                        );

                    }
                );
            }


            // =================================================
            // ADD CARD
            // =================================================

            resultsContainer.appendChild(
                card
            );

        }
    );


    // ========================================================
    // SHOW RESULTS
    // ========================================================

    if (resultsSection) {

        resultsSection.classList.remove(
            "hidden"
        );


        resultsSection.scrollIntoView(
            {
                behavior:
                    "smooth"
            }
        );
    }
}


// ============================================================
// BOOK NOW
// ============================================================
//
// IMPORTANT:
//
// The AI recommendation contains:
//
//     place.destination
//
// but your database booking system requires:
//
//     Trip.id
//
// Therefore:
//
// AI destination
//        ↓
// GET /api/trips
//        ↓
// Find matching Trip
//        ↓
// Get Trip.id
//        ↓
// GET /api/trips/{id}/hotels
//        ↓
// Open hotels.html?trip_id=id
//
// ============================================================

async function handleBookNow(
    place
) {

    const destinationName =
        String(
            place.destination ||
            ""
        )
        .trim();


    // ========================================================
    // DESTINATION REQUIRED
    // ========================================================

    if (!destinationName) {

        alert(
            "Destination information is missing."
        );

        return;
    }


    console.log(
        "===================================="
    );

    console.log(
        "BOOK NOW CLICKED"
    );

    console.log(
        "AI Destination:",
        destinationName
    );

    console.log(
        "===================================="
    );


    try {

        // ====================================================
        // GET ALL TRIPS FROM DATABASE
        // ====================================================

        console.log(
            "Loading trips from database..."
        );


        const response =
            await fetch(
                `${API_URL}/api/trips`
            );


        if (!response.ok) {

            throw new Error(
                `Trips API returned ${response.status}`
            );
        }


        const trips =
            await response.json();


        console.log(
            "Database trips:",
            trips
        );


        if (
            !Array.isArray(trips) ||
            trips.length === 0
        ) {

            throw new Error(
                "No trips are available in the database."
            );
        }


        // ====================================================
        // NORMALIZE TEXT
        // ====================================================

        function normalize(
            value
        ) {

            return String(
                value || ""
            )
            .toLowerCase()
            .replace(
                /[^a-z0-9\s]/g,
                " "
            )
            .replace(
                /\s+/g,
                " "
            )
            .trim();
        }


        const destination =
            normalize(
                destinationName
            );


        const destinationWords =
            destination
                .split(" ")
                .filter(
                    function (word) {

                        return (
                            word.length >= 3
                        );
                    }
                );


        // ====================================================
        // FIND BEST DATABASE TRIP
        // ====================================================

        let bestTrip =
            null;

        let bestScore =
            0;


        trips.forEach(
            function (trip) {

                const title =
                    normalize(
                        trip.title
                    );


                const route =
                    normalize(
                        trip.route
                    );


                const description =
                    normalize(
                        trip.description
                    );


                const category =
                    normalize(
                        trip.category
                    );


                const tags =
                    normalize(
                        trip.tags
                    );


                const recommendedFor =
                    normalize(
                        trip.recommended_for
                    );


                const allTripText = [

                    title,

                    route,

                    description,

                    category,

                    tags,

                    recommendedFor

                ].join(" ");


                let score =
                    0;


                // =================================================
                // EXACT TITLE MATCH
                // =================================================

                if (
                    title === destination
                ) {

                    score +=
                        100;
                }


                // =================================================
                // TITLE CONTAINS DESTINATION
                // =================================================

                if (
                    title.includes(
                        destination
                    )
                ) {

                    score +=
                        70;
                }


                // =================================================
                // ROUTE CONTAINS DESTINATION
                // =================================================
                //
                // Example:
                //
                // AI:
                //     Darjeeling
                //
                // Database:
                //     Kurseong → Mirik → Darjeeling
                //
                // This should match.
                //
                // =================================================

                if (
                    route.includes(
                        destination
                    )
                ) {

                    score +=
                        100;
                }


                // =================================================
                // DESCRIPTION MATCH
                // =================================================

                if (
                    description.includes(
                        destination
                    )
                ) {

                    score +=
                        40;
                }


                // =================================================
                // CATEGORY MATCH
                // =================================================

                if (
                    category.includes(
                        destination
                    )
                ) {

                    score +=
                        20;
                }


                // =================================================
                // TAG MATCH
                // =================================================

                if (
                    tags.includes(
                        destination
                    )
                ) {

                    score +=
                        20;
                }


                // =================================================
                // WORD LEVEL MATCH
                // =================================================

                destinationWords.forEach(
                    function (word) {

                        if (
                            allTripText.includes(
                                word
                            )
                        ) {

                            score +=
                                15;
                        }

                    }
                );


                // =================================================
                // SAVE BEST MATCH
                // =================================================

                if (
                    score >
                    bestScore
                ) {

                    bestScore =
                        score;

                    bestTrip =
                        trip;
                }

            }
        );


        // ====================================================
        // CHECK MATCH
        // ====================================================

        console.log(
            "Best matched trip:",
            bestTrip
        );


        console.log(
            "Match score:",
            bestScore
        );


        if (
            !bestTrip ||
            bestScore < 30
        ) {

            console.error(
                "No matching database trip found."
            );


            console.log(
                "AI destination:",
                destinationName
            );


            console.log(
                "Available database trips:",
                trips
            );


            alert(
                `No bookable trip is currently connected to "${destinationName}".`
            );


            return;
        }


        // ====================================================
        // VALID TRIP ID REQUIRED
        // ====================================================

        if (
            !bestTrip.id
        ) {

            alert(
                "The selected trip does not have a valid Trip ID."
            );


            return;
        }


        const tripId =
            bestTrip.id;


        console.log(
            "Matched Trip:",
            bestTrip.title
        );


        console.log(
            "Trip ID:",
            tripId
        );


        // ====================================================
        // CHECK HOTELS
        // ====================================================

        console.log(
            "Checking hotels..."
        );


        const hotelResponse =
            await fetch(
                `${API_URL}/api/trips/${encodeURIComponent(
                    tripId
                )}/hotels`
            );


        console.log(
            "Hotel API status:",
            hotelResponse.status
        );


        if (
            !hotelResponse.ok
        ) {

            let hotelError =
                "";


            try {

                const errorData =
                    await hotelResponse.json();


                hotelError =
                    errorData.detail ||
                    "";

            } catch (
                parseError
            ) {

                // Ignore JSON parsing error.

            }


            throw new Error(
                hotelError ||
                `Hotel API returned ${hotelResponse.status}`
            );
        }


        const hotels =
            await hotelResponse.json();


        console.log(
            "Hotels returned:",
            hotels
        );


        // ====================================================
        // NO HOTELS
        // ====================================================

        if (
            !Array.isArray(hotels) ||
            hotels.length === 0
        ) {

            alert(
                `No hotels have been added for "${bestTrip.title}" yet.`
            );


            console.warn(
                "No hotels found for Trip ID:",
                tripId
            );


            return;
        }


        // ====================================================
        // HOTELS FOUND
        // ====================================================

        console.log(
            `Found ${hotels.length} hotels for Trip ID ${tripId}.`
        );


        // ====================================================
        // OPEN HOTEL PAGE
        // ====================================================
        //
        // Your FastAPI frontend is served under /frontend.
        //
        // Correct:
        //
        // /frontend/hotels.html?trip_id=4
        //
        // ====================================================

        const hotelPage =
            `${API_URL}/frontend/hotels.html?trip_id=${encodeURIComponent(
                tripId
            )}`;


        console.log(
            "Opening hotel page:",
            hotelPage
        );


        window.location.href =
            hotelPage;

    } catch (error) {

        console.error(
            "===================================="
        );

        console.error(
            "BOOKING ERROR"
        );

        console.error(
            error
        );

        console.error(
            "===================================="
        );


        alert(
            error.message ||
            "Unable to open hotel booking."
        );
    }
}


// ============================================================
// HELPER: GET INPUT VALUE
// ============================================================

function getValue(
    id
) {

    const element =
        document.getElementById(
            id
        );


    if (!element) {

        console.warn(
            `Element #${id} was not found.`
        );


        return "";
    }


    return element.value;
}


// ============================================================
// HELPER: ESCAPE HTML
// ============================================================

function escapeHTML(
    value
) {

    const div =
        document.createElement(
            "div"
        );


    div.textContent =
        String(
            value ?? ""
        );


    return div.innerHTML;
}


// ============================================================
// PAGE LOAD
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "===================================="
        );

        console.log(
            "BengalTrail AI Planner loaded."
        );

        console.log(
            "API:",
            API_URL
        );

        console.log(
            "===================================="
        );

    }
);