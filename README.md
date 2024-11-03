# LPITutor

**Steps for Execution**

1) Set Up the Vector Database:

     a) Create an index named "intelligent_tutor" on Pinecone (or your chosen vector database) before running the script.

2) Phase 1: Document Processing:

   a) Place your PDF files in the ./pdf_files directory.

   b) Run document_processing.py to process the PDFs, generate embeddings, and upload them to the vector database.

3) User Input:

   a) Run main.py.
  
   b) Enter your question.
  
   c) Specify the level (beginner, intermediate, or expert) as per your requirement.

4) Phase 2: Query Processing:

   a) The query will be preprocessed, and an embedding will be generated for similarity matching.

5) Phase 3: Response Generation:

   a) The system will fetch the most relevant responses.
  
   b) The selected context and user-specified level will be sent to the GPT model for a detailed answer.
  
   c) The response will be displayed on the console.
