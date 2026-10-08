from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


reader = PdfReader("document.pdf")

pages = []

for page in reader.pages:
    pages.append(page.extract_text())


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


all_chunks = []

for page_number, page_text in enumerate(pages, start=1):

    chunks = splitter.split_text(page_text)

    for chunk in chunks:
        all_chunks.append({
            "document": "document.pdf",
            "page": page_number,
            "text": chunk
        })


print(f"Total chunks: {len(all_chunks)}")

for i, chunk in enumerate(all_chunks[:3]):
    print(f"\n--- CHUNK {i + 1} | PAGE {chunk['page']} ---\n")
    print(chunk["text"])