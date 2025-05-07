# 🧠 AI Text Summarizer

A web-based AI tool that provides concise, intelligent summaries from raw text, news articles, and PDF documents. Built using a fine-tuned BART model, it offers a seamless user experience powered by a Flask backend and React frontend.

## ✨ Features

- 📝 **Manual Text Summarization** – Paste any block of text and generate a summary.
- 🌐 **News Article Summarization** – Enter a news URL and get an AI-generated summary of the content.
- 📄 **PDF Summarization** – Upload PDF files and receive an accurate summary of the document.
- 💻 **Interactive User Interface** – Built using Bootstrap for a clean, responsive design.
- 🔄 **Full-Stack Architecture** – Smooth communication between frontend and backend using REST APIs.

## 🧩 Tech Stack

### 🔙 Backend
- Python (Flask)
- `flask-cors`
- `transformers` (`facebook/bart-large-cnn`)
- `newspaper3k` (for extracting article text from URLs)
- `PyMuPDF` (for parsing PDF content)

### 🔜 Frontend
- React.js
- Axios
- Bootstrap
- React-Toastify (for notifications)
