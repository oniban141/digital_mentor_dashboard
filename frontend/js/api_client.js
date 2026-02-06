const API_BASE_URL = "http://localhost:8000/api/dashboard";

async function fetchMetrics() {
    const response = await fetch(`${API_BASE_URL}/metrics`);
    if (!response.ok) throw new Error(`Ошибка загрузки метрик: ${response.status}`);
    return await response.json();
}

async function fetchHistory(period = "7d") {
    const response = await fetch(`${API_BASE_URL}/history?period=${period}`);
    if (!response.ok) throw new Error(`Ошибка загрузки истории: ${response.status}`);
    return await response.json();
}
