import requests
from typing import List
from langchain_core.embeddings import Embeddings
from langchain_astradb import AstraDBVectorStore
from flipkart.data_converter import DataConverter
from flipkart.config import Config


class CustomHFEmbeddings(Embeddings):
    def __init__(self, model_name: str, token: str):
        self.model_name = model_name
        self.token = token
        self.url = f"https://router.huggingface.co/hf-inference/models/{model_name}/pipeline/feature-extraction"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # Replace newlines, which can negatively affect performance
        texts = [t.replace("\n", " ") for t in texts]
        response = requests.post(self.url, headers=self.headers, json={"inputs": texts})
        response.raise_for_status()
        return response.json()

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]


class DataIngestor:
    def __init__(self):
        self.embedding = CustomHFEmbeddings(
            model_name=Config.EMBEDDING_MODEL,
            token=Config.HF_TOKEN
        )

        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="flipkart_database",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )

    def ingest(self, load_existing=True):
        if load_existing == True:
            return self.vstore
        
        docs = DataConverter("data/flipkart_product_review.csv").convert()

        self.vstore.add_documents(docs)

        return self.vstore
