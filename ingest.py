import pdfplumber
import json

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file, keeping track of page numbers.
    Returns a list of tuples: (page_number, page_text)
    """
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                pages.append((page_number, page_text))
    return pages

def chunk_text_with_pages(pages, max_chars=1000):
    """
    Splits text into chunks by paragraphs while keeping track of page numbers.
    Returns a list of dictionaries: {"page": ..., "text": ...}
    """
    chunks = []

    for page_number, page_text in pages:
        paragraphs = [p.strip() for p in page_text.split("\n\n") if p.strip()]
        current_chunk = ""
        for paragraph in paragraphs:
            # If adding this paragraph exceeds max_chars, save current chunk first
            if len(current_chunk) + len(paragraph) + 2 > max_chars:
                if current_chunk:  # avoid empty chunk
                    chunks.append({"page": page_number, "text": current_chunk.strip()})
                current_chunk = paragraph
            else:
                if current_chunk:
                    current_chunk += "\n\n" + paragraph
                else:
                    current_chunk = paragraph
        # Add remaining chunk for this page
        if current_chunk:
            chunks.append({"page": page_number, "text": current_chunk.strip()})

    return chunks

if __name__ == "__main__":
    pdf_path = "data/sample.pdf"

    # 1. Extract text from PDF with page numbers
    pages = extract_text_from_pdf(pdf_path)

    # 2. Preview first 2000 characters from all pages combined
    combined_text = "\n\n".join([p[1] for p in pages])
    print("PDF TEXT PREVIEW:")
    print(combined_text[:2000])

    # 3. Split text into chunks with page references
    text_chunks = chunk_text_with_pages(pages, max_chars=1000)

    # 4. Print total chunks and preview first 3
    print(f"\nTotal chunks created: {len(text_chunks)}")
    print("\n--- First 3 chunks preview ---")
    for i, chunk in enumerate(text_chunks[:3], start=1):
        print(f"\nChunk {i} (Page {chunk['page']}):\n{chunk['text']}")

    # 5. Save chunks to JSON file
    with open("chunks_output.json", "w", encoding="utf-8") as f:
        json.dump(text_chunks, f, ensure_ascii=False, indent=4)
    print("\nChunks saved to chunks_output.json")

    # 6. Save chunks to text file with page references
    with open("chunks_output.txt", "w", encoding="utf-8") as f:
        for i, chunk in enumerate(text_chunks, start=1):
            f.write(f"--- Chunk {i} (Page {chunk['page']}) ---\n")
            f.write(chunk['text'] + "\n\n")
    print("Chunks also saved to chunks_output.txt")
