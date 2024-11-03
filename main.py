from document_processing import DocumentProcessor
from user_view import QueryProcessor
from response_generation import ResponseGenerator
from sentence_transformers import SentenceTransformer

def main():
    # Phase 1: Document Processing
    document_processor = DocumentProcessor(pdf_dir="./pdf_files", vector_db_api_key="your_pinecone_api_key")
    document_processor.upload_to_vector_db()

    # Phase 2: User Query Input
    query_processor = QueryProcessor()
    user_query = input("Please enter your question: ")
    level = input("Please specify the detail level (beginner, intermediate, expert): ").strip().lower()
    processed_query_data = query_processor.process_query(user_query, level)

    # Generate embedding for the processed query
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    query_embedding = model.encode(processed_query_data["query"])

    # Phase 3: Response Generation
    response_generator = ResponseGenerator(vector_db_api_key="your_pinecone_api_key", llm_api_key="your_openai_api_key")
    response = response_generator.respond_to_user(query_embedding, processed_query_data["level"])

    # Output the final response
    print("\nIntelligent Tutor Response:")
    print(response)

if __name__ == "__main__":
    main()
