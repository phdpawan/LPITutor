import openai
from sentence_transformers import util
import pinecone

class ResponseGenerator:
    def __init__(self, vector_db_api_key, llm_api_key, model_name="gpt-3.5-turbo"):
        pinecone.init(api_key=vector_db_api_key, environment='us-west1-gcp')
        self.index = pinecone.Index("intelligent_tutor")
        openai.api_key = llm_api_key
        self.model_name = model_name

    def fetch_answer(self, query_embedding):
        results = self.index.query(query_embedding, top_k=5, include_metadata=True)
        return results['matches']

    def generate_response(self, matches, level):
        context = " ".join([match["metadata"]["sentence"] for match in matches])
        prompt = f"Answer this question at a {level} level of understanding: {context}"
        
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable tutor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']

    def respond_to_user(self, query_embedding, level):
        matches = self.fetch_answer(query_embedding)
        return self.generate_response(matches, level)

if __name__ == "__main__":
    query_embedding = [0.2, 0.1, ...]  # example embedding array
    level = "beginner"
    generator = ResponseGenerator(vector_db_api_key="your_pinecone_api_key", llm_api_key="your_openai_api_key")
    response = generator.respond_to_user(query_embedding, level)
    print(response)
