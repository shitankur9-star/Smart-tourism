// ==========================================
// BENGALTRAIL AUTHENTICATION
// ==========================================

// const FALLBACK_API_URL = "http://127.0.0.1:8000";

// const API_URL = window.location.protocol.startsWith("http")
//     ? `${window.location.protocol}//${window.location.hostname}${window.location.port ? ":" + window.location.port : ""}`
//     : FALLBACK_API_URL;

// if (window.location.protocol === "file:") {
//     window.location.href = `${FALLBACK_API_URL}/frontend/auth.html`;
// }

const API_URL = "http://127.0.0.1:8000";

// ==========================================
// ELEMENTS
// ==========================================

const loginContainer =
    document.getElementById("loginContainer");

const signupContainer =
    document.getElementById("signupContainer");

const loginForm =
    document.getElementById("loginForm");

const signupForm =
    document.getElementById("signupForm");

const showSignup =
    document.getElementById("showSignup");

const showLogin =
    document.getElementById("showLogin");

const loginMessage =
    document.getElementById("loginMessage");

const signupMessage =
    document.getElementById("signupMessage");


// ==========================================
// SWITCH LOGIN → SIGNUP
// ==========================================

showSignup.addEventListener("click", () => {

    loginContainer.classList.add("hidden");

    signupContainer.classList.remove("hidden");

    clearMessages();

});


// ==========================================
// SWITCH SIGNUP → LOGIN
// ==========================================

showLogin.addEventListener("click", () => {

    signupContainer.classList.add("hidden");

    loginContainer.classList.remove("hidden");

    clearMessages();

});


// ==========================================
// CLEAR MESSAGES
// ==========================================

function clearMessages() {

    loginMessage.textContent = "";

    signupMessage.textContent = "";

}


// ==========================================
// PASSWORD VISIBILITY
// ==========================================

function setupPasswordToggle(
    inputId,
    buttonId
) {

    const input =
        document.getElementById(inputId);

    const button =
        document.getElementById(buttonId);

    button.addEventListener("click", () => {

        if (input.type === "password") {

            input.type = "text";

            button.innerHTML =
                '<i class="ri-eye-off-line"></i>';

        } else {

            input.type = "password";

            button.innerHTML =
                '<i class="ri-eye-line"></i>';

        }

    });

}


setupPasswordToggle(
    "loginPassword",
    "loginPasswordToggle"
);


setupPasswordToggle(
    "signupPassword",
    "signupPasswordToggle"
);


// ==========================================
// SIGN UP
// ==========================================

signupForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        // ----------------------------------
        // Get form values
        // ----------------------------------

        const fullName =
            document
                .getElementById("signupName")
                .value
                .trim();


        const email =
            document
                .getElementById("signupEmail")
                .value
                .trim();


        const password =
            document
                .getElementById("signupPassword")
                .value;


        // ----------------------------------
        // Basic validation
        // ----------------------------------

        if (!fullName) {

            showMessage(
                signupMessage,
                "Please enter your full name.",
                "error"
            );

            return;
        }


        if (password.length < 6) {

            showMessage(
                signupMessage,
                "Password must be at least 6 characters.",
                "error"
            );

            return;
        }


        // ----------------------------------
        // Disable button
        // ----------------------------------

        const button =
            signupForm.querySelector(
                ".auth-btn"
            );

        button.disabled = true;

        button.innerHTML =
            `Creating Account
             <i class="ri-loader-4-line"></i>`;


        try {

            // ----------------------------------
            // Send signup request
            // ----------------------------------

            const response =
                await fetch(
                    `${API_URL}/api/signup`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            full_name: fullName,

                            email: email,

                            password: password

                        })

                    }
                );


            const data =
                await response.json();


            // ----------------------------------
            // Signup failed
            // ----------------------------------

            if (!response.ok) {

                let message =
                    data.detail ||
                    "Unable to create account.";


                showMessage(
                    signupMessage,
                    message,
                    "error"
                );


                return;
            }


            // ----------------------------------
            // Signup successful
            // ----------------------------------

            localStorage.setItem(
                "bengaltrail_token",
                data.access_token
            );


            showMessage(
                signupMessage,
                "Account created successfully! Redirecting...",
                "success"
            );

            localStorage.setItem(
                "bengaltrail_token",
                data.access_token
            );

            // setTimeout(() => {
            //     window.location.href = "mainpage.html";
            // }, 1000);


            // ----------------------------------
            // Redirect to landing page
            // ----------------------------------

            setTimeout(() => {

                window.location.href =
                    "mainpage.html";

            }, 1000);


        } catch (error) {

            console.error(
                "Signup error:",
                error
            );


            showMessage(
                signupMessage,
                "Unable to connect to the BengalTrail server.",
                "error"
            );


        } finally {

            button.disabled = false;

            button.innerHTML =
                `Create Account
                 <i class="ri-arrow-right-line"></i>`;

        }

    }
);


// ==========================================
// LOGIN
// ==========================================

loginForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        // ----------------------------------
        // Get form values
        // ----------------------------------

        const email =
            document
                .getElementById("loginEmail")
                .value
                .trim();


        const password =
            document
                .getElementById("loginPassword")
                .value;


        // ----------------------------------
        // Disable button
        // ----------------------------------

        const button =
            loginForm.querySelector(
                ".auth-btn"
            );


        button.disabled = true;

        button.innerHTML =
            `Signing In
             <i class="ri-loader-4-line"></i>`;


        try {

            // ----------------------------------
            // Send login request
            // ----------------------------------

            const response =
                await fetch(
                    `${API_URL}/api/login`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            email: email,

                            password: password

                        })

                    }
                );


            const data =
                await response.json();


            // ----------------------------------
            // Login failed
            // ----------------------------------

            if (!response.ok) {

                showMessage(
                    loginMessage,
                    data.detail ||
                        "Invalid email or password.",
                    "error"
                );


                return;
            }


            // ----------------------------------
            // Login successful
            // ----------------------------------

            localStorage.setItem(
                "bengaltrail_token",
                data.access_token
            );


            showMessage(
                loginMessage,
                "Login successful! Redirecting...",
                "success"
            );

            localStorage.setItem(
                "bengaltrail_token",
                data.access_token
            );

            // setTimeout(() => {
            //     window.location.href = "profile.html";
            // }, 800);


            // ----------------------------------
            // Redirect to landing page
            // ----------------------------------

            setTimeout(() => {

                window.location.href =
                    "profile.html";

            }, 800);


        } catch (error) {

            console.error(
                "Login error:",
                error
            );


            showMessage(
                loginMessage,
                "Unable to connect to the BengalTrail server.",
                "error"
            );


        } finally {

            button.disabled = false;

            button.innerHTML =
                `Sign In
                 <i class="ri-arrow-right-line"></i>`;

        }

    }
);


// ==========================================
// SHOW MESSAGE
// ==========================================

function showMessage(
    element,
    message,
    type
) {

    element.textContent = message;


    if (type === "success") {

        element.style.color =
            "#16a34a";

    } else {

        element.style.color =
            "#dc2626";

    }

}


///LOGOUT

function logoutUser() {

    localStorage.removeItem(
        "bengaltrail_token"
    );

    window.location.href =
        "mainpage.html";
}