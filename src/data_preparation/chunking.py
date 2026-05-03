"""Document chunking utilities for medical documents."""

from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class DocumentChunker:
    """Split documents into chunks for embedding and retrieval."""
    
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 50):
        """Initialize chunker.
        
        Args:
            chunk_size: Size of each chunk in characters
            chunk_overlap: Overlap between chunks in characters
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
    def chunk_document(self, content: str, document_id: str) -> List[Dict]:
        """Split document into overlapping chunks.
        
        Args:
            content: Document content
            document_id: Unique document identifier
            
        Returns:
            List of chunks with metadata
        """
        chunks = []
        start = 0
        
        while start < len(content):
            end = start + self.chunk_size
            chunk_text = content[start:end]
            
            chunks.append({
                'text': chunk_text,
                'document_id': document_id,
                'start_char': start,
                'end_char': end
            })
            
            start += self.chunk_size - self.chunk_overlap
            
        logger.info(f"Document {document_id} chunked into {len(chunks)} chunks")
        return chunks
    
    def chunk_documents(self, documents: List[Dict]) -> List[Dict]:
        """Chunk multiple documents.
        
        Args:
            documents: List of documents with 'filename' and 'content'
            
        Returns:
            List of all chunks from all documents
        """
        all_chunks = []
        
        for doc in documents:
            chunks = self.chunk_document(
                content=doc['content'],
                document_id=doc['filename']
            )
            all_chunks.extend(chunks)
            
        logger.info(f"Total chunks created: {len(all_chunks)}")
        return all_chunks
