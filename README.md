# RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot that lets you ask questions about the contents of a PDF document. It extracts text from the PDF, splits the text into overlapping chunks, retrieves the most relevant chunk using TF-IDF and cosine similarity, and sends that context to Google's Gemini model to generate an answer.

## Features

- Extracts text from PDF files using `pdfplumber`
- Splits document text into smaller, overlapping chunks
- Creates TF-IDF vectors with `scikit-learn`
- Retrieves the most relevant chunk using cosine similarity
- Uses Google Gemini to generate an answer based on the retrieved context
- Checks a similarity threshold before sending context to Gemini

## Project structure

```text
RAG-Chatbot/
├── app.py              # Runs the command-line chatbot
├── chunker.py          # Splits document text into chunks
├── embedder.py         # Creates TF-IDF vectors
├── llm_gemini.py       # Calls the Gemini API
├── pdf_loader.py       # Extracts text from PDF files
├── searcher.py         # Finds the most relevant chunk
├── requirement.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore
└── data/
    └── Tutorial_EDIT.pdf   # Add your own PDF here (not included)
```

## Requirements

- Python 3.10 or later
- A Google Gemini API key
- A PDF document to query

## Setup and installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Tusharkarode/RAG-Chatbot.git
   cd RAG-Chatbot
   ```

2. **Create and activate a virtual environment**

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   The dependency file in this repository is named `requirement.txt`:

   ```bash
   python -m pip install -r requirement.txt
   ```

4. **Configure your Gemini API key**

   Copy `.env.example` to a new file named `.env` and add your API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   Keep `.env` private. Do not commit or share your API key.

5. **Add a PDF document**

   Create a `data` folder in the project root if it does not already exist, then place your PDF inside it with the filename:

   ```text
   data/Tutorial_EDIT.pdf
   ```

   The current `app.py` uses this exact file path. To use a different PDF, update the path in `app.py`.

## Run the chatbot

From the project root, run:

```bash
python app.py
```

Type a question when prompted. Type `exit` to stop the chatbot.

## How it works

1. **Load:** `pdf_loader.py` extracts text from the configured PDF.
2. **Chunk:** `chunker.py` divides the extracted text into overlapping word chunks.
3. **Vectorize:** `embedder.py` converts the chunks into TF-IDF vectors.
4. **Retrieve:** `searcher.py` compares the question vector with document chunk vectors using cosine similarity and returns the best-matching chunk.
5. **Check relevance:** `app.py` checks whether the similarity score meets the configured threshold (`0.1`).
6. **Generate:** `llm_gemini.py` sends the retrieved chunk and question to Gemini and prints the generated answer.

## Current implementation notes

- Retrieval currently uses **TF-IDF**, not transformer embeddings or a vector database such as FAISS.
- The current implementation retrieves the single best-matching chunk.
- The similarity threshold is set to `0.1` in `app.py`; you can tune it for your documents and questions.
- The chatbot currently runs in the terminal/command line.

## Troubleshooting

- **Missing API key:** Check that your `.env` file is in the project root and contains `GEMINI_API_KEY`.
- **PDF not found:** Confirm that `data/Tutorial_EDIT.pdf` exists, or update the path in `app.py`.
- **Missing Python package:** Activate the virtual environment and run `python -m pip install -r requirement.txt`.

## Future improvements

- Support multiple PDF and text documents
- Retrieve multiple relevant chunks
- Add a Streamlit or web-based chat interface
- Explore semantic embeddings and a vector database for retrieval

## License

No license has been specified yet. Contact the repository owner before reusing or distributing this project.
