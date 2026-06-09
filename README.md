# RAG Project

This repository contains my Retrieval-Augmented Generation (RAG) project for the GenAI Secure Coding course.
This project will be built incrementally each week.

## Week 4 Setup & Progress
This week, I successfully initialized the core backend skeleton for the RAG application and established secure environment handling.
* **Environment Configuration:** Set up a hidden `.env` file to securely store the `GEMINI_API_KEY` away from the public repository.
* **API Client Initialization:** Configured the `google-generativeai` SDK to authenticate safely using local environment variables.
* **Health Check Verification:** Verified the active backend server using the FastAPI local testing endpoint.

## Purpose of `rag_app.py`
The `rag_app.py` file serves as the main entry point and backbone of our backend server. Its primary purposes are:
1. **Securely Loading Configurations:** Utilizing `python-dotenv` to inject environment variables into memory at runtime, preventing accidental hardcoded API key leaks.
2. **Application Routing:** Initializing the `FastAPI` instance and managing server endpoints (such as the `/health` route) that handle web requests.
3. **API Client Lifecycle:** Acting as the bridge that safely instantiates and configures the Google Gemini API client before handling data operations.

## Git Commands Used So Far
* `git clone`
* `git status`
* `git add`
* `git commit`
* `git push`
* `git pull` (Used to reconcile remote changes and resolve branch divergences)
* `git stash` / `git stash pop` (Used to safely manage local changes during merge conflicts)

---

## Week 5 — First Backend API + Gemini Call
This week, I successfully integrated the Google Generative AI SDK with FastAPI to execute a live AI text generation call entirely server-side.

* **What `/test-gemini` does:** This endpoint securely triggers a backend call to Google's infrastructure using a hardcoded prompt ("Explain what a large language model is in one paragraph.") and returns the model's text output as a structured JSON object.
* **Where the Gemini call lives:** The entire model initialization, execution, and text-extraction lifecycle is encapsulated safely inside the `test_gemini()` endpoint function inside `rag_app.py`.
* **What I learned from documentation:** I learned how the `google-generativeai` library uses `genai.GenerativeModel` to instantiate a model environment. I also discovered that older model versions (like `gemini-1.5-flash`) have been updated in production environments, requiring a migration to `gemini-2.5-flash` to execute successful API handshakes.

### Questions or Uncertainties
* None! The security architecture keeping the API key hidden on the server while exposing clean JSON to the client makes complete sense. Ready for Week 6 chunking and data embedding!

## Week 6 Multi-Step Execution

The `/test-gemini` endpoint now performs two sequential Gemini calls.

### Step 1
Generate a short outline explaining a large language model.

### Step 2
Use the generated outline to create a more detailed explanation.

The output from the first call is stored in a variable and passed into the second call. This demonstrates multi-step execution and control flow within the backend.

## Week 7 — Validating User Input and AI Output

This week, I enhanced the AI application by adding validation steps before and after the model generates a response. Input validation ensures that users provide meaningful questions before any AI processing occurs. Requests that are empty, too short, or excessively long are rejected immediately, preventing unnecessary API calls and improving overall reliability.

I also implemented output validation to verify that the AI returns a useful response before it is sent back to the user. Responses that are empty or obviously inadequate are caught and handled appropriately. In addition, I added a second Gemini model call that reviews the first model’s answer. This reviewer model is responsible for improving unclear or incomplete responses and returning higher-quality output when necessary. Together, these validation and review steps demonstrate how real-world AI systems use multiple layers of quality control to produce safer, more reliable results.
