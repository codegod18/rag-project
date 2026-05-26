
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv(dotenv_path="./.env")

# Read the GEMINI_API_KEY from memory
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Fail clearly if the key is missing or is still the placeholder string
if not gemini_api_key or gemini_api_key == "your_api_key_here":
    raise ValueError("CRITICAL ERROR: GEMINI_API_KEY is missing from the .env file.")

# Configure the Gemini API client with the loaded key
genai.configure(api_key=gemini_api_key)

# Initialize the FastAPI application instance
app = FastAPI(title="RAG Project Skeleton")

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Backend server is running successfully!",
        "gemini_config": "Initialized"
    }

# Week 5: First Backend API + Gemini Call
@app.get("/test-gemini")
def test_gemini():
    """
    Initializes a Gemini model, sends a hardcoded prompt, 
    and returns the generated text response.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = "Explain what a large language model is in one paragraph."
        response = model.generate_content(prompt)
        
        return {
            "prompt": prompt,
            "response": response.text
        }
        
    except Exception as e:
        # This syntax is clean and will print the raw error directly to your console
        print("DEBUG GEMINI ERROR:", str(e))
        raise HTTPException(
            status_code=500, 
            detail="An error occurred while generating content from Gemini."
        )