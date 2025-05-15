import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export const summarizeText = async (text) => {
    const response = await axios.post(`${API_URL}/summarize`, { text });
    return response.data;
};

export const summarizeURL = async (url) => {
    const response = await axios.post(`${API_URL}/summarize-url`, { url });
    return response.data;
};

export const summarizePDF = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(`${API_URL}/summarize-pdf`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
};
