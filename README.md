# LPITutor

**Steps for Execution**
Set Up the Vector Database:

Create an index named "intelligent_tutor" on Pinecone (or your chosen vector database) before running the script.
Phase 1: Document Processing:

Place your PDF files in the ./pdf_files directory.
Run document_processing.py to process the PDFs, generate embeddings, and upload them to the vector database.
User Input:

Run main.py.
Enter your question when prompted.
Specify the level (beginner, intermediate, or expert) as per your requirement.
Phase 2: Query Processing:

The query will be preprocessed, and an embedding will be generated for similarity matching in the vector database.
Phase 3: Response Generation:

The system will fetch the most relevant responses from the vector database.
The selected context and user-specified level will be sent to the GPT model for a detailed answer.
The response will be displayed on the console.
