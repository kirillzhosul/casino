function diceBetPercentUpdateInput(value) {
    // Updates dice bet percent inpup text.

    // Update.
    let betPercent = document.getElementById("dice-game-bet-percent-input").value;
    if (betPercent != ""){
        if (betPercent < 1) betPercent = 1;
        if (betPercent > 95) betPercent = 95;
    }

    // Set value.
    document.getElementById("dice-game-bet-percent-input").value = betPercent;

    // Re-update win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
}

function diceBetSizeUpdateInput(value){
    // Updates bet size input.

    // Update.
    let betSize = document.getElementById("dice-game-bet-size-input").value;
    if (betSize != ""){
        if (betSize < 1) betSize = 1;
        if (betSize > Number.MAX_SAFE_INTEGER) betSize = Number.MAX_SAFE_INTEGER;
    }

    // Set value.
    document.getElementById("dice-game-bet-size-input").value = betSize;

    // Re-update win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
}

function diceBetPotentialWinSizeUpdate(){
    // Updates potential win size information preview.

    // Get values.
    let betPercent = parseInt(document.getElementById("dice-game-bet-percent-input").value);
    let betSize = parseInt(document.getElementById("dice-game-bet-size-input").value);

    // Calculate win size.
    let winSize = (100 / betPercent * betSize);
    winSize = winSize.toFixed(2);

    // Set.
    document.getElementById("dice-game-bet-potential-win-size").innerText = winSize;
}

function diceBetRangesUpdate(){
    // Updates bet ranges.

    // Get values.
    let betPercent = parseInt(document.getElementById("dice-game-bet-percent-input").value);

    // Max range for the bet value.
    let betRange = 1000000;

    // Difference for threshold max and min calculation.
    let betRequiredThresholdDifference = (betRange / 100) * betPercent

    // Set.
    document.getElementById("dice-game-bet-range-min").innerText = "0 - " + betRequiredThresholdDifference.toString();
    document.getElementById("dice-game-bet-range-max").innerText = (betRange - betRequiredThresholdDifference).toString() + " - " + betRange.toString();
}

function diceBetPlace(type){
    // Places bet, by sending request and showing result.

    // Get values.
    let betPercent = parseInt(document.getElementById("dice-game-bet-percent-input").value);
    let betSize = parseInt(document.getElementById("dice-game-bet-size-input").value);

    // Create url.
    let url = "/games/dice/?bet_size=" + betSize.toString() + "&bet_percent=" + betPercent.toString() + "&&bet_type=" + type.toString();

    // POST.
    $.ajax({
      type: "POST", url: url,
      success: function(data){
        if ("bet_response" in data && "bet_result" in data["bet_response"]){
            let betResult = data["bet_response"]["bet_result"];
            let betResults = document.getElementById("dice-game-bet-results");
            if (betResult){
                betResults.innerText = "Bet win!\n+ " + data["bet_response"]["bet_win_size"];
                betResults.classList.remove("text-danger");
                betResults.classList.add("text-success");
            }else{
                betResults.innerText = "Bet lose!\n- " + data["bet_arguments"]["bet_size"];
                betResults.classList.remove("text-success");
                betResults.classList.add("text-danger");
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
        let betPercent = 50;
        document.getElementById("dice-game-bet-percent-input").value = betPercent;
        diceBetPercentUpdateInput(betPercent);
    }
    // Potential win size.
    diceBetPotentialWinSizeUpdate();

    // Ranges.
    diceBetRangesUpdate();
})