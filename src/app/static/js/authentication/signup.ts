function signup(event: any){
    // Do signup submit.

    // Preventing reloading.
    event.preventDefault();

    // Send data.
    $.ajax({
        type: "POST",
        url: "/authentication/signup",
        dataType: 'json',
        data: {
            "username": $("#signup-username").val(),
            "email": $("#signup-email").val(),
            "password": $("#signup-password").val(),
            "password_confirmation": $("#signup-password-confirmation").val()
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
            let json = JSON.parse(xhr.responseText);
            if ("error" in json){
                signupError(json["error"], "api-error");
                return;
            }
            signupError(xhr.statusText, "xhr-error");
        }
    })
}

function signupError(text: string, name: string){
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

function signupMessage(html: string){
    // Show message.

    // Message.
    let message = $("#ajax-message");
    message.html(html);
    message.addClass("border")
    message.show();
}