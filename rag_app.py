import os
from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as genai

# Step 7: Load environment variables from the .env file into Python's memory
load_dotenv()

# Read the GEMINI_API_KEY from memory. 
# Inside os.getenv(), the string must be ALL CAPS to match your .env file.
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Fail clearly if the key is missing or is still the placeholder string
if not gemini_api_key or gemini_api_key == "your_api_key_here":
    raise ValueError("CRITICAL ERROR: GEMINI_API_KEY is missing from the .env file.")

# Configure the Gemini API client with the loaded key
genai.configure(api_key=gemini_api_key)

# Initialize the FastAPI application instance
app = FastAPI(title="RAG Project Skeleton")

# Step 8: Define the health check endpoint
@app.get("/health")
def health_check():
    """
    Simple endpoint to confirm the server is running 
    and environment variables are loaded correctly.
    """
    return {
        "status": "healthy",
        "message": "Backend server is running successfully!",
        "gemini_config": "Initialized"
    }