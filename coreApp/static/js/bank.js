/**
 * 
 * @param {string} lastDaily formatted in iso
 */
function updateDailyCooldown(lastDaily) {
    let datedLast = new Date(lastDaily);
    let since = new Date(new Date() - datedLast);
    let cooldown = datedLast.getTime() + 86_400_000 - since
    let formattedCooldown = new Date(cooldown).toLocaleTimeString()

    document.getElementById("dailyCooldown").innerHTML = formattedCooldown;
}
