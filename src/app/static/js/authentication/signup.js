function signup(event){
    // Do signup submit.

    // Preventing reloading.
    event.preventDefault();

    $.ajax({
        type: "POST",
        url: "/authentication/signup",
        data: {
            "username": $("#signup-username").value,
            "mail": $("#signup-mail").value,
            "password": $("#signup-password").value,
            "passwordVerify": $("#signup-password-verify").value
        },
        success: function (data){
            if (!("authentication" in data)){
                // Error if invalid data.
                signupError(data, "data-error");
                return;
            }

            if (!data.authentication.status){
                // If error when authenticating.

                // Error.
                signupError(data.authentication.message, "api-error");
                return;
            }

            // Success.
            signupSuccess();
        },
        error: function(xhr){
            // Error.
            signupError(statusText, "xhr-error");
        }
    })
}

function signupError(message, name){
    // Error signup.

    // Message.
    $("#ajax-message").html(
        "<big class='text-danger'>Sorry, unexpected error occured!</big><br><b>"
        + message +
        "</b><br><small class='text-muted'>"
        + name +
        "</small>"
    ).show();
}

function signupSuccess(){
    // Successfully signup.

    // Messsage.
    $("#ajax-message").html(
        "<big class='text-success'>Successfully authenticated!</big><br><small class='text-muted'>you will be redirected...</small>"
    ).show();

    // Go to root.
    window.location.href = "/";
}