import os
import pdfplumber
from sentence_transformers import SentenceTransformer
import pinecone

class DocumentProcessor:
    def __init__(self, pdf_dir, vector_db_api_key, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.pdf_dir = pdf_dir
        self.model = SentenceTransformer(model_name)
        pinecone.init(api_key=vector_db_api_key, environment='us-west1-gcp')
        self.index = pinecone.Index("intelligent_tutor")  

    def read_pdf(self, pdf_file):
        text_content = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text_content += page.extract_text()
        return text_content

    def generate_embeddings(self, text):
        sentences = text.split('\n')  
        embeddings = self.model.encode(sentences)
        return sentences, embeddings

    def upload_to_vector_db(self):
        for pdf_file in os.listdir(self.pdf_dir):
            if pdf_file.endswith(".pdf"):
                text = self.read_pdf(os.path.join(self.pdf_dir, pdf_file))
                sentences, embeddings = self.generate_embeddings(text)
                for i, embedding in enumerate(embeddings):
                    self.index.upsert([(f"{pdf_file}_{i}", embedding, {"sentence": sentences[i]})])

if __name__ == "__main__":
    processor = DocumentProcessor(pdf_dir="./pdf_files", vector_db_api_key="your_pinecone_api_key")
    processor.upload_to_vector_db()
