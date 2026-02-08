document.addEventListener("DOMContentLoaded", async () => {
    async function updateMetrics() {
        try {
            document.getElementById("current-count").textContent = "Загрузка...";
            document.getElementById("connection-status").textContent = "Проверка...";

            const metrics = await fetchMetrics();
            document.getElementById("current-count").textContent = metrics.current_count;
            document.getElementById("last-updated").textContent = new Date(metrics.last_updated).toLocaleString();
            document.getElementById("connection-status").textContent = metrics.status === "active" ? "Активно" : "Ошибка";
        } catch (error) {
            console.error("Error updating metrics:", error);
            document.getElementById("current-count").textContent = "Ошибка";
            document.getElementById("connection-status").textContent = "Ошибка";
        }
    }

    async function updateChart(period = "7d") {
        try {
            const history = await fetchHistory(period);
            renderGrowthChart(history.data);
        } catch (error) {
            console.error("Error updating chart:", error);
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
