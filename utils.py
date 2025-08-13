# utils.py
"""
Utility functions for RAG Hybrid Eval project.
Add common helpers here for logging, file I/O, and config management.
"""

import os
import logging
from typing import Optional


def setup_logger(name: str = "rag_eval", level: int = logging.INFO) -> logging.Logger:
    """Set up a logger with a standard format."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def read_file(filepath: str) -> Optional[str]:
    """Read a text file and return its contents, or None if not found."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    """Write content to a text file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def load_env(env_path: str = ".env") -> None:
    """Load environment variables from a .env file if present."""
    if not os.path.exists(env_path):
        return
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.strip().partition('=')
                os.environ[key] = value

# Add more utility functions as needed
