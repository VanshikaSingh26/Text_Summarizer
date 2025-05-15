from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import fitz  # PyMuPDF for PDFs
import newspaper
import os

app = Flask(__name__)
CORS(app)

# Load Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# 📌 Summarization from Text
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    return jsonify({"summary": generate_summary(text)})

# 📌 Summarization from News URL
@app.route("/summarize-url", methods=["POST"])
def summarize_url():
    data = request.json
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        text = article.text.strip()

        if len(text) < 200:
            return jsonify({"error": "Article text is too short for summarization"}), 400

        return jsonify({"summary": generate_summary(text)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 Summarization from PDF
@app.route("/summarize-pdf", methods=["POST"])
def summarize_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text_from_pdf(filepath)
    if not text or len(text) < 200:
        return jsonify({"error": "Extracted text is too short for summarization"}), 400

    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = [generate_summary(chunk) for chunk in chunks]

    return jsonify({"summary": " ".join(summaries)})

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join([page.get_text("text") for page in doc])
    return text.strip()

def generate_summary(text):
    """Dynamically adjusts summarization length based on input size."""
    token_count = len(text.split())

    max_len = max(50, int(token_count * 0.5))  # 50% of input
    min_len = max(20, int(token_count * 0.25))  # 25% of input

    if token_count < 50:
        return text  # If too short, return original

    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    app.run(debug=True)