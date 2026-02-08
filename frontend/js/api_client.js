const API_BASE_URL = "http://localhost:8000/api/dashboard";

async function fetchMetrics() {
    try {
        const response = await axios.get(`${API_BASE_URL}/metrics`, { timeout: 10000 });
        return response.data;
    } catch (error) {
        console.error("Error fetching metrics:", error);
        throw error;
    }
}

async function fetchHistory(period = "7d") {
    try {
        const response = await axios.get(`${API_BASE_URL}/history?period=${period}`, { timeout: 10000 });
        return response.data;
    } catch (error) {
        console.error("Error fetching history:", error);
        throw error;
    }
}
