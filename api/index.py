import sys
from pathlib import Path

# Add backend folder to Python path
BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

# Import the FastAPI application
from backend.main import app