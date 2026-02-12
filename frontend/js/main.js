let historyChart;

document.addEventListener("DOMContentLoaded", async () => {
    async function updateMetrics() {
        try {
            document.getElementById("pensioners-count").textContent = "Загрузка...";
            document.getElementById("volunteers-count").textContent = "Загрузка...";
            document.getElementById("connection-status").textContent = "Проверка...";

            const metrics = await fetchMetrics();
            document.getElementById("pensioners-count").textContent = metrics.pensioners_count;
            document.getElementById("volunteers-count").textContent = metrics.volunteers_count;
            document.getElementById("last-updated").textContent = new Date(metrics.last_updated).toLocaleString();
            document.getElementById("connection-status").textContent = metrics.status === "active" ? "Активно" : metrics.status;
        } catch (error) {
            console.error("Error updating metrics:", error);
            document.getElementById("pensioners-count").textContent = "Ошибка загрузки";
            document.getElementById("volunteers-count").textContent = "Ошибка загрузки";
            document.getElementById("connection-status").textContent = "Ошибка сервера";
        }
    }

    async function updateHistoryChart(period = "30d") {
        try {
            const loadingElement = document.createElement('div');
            loadingElement.className = 'loading';
            loadingElement.textContent = 'Загрузка данных...';
            document.getElementById("history-chart").before(loadingElement);

            const history = await fetchHistory(period);
            loadingElement.remove();
            renderHistoryChart(history);
        } catch (error) {
            console.error("Error updating history chart:", error);
            const loadingElement = document.querySelector('.loading') || document.createElement('div');
            loadingElement.className = 'loading';
            loadingElement.textContent = "Ошибка загрузки данных";
            document.getElementById("history-chart").before(loadingElement);
        }
    }

    function renderHistoryChart(history) {
        const ctx = document.getElementById("history-chart").getContext("2d");
        const labels = history.pensioners.map(item => item.date);
        const pensionersData = history.pensioners.map(item => item.count);
        const volunteersData = history.volunteers.map(item => item.count);

        if (historyChart) historyChart.destroy();

        historyChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Пенсионеры",
                        data: pensionersData,
                        borderColor: "rgb(75, 192, 192)",
                        tension: 0.1,
                        fill: false
                    },
                    {
                        label: "Волонтеры",
                        data: volunteersData,
                        borderColor: "rgb(192, 75, 192)",
                        tension: 0.1,
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    tooltip: {
                        mode: "index",
                        intersect: false,
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Количество'
                        }
                    }
                }
            }
        });
    }

    document.getElementById("refresh-btn").addEventListener("click", updateMetrics);

    document.querySelectorAll(".period-selector button").forEach(button => {
        button.addEventListener("click", () => {
            updateHistoryChart(button.dataset.period);
        });
    });

    await updateMetrics();
    await updateHistoryChart();
});
