# PrepPals

A Discord bot designed to help students prepare for interviews through real-time, personalized guidance. By combining open-source language models and web scraping, PrepPals delivers targeted advice and resources based on user-provided resumes or other input.

## Features
- **Custom Interview Prep:** Uses language models to tailor interview questions and suggestions.
- **Resume Analysis:** Extracts key points from resumes or other text to generate relevant feedback.
- **Web Scraping Support:** Gathers additional information from reliable sources to enhance guidance.
- **HuggingFace Embeddings + Retrieval-Augmented Generation (RAG):** Adds depth and context to responses.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/PrepPals.git

2. **Install Dependencies**
   ```bash
   cd PrepPals
   pip install -r requirements.txt

4. **Set Up Credentials**
   Create a .env file or export environment variables for your Discord Bot Token, API keys, etc.
   ```bash
   Example:
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key

5. **Run the Bot**
   ```bash
   python main.py

**Usage**
- Send messages or commands to the bot in Discord channels where it’s active.
- Attach or reference a resume or relevant text to generate specific interview questions and tips.
- Get real-time feedback, best-practice advice, and topic breakdowns for targeted prep.


