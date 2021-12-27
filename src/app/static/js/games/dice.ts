function diceBetPercentUpdateInput() {
    // Updates dice bet percent inpup text.

    // Update.
    let betPercent: any = $("#dice-game-bet-percent-input").val();
    if (betPercent != "" && typeof betPercent == "number"){
        if (betPercent < 1) betPercent = 1;
        if (betPercent > 95) betPercent = 95;
    }

    // Set value.
    $("#dice-game-bet-percent-input").val(betPercent);

    // Re-update win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
}

function diceBetSizeUpdateInput(){
    // Updates bet size input.

    // Update.
    let betSize: any = $("#dice-game-bet-size-input").val();
    if (betSize != "" && typeof betSize == "number"){
        if (betSize < 1) betSize = 1;
        if (betSize > Number.MAX_SAFE_INTEGER) betSize = Number.MAX_SAFE_INTEGER;
    }

    // Set value.
    $("#dice-game-bet-size-input").val(betSize);

    // Re-update win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
}

function diceBetPotentialWinSizeUpdate(){
    // Updates potential win size information preview.

    // Get values.
    let betPercent: number = Number($("#dice-game-bet-percent-input").val());
    let betSize: number = Number($("#dice-game-bet-size-input").val());

    // Calculate win size.
    let winSize: number = -1;
    if (typeof betSize == "number" && typeof betPercent == "number"){
        winSize = (100 / betPercent * betSize);
    }
    
    // Set.
    $("#dice-game-bet-potential-win-size").text(winSize.toFixed(2));
}

function diceBetRangesUpdate(){
    // Updates bet ranges.

    // Get values.
    let betPercent: any = $("#dice-game-bet-percent-input").val();

    // Max range for the bet value.
    let betRange: number = 1000000;

    // Difference for threshold max and min calculation.
    let betRequiredThresholdDifference: number = (betRange / 100) * betPercent

    // Set.
    $("#dice-game-bet-range-min").text("0 - " + betRequiredThresholdDifference.toString());
    $("#dice-game-bet-range-max").text((betRange - betRequiredThresholdDifference).toString() + " - " + betRange.toString());
}

function diceBetPlace(type: string){
    // Places bet, by sending request and showing result.

    // Get values.
    let betPercent: any = $("#dice-game-bet-percent-input").val();
    let betSize: any = $("#dice-game-bet-size-input").val();

    // Create url.
    let url: string = "/games/dice/?bet_size=" + betSize.toString() + "&bet_percent=" + betPercent.toString() + "&&bet_type=" + type.toString();

    // POST.
    $.ajax({
      type: "POST", url: url,
      success: function(data){
        if ("bet_response" in data && "bet_result" in data["bet_response"]){
            let betResult = data["bet_response"]["bet_result"];
            let betResults = $("#dice-game-bet-results");
            if (betResult){
                betResults.text("Bet win!\n+ " + data["bet_response"]["bet_win_size"]);
                betResults.removeClass("text-danger");
                betResults.addClass("text-success");
            }else{
                betResults.text("Bet lose!\n- " + data["bet_arguments"]["bet_size"]);
                betResults.removeClass("text-success");
                betResults.addClass("text-danger");
            }
            return;
        }

        alert("Failed to place bet! Invalid response data!");
      },
    });
}

window.addEventListener("load", function () {
    // Page is loaded.

    // Set default values.
    {
        // Bet percents.
        $("#dice-game-bet-percent-input").val(50);
        diceBetPercentUpdateInput();
    }

    // Potential win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
})