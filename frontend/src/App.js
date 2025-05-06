import React, { useState } from "react";
import { summarizeText, summarizeURL, summarizePDF } from "./services/api";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [inputText, setInputText] = useState("");
    const [url, setURL] = useState("");
    const [file, setFile] = useState(null);
    const [summary, setSummary] = useState("");

    const handleSummarizeText = async () => {
        const res = await summarizeText(inputText);
        setSummary(res.summary);
    };

    const handleSummarizeURL = async () => {
        const res = await summarizeURL(url);
        setSummary(res.summary);
    };

    const handleSummarizePDF = async () => {
        if (!file) {
            toast.error("Please select a PDF file.");
            return;
        }
        const res = await summarizePDF(file);
        setSummary(res.summary);
    };

    return (
        <div className="container mt-4">
            <h2 className="text-center">AI Text Summarizer</h2>
            
            <textarea 
                className="form-control mt-3"
                rows="4"
                placeholder="Enter text to summarize..."
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
            />
            <button className="btn btn-primary mt-2" onClick={handleSummarizeText}>Summarize Text</button>

            <input 
                type="text" 
                className="form-control mt-3" 
                placeholder="Enter news URL..."
                value={url}
                onChange={(e) => setURL(e.target.value)}
            />
            <button className="btn btn-success mt-2" onClick={handleSummarizeURL}>Summarize URL</button>

            <input type="file" className="form-control mt-3" onChange={(e) => setFile(e.target.files[0])} />
            <button className="btn btn-warning mt-2" onClick={handleSummarizePDF}>Summarize PDF</button>

            <h4 className="mt-4">Summary:</h4>
            <p className="alert alert-info">{summary}</p>

            <ToastContainer />
        </div>
    );
}

export default App;