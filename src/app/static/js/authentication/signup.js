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
            "passwordConfirmation": $("#signup-password-confirmation").value
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
            signupError(xhr.statusText, "xhr-error");
        }
    })
}

function signupError(text, name){
    // Error signup.

    // Message
    signupMessage(
        "<big class='text-danger'>Sorry, unexpected error occured!</big><br><b>"
        + text +
        "</b><br><small class='text-muted'>"
        + name +
        "</small>"
    );
}

function signupSuccess(){
    // Successfully signup.

    // Messsage.
    signupMessage(
        "<big class='text-success'>Successfully authenticated!</big><br><small class='text-muted'>you will be redirected...</small>"
    );

    // Go to root.
    window.location.href = "/";
}

function signupMessage(html){
    // Show message.

    // Message.
    let message = $("#ajax-message");
    message.html(html);
    message.addClass("border")
    message.show();
}