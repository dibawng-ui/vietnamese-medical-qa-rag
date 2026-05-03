"""Load documents from raw data directory."""

import os
from pathlib import Path
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class DataLoader:
    """Load medical documents from raw directory."""
    
    def __init__(self, raw_documents_path: str):
        """Initialize data loader.
        
        Args:
            raw_documents_path: Path to raw documents directory
        """
        self.raw_documents_path = Path(raw_documents_path)
        
    def load_txt_files(self) -> List[Dict[str, str]]:
        """Load all .txt files from raw documents directory.
        
        Returns:
            List of dictionaries with 'filename' and 'content'
        """
        documents = []
        
        if not self.raw_documents_path.exists():
            logger.warning(f"Path {self.raw_documents_path} does not exist")
            return documents
            
        for txt_file in self.raw_documents_path.glob("*.txt"):
            try:
                with open(txt_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                documents.append({
                    'filename': txt_file.name,
                    'content': content
                })
                logger.info(f"Loaded: {txt_file.name}")
            except Exception as e:
                logger.error(f"Error loading {txt_file.name}: {e}")
                
        logger.info(f"Total documents loaded: {len(documents)}")
        return documents
    
    def load_pdf_files(self) -> List[Dict[str, str]]:
        """Load all .pdf files from raw documents directory.
        
        Note: Requires PyPDF2 or similar library
        """
        # TODO: Implement PDF loading with PyPDF2
        pass
