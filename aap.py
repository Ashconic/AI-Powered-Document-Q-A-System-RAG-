from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline

# Example usage
if __name__ == "__main__":
    docs = load_all_documents("data")
    
    if docs:
        print(f"\nFirst document preview:")

        first_doc = docs[0]
        if hasattr(first_doc, "page_content"):
            safe_preview = first_doc.page_content[:1000]
            print(safe_preview)
        else:
            print(str(first_doc))

    chunks = EmbeddingPipeline().chunk_documents(docs)
    chunkvectors=EmbeddingPipeline().embed_chunks(chunks)