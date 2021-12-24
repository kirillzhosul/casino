function signup(event){
    // Do signup submit.

    // Preventing reloading.
    event.preventDefault();

    // Getting all fields.
    let signupUsername = document.getElementById("signup-username");
    let signupMail = document.getElementById("signup-mail");
    let signupPassword = document.getElementById("signup-password");
    let signupPasswordVerfiy = document.getElementById("signup-password-verify");

    $.ajax({
        "type": "POST",
        "url": "/authentication/signup",
        success: function (data){
            if ("authentication" in data){
                let authentication = data.authentication;

                // Get authentication details.
                let status = authentication.status;
                let message = authentication.message;

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