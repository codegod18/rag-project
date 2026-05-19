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


