from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_chunker(chunk_size: int = 500, chunk_overlap: int = 50):
    """
    Utility function that returns a configured text splitter 
    optimized for legal markdown documents.
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n# ", "\n## ", "\n\n", "\n", " ", ""]
    )

def chunk_text(text: str) -> list[str]:
    """
    Takes a raw string of text and returns a list of chunked strings.
    """
    chunker = get_text_chunker()
    return chunker.split_text(text)