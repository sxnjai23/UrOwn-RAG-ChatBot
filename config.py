import os

class Config:
    """
    Configuration class to manage file paths and settings for the application.
    """
    PDF_SOURCE_DIRECTORY: str = "data"
    CHROMA_PERSIST_DIRECTORY: str = "docs/chroma"

    # ---Embedding Model Configuration ---
    EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2" # "intfloat/multilingual-e5-large"
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    def __init__(self):
        os.makedirs(self.PDF_SOURCE_DIRECTORY, exist_ok=True)
        print(f"Configuration loaded. PDF documents should be placed in '{self.PDF_SOURCE_DIRECTORY}'.")
        
config = Config()
