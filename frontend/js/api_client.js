const API_BASE_URL = "http://localhost:8000/api/dashboard";

async function fetchMetrics() {
    try {
        const response = await axios.get(`${API_BASE_URL}/metrics`);
        return response.data;
    } catch (error) {
        console.error("Error fetching metrics:", error);
        throw error;
    }
}

async function fetchHistory(period = "30d") {
    try {
        const response = await axios.get(`${API_BASE_URL}/history?period=${period}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching history:", error);
        throw error;
    }
}
