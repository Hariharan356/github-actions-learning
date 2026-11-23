
function refreshDashboard() {
    const button = document.querySelector(".refresh-btn");

    button.textContent = "Refreshing...";

    setTimeout(() => {
        button.textContent = "↻ Refresh";
        document.getElementById("app-status").textContent = "Operational";
    }, 600);
}
