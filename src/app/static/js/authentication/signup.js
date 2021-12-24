function signup(event){
    // Do signup submit.

    // Preventing reloading.
    event.preventDefault();

    // Getting all fields.
    let signupUsername = document.getElementById("signup-username").value;
    let signupMail = document.getElementById("signup-mail").value;
    let signupPassword = document.getElementById("signup-password").value;
    let signupPasswordVerfiy = document.getElementById("signup-password-verify").value;

    $.ajax({
        type: "POST",
        url: "/authentication/signup",
        data: {
            "username": signupUsername,
            "mail": signupMail,
            "password": signupPassword,
            "passwordVerify": signupPasswordVerfiy
        },
        success: function (data){
            if ("authentication" in data){
                // If this is valid data.

                // Get authentication details.
                let status = data.authentication.status;
                let message = data.authentication.message;

                if (status){
                    // If success authentication.

                    // Go root page.
                    window.location.href = "/";
                }else{
                    // If any error.

                    // Console.
                    console.log("Got authentication API error! Message from the server: " + message);
                }
            }
        },
        error: function(xhr){
            // If any error.

            // Console.
            console.log("Got authentication AJAX error! Message from the server: " + xhr.statusText);
        }
    })
}