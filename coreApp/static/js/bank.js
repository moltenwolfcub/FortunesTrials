/**
 * 
 * @param {string} lastDaily formatted in iso
 */
function updateDailyCooldown(lastDaily) {
    let msLast = +new Date(lastDaily);
    let msSince = Date.now()-msLast;
    let cooldownLength = 86_400_000;
    let timeLeft = cooldownLength-msSince;

    if (timeLeft<1) {
        document.location.reload()
    } else {
        let fmtTimeLeft = formatMs(timeLeft);

        document.getElementById("dailyCooldown").innerHTML = fmtTimeLeft;
    }
}

function formatMs(s) {
    var ms = s % 1000;
    s = (s - ms) / 1000;
    var secs = s % 60;
    s = (s - secs) / 60;
    var mins = s % 60;
    var hrs = (s - mins) / 60;

    var returnStr = secs;
    if (mins > 0) {
        returnStr = mins + ':' + returnStr;
    }
    if (hrs > 0) {
        if (mins <= 0) {
            returnStr = mins + ':' + returnStr;
        }
        returnStr = hrs + ':' + returnStr;
    }

    return returnStr;
}
