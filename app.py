from pdf_loader import load_pdf
from chunker import chunk_text
from embedder import create_embeddings
from searcher import search
from llm_gemini import ask_gemini

SIMILARITY_THRESHOLD = 0.1

print("📄 Loading PDF...")
text = load_pdf("data/Tutorial_EDIT.pdf")

chunks = chunk_text(text, chunk_size=200)
embeddings, vectorizer = create_embeddings(chunks)

print("\n🤖 Gemini-Powered PDF Chatbot Ready!")
print("Type your question (exit to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        print("🤖 Bye!")
        break

    best_chunk, score = search(
        query,
        chunks,
        embeddings,
        vectorizer,
        top_k=1
    )

    # ❌ No relevant content
    if score < SIMILARITY_THRESHOLD:
        print("\n🤖 Answer:\n")
        print("The document does not contain information related to your query.")
        print("\n" + "-" * 50)
        continue

    # ✅ Relevant content found
    answer = ask_gemini(best_chunk, query)

    print("\n🤖 Answer:\n")
    print(answer)
    print("\n" + "-" * 50)
