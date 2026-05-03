"""Vector store for semantic search and retrieval."""

import logging
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class VectorStore:
    """Store and retrieve document chunks using embeddings."""
    
    def __init__(
        self,
        model_name: str = "sentence-transformers/distiluse-base-multilingual-case-sensitive-v2",
        persist_directory: str = "data/embeddings/"
    ):
        """Initialize vector store.
        
        Args:
            model_name: Embedding model name from HuggingFace
            persist_directory: Directory to save embeddings
        """
        self.model_name = model_name
        self.persist_directory = persist_directory
        self.model = SentenceTransformer(model_name)
        self.embeddings = {}
        self.documents = {}
        
    def add_documents(self, chunks: List[Dict]) -> None:
        """Add document chunks to vector store.
        
        Args:
            chunks: List of chunks with 'text' and metadata
        """
        texts = [chunk['text'] for chunk in chunks]
        
        logger.info(f"Creating embeddings for {len(texts)} chunks...")
        chunk_embeddings = self.model.encode(texts, show_progress_bar=True)
        
        for chunk, embedding in zip(chunks, chunk_embeddings):
            chunk_id = f"{chunk['document_id']}_{chunk['start_char']}"
            self.embeddings[chunk_id] = embedding
            self.documents[chunk_id] = chunk
            
        logger.info(f"Added {len(chunks)} chunks to vector store")
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search for relevant chunks using semantic similarity.
        
        Args:
            query: Search query
            top_k: Number of top results to return
            
        Returns:
            List of top-k most similar chunks
        """
        query_embedding = self.model.encode(query)
        
        # Simple cosine similarity search
        similarities = {}
        for chunk_id, embedding in self.embeddings.items():
            # Compute cosine similarity
            similarity = sum(a*b for a, b in zip(query_embedding, embedding)) / (
                sum(a**2 for a in query_embedding)**0.5 * sum(b**2 for b in embedding)**0.5
            )
            similarities[chunk_id] = similarity
        
        # Get top-k
        top_chunks = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:top_k]
        
        results = [
            {
                'chunk': self.documents[chunk_id],
                'similarity': similarity
            }
            for chunk_id, similarity in top_chunks
        ]
        
        return results
