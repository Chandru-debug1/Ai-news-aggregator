import os
from dotenv import load_dotenv

load_dotenv()

MEDIASTACK_API_KEY = os.getenv("MEDIASTACK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not MEDIASTACK_API_KEY:
    raise ValueError("MEDIASTACK_API_KEY not found in .env")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")