
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

class QueryRequest(BaseModel):
    question: str

def validate_user_input(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    if len(text) < 5:
        raise HTTPException(
            status_code=400,
            detail="Question is too short"
        )

    if len(text) > 500:
        raise HTTPException(
            status_code=400,
            detail="Question is too long"
        )

def validate_model_output(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(
            status_code=500,
            detail="AI returned an empty response"
        )

    if len(text) < 10:
        raise HTTPException(
            status_code=500,
            detail="AI response is too short"
        )

def review_model_output(original_answer: str):

    review_prompt = f"""
You are reviewing an AI-generated response.

Your job:
- If the response is unclear, incomplete, or poorly written, improve it.
- If the response is already good, return it unchanged.

AI response to review:

{original_answer}
"""

    review_model = genai.GenerativeModel("gemini-2.5-flash")

    review_response = review_model.generate_content(
        review_prompt
    )

    return review_response.text

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
        outline_prompt = """
        Create a short outline explaining what a large language model is.

        Use 3-5 bullet points.
        """

        outline_response = model.generate_content(outline_prompt)
        
        outline = outline_response.text
        
        print("Generated Outline:")
        print(outline)

        expand_prompt = f"""
        Using the outline below, write a detailed explanation.

        Outline:
        {outline}
        """
        
        final_response = model.generate_content(expand_prompt)
        
        final = final_response.text
        
        print("Generated Expansion:")
        print(final_response.text)

        return {
            "response": final_response.text
            }
    except Exception as e:
        # This syntax is clean and will print the raw error directly to your console
        print("DEBUG GEMINI ERROR:", str(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
            )

@app.post("/query")
def query_ai(request: QueryRequest):

    validate_user_input(request.question)

    primary_model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    primary_response = primary_model.generate_content(
        request.question
    )

    raw_answer = primary_response.text

    validate_model_output(raw_answer)

    reviewed_answer = review_model_output(
        raw_answer
    )

    return {
        "question": request.question,
        "answer": reviewed_answer
    }