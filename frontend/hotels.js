const API_BASE_URL =
    "http://127.0.0.1:8000";


// =====================================================
// GET TRIP ID FROM URL
// =====================================================

const urlParams =
    new URLSearchParams(
        window.location.search
    );


const tripId =
    urlParams.get("trip_id");


console.log(
    "Selected Trip ID:",
    tripId
);


// =====================================================
// ELEMENTS
// =====================================================

const hotelsContainer =
    document.getElementById(
        "hotelsContainer"
    );


const tripRoute =
    document.getElementById(
        "tripRoute"
    );


// =====================================================
// CHECK TRIP ID
// =====================================================

if (!tripId) {

    hotelsContainer.innerHTML = `

        <div class="error">

            <h2>
                Trip not selected
            </h2>

            <p>
                Please return to the trip page
                and select a trip.
            </p>

        </div>

    `;

} else {

    loadHotels();

}


// =====================================================
// LOAD HOTELS
// =====================================================

async function loadHotels() {

    try {

        const response =
            await fetch(
                `${API_BASE_URL}/api/trips/${tripId}/hotels`
            );


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const hotels =
            await response.json();


        console.log(
            "Hotels received:",
            hotels
        );


        renderHotels(
            hotels
        );


    } catch (error) {

        console.error(
            "Hotel loading error:",
            error
        );


        hotelsContainer.innerHTML = `

            <div class="error">

                <h2>
                    Unable to load hotels
                </h2>

                <p>
                    ${error.message}
                </p>

            </div>

        `;

    }

}


// =====================================================
// RENDER HOTELS
// =====================================================

function renderHotels(
    hotels
) {

    hotelsContainer.innerHTML = "";


    if (!hotels || hotels.length === 0) {

        hotelsContainer.innerHTML = `

            <div class="error">

                <h2>
                    No hotels available
                </h2>

                <p>
                    No hotels have been added
                    for this trip yet.
                </p>

            </div>

        `;

        return;

    }


    hotels.forEach(
        hotel => {

            const card =
                document.createElement(
                    "article"
                );


            card.className =
                "hotel-card";


            const image =
                hotel.image ||
                "assets/img1.jpeg";


            const facilities =
                hotel.facilities
                    ? hotel.facilities
                        .split(",")
                        .join(" • ")
                    : "Facilities not specified";


            card.innerHTML = `

                <img
                    class="hotel-image"
                    src="${image}"
                    alt="${hotel.name}"
                    onerror="
                        this.src='assets/img1.jpeg'
                    "
                >


                <div
                    class="hotel-content"
                >

                    <h2>
                        ${hotel.name}
                    </h2>


                    <div
                        class="hotel-location"
                    >

                        📍 ${hotel.location || "Bengal"}

                    </div>


                    <div
                        class="hotel-rating"
                    >

                        ⭐ ${hotel.rating || "N/A"} / 5

                    </div>


                    <div
                        class="hotel-price"
                    >

                        ₹${hotel.price_per_night || "N/A"}

                        <span>
                            / night
                        </span>

                    </div>


                    <div
                        class="hotel-room"
                    >

                        🛏️ ${hotel.room_type || "Room"}

                    </div>


                    <div
                        class="hotel-facilities"
                    >

                        ${facilities}

                    </div>


                    <button
                        class="choose-hotel-btn"
                        data-hotel-id="${hotel.id}"
                    >

                        Choose This Hotel

                    </button>

                </div>

            `;


            hotelsContainer.appendChild(
                card
            );

        }
    );

}


// =====================================================
// CHOOSE HOTEL
// =====================================================

document.addEventListener(
    "click",
    function(event) {

        const button =
            event.target.closest(
                ".choose-hotel-btn"
            );


        if (!button) {
            return;
        }


        const hotelId =
            button.dataset.hotelId;


        console.log(
            "Selected Hotel ID:",
            hotelId
        );


        /*
         * NEXT STEP:
         *
         * We will create the booking page here.
         *
         * Example:
         *
         * booking.html?trip_id=4&hotel_id=1
         */


        alert(
            `Hotel ${hotelId} selected`
        );

    }
);