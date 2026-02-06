document.addEventListener("DOMContentLoaded", async () => {
    async function updateMetrics() {
        try {
            const metrics = await fetchMetrics();
            console.log("Metrics:", metrics);
            document.getElementById("current-count").textContent = metrics.current_count;
            document.getElementById("last-updated").textContent = new Date(metrics.last_updated).toLocaleString();
            document.getElementById("connection-status").textContent = metrics.status === "active" ? "Активно" : "Ошибка";
        } catch (error) {
            console.error("Error fetching metrics:", error);
            document.getElementById("connection-status").textContent = "Ошибка";
        }
    }

    async function updateChart(period = "7d") {
        try {
            const history = await fetchHistory(period);
            console.log("History:", history);
            renderGrowthChart(history.data);
        } catch (error) {
            console.error("Error fetching history:", error);
        }
    }

    document.getElementById("refresh-btn").addEventListener("click", updateMetrics);

    document.querySelectorAll(".period-selector button").forEach(button => {
        button.addEventListener("click", () => {
            updateChart(button.dataset.period);
        });
    });

    await updateMetrics();
    await updateChart();
});
