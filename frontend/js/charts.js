let growthChart;

function renderGrowthChart(data) {
    const ctx = document.getElementById("growth-chart").getContext("2d");
    const labels = data.map(item => item.date);
    const counts = data.map(item => item.count);

    if (growthChart) growthChart.destroy();

    growthChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Количество пенсионеров",
                data: counts,
                borderColor: "rgb(75, 192, 192)",
                tension: 0.1,
                fill: false
            }]
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
                    beginAtZero: true
                }
            }
        }
    });
}
