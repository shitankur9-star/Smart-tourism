document.addEventListener("DOMContentLoaded", async () => {

    const FALLBACK_API_URL = "http://127.0.0.1:8000";

    const API_URL = window.location.protocol.startsWith("http")
        ? `${window.location.protocol}//${window.location.hostname}${window.location.port ? ":" + window.location.port : ""}`
        : FALLBACK_API_URL;

    const FRONTEND_BASE_URL = `${API_URL}/frontend`;


    // ==========================================
    // CHECK LOGIN TOKEN
    // ==========================================

    const token = localStorage.getItem(
        "bengaltrail_token"
    );


    // ==========================================
    // USER IS NOT LOGGED IN
    // ==========================================

    if (!token) {

        window.location.href = `${FRONTEND_BASE_URL}/auth.html`;

        return;
    }


    // ==========================================
    // GET USER PROFILE
    // ==========================================

    try {

        const response = await fetch(
            `${API_URL}/api/profile`,
            {
                method: "GET",

                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            }
        );


        // ==========================================
        // TOKEN INVALID / EXPIRED
        // ==========================================

        if (response.status === 401) {

            localStorage.removeItem(
                "bengaltrail_token"
            );

            window.location.href = `${FRONTEND_BASE_URL}/auth.html`;

            return;
        }


        if (!response.ok) {

            throw new Error(
                "Unable to load profile"
            );
        }


        // ==========================================
        // GET USER DATA
        // ==========================================

        const user = await response.json();

        console.log("Logged in user:", user);

        // ==========================================
        // PROFILE PHOTO
        // ==========================================

        const profileImage =
            document.getElementById(
                "profileImage"
            );

        const defaultAvatar =
            document.getElementById(
                "defaultAvatar"
            );


        if (user.profile_image) {

            profileImage.src =
                `http://127.0.0.1:8000${user.profile_image}`;

            profileImage.style.display =
                "block";

            defaultAvatar.style.display =
                "none";

        } else {

            profileImage.style.display =
                "none";

            defaultAvatar.style.display =
                "block";
        }


        // ==========================================
        // DISPLAY USER INFORMATION
        // ==========================================

        document.getElementById(
            "profileName"
        ).textContent = user.full_name;


        document.getElementById(
            "profileEmail"
        ).textContent = user.email;


        document.getElementById(
            "fullName"
        ).textContent = user.full_name;


        document.getElementById(
            "email"
        ).textContent = user.email;


        document.getElementById(
            "userId"
        ).textContent = `#${user.id}`;


        if (user.created_at) {

            const date = new Date(
                user.created_at
            );

            document.getElementById(
                "memberSince"
            ).textContent =
                date.toLocaleDateString(
                    "en-IN",
                    {
                        day: "2-digit",
                        month: "short",
                        year: "numeric"
                    }
                );
        }


    } catch (error) {

        console.error(
            "Profile loading failed:",
            error
        );

    }


    // ==========================================
    // LOGOUT
    // ==========================================

    function logoutUser() {

        localStorage.removeItem(
            "bengaltrail_token"
        );

        window.location.href =
            `${FRONTEND_BASE_URL}/mainpage.html`;
    }


    const logoutBtn =
        document.getElementById("logoutBtn");


    const logoutBtnBottom =
        document.getElementById(
            "logoutBtnBottom"
        );


    if (logoutBtn) {

        logoutBtn.addEventListener(
            "click",
            logoutUser
        );

    }


    if (logoutBtnBottom) {

        logoutBtnBottom.addEventListener(
            "click",
            logoutUser
        );

    }

    // ==========================================
    // PROFILE PHOTO UPLOAD
    // ==========================================

    const profileImageInput =
        document.getElementById(
            "profileImageInput"
        );


    if (profileImageInput) {

        profileImageInput.addEventListener(
            "change",
            async () => {

                const file =
                    profileImageInput.files[0];


                if (!file) {
                    return;
                }


                // ----------------------------------
                // Check file type
                // ----------------------------------

                const allowedTypes = [
                    "image/jpeg",
                    "image/png",
                    "image/webp"
                ];


                if (!allowedTypes.includes(
                    file.type
                )) {

                    alert(
                        "Please select a JPG, PNG or WEBP image."
                    );

                    profileImageInput.value = "";

                    return;
                }


                // ----------------------------------
                // Check file size
                // ----------------------------------

                if (
                    file.size >
                    10 * 1024 * 1024
                ) {

                    alert(
                        "Image must be smaller than 10 MB."
                    );

                    profileImageInput.value = "";

                    return;
                }


                // ----------------------------------
                // Create FormData
                // ----------------------------------

                const formData =
                    new FormData();

                formData.append(
                    "file",
                    file
                );


                try {

                    const response =
                        await fetch(
                            "http://127.0.0.1:8000/api/profile/photo",
                            {

                                method: "POST",

                                headers: {

                                    "Authorization":
                                        `Bearer ${token}`

                                },

                                body: formData

                            }
                        );


                    const data =
                        await response.json();


                    if (!response.ok) {

                        alert(
                            data.detail ||
                            "Unable to upload image."
                        );

                        return;
                    }


                    // ----------------------------------
                    // Show new image immediately
                    // ----------------------------------

                    const profileImage =
                        document.getElementById(
                            "profileImage"
                        );


                    const defaultAvatar =
                        document.getElementById(
                            "defaultAvatar"
                        );


                    profileImage.src =
                        `http://127.0.0.1:8000${data.profile_image}`;


                    profileImage.style.display =
                        "block";


                    defaultAvatar.style.display =
                        "none";


                    alert(
                        "Profile photo updated successfully!"
                    );


                } catch (error) {

                    console.error(
                        "Photo upload error:",
                        error
                    );


                    alert(
                        "Unable to connect to the server."
                    );

                }

            }
        );
    }

});