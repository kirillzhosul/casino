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