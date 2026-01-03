Project: AI‑Powered News Aggregator with Multilingual Voice
🔹 Overview
This project is a Streamlit web application that fetches news articles from the Mediastack API, processes them with NLP (spaCy + TextBlob), summarizes content using Google Gemini API, translates into multiple languages, and generates speech output using gTTS.
Features include:
- 🌍 Country & category‑based news filtering
- 🧠 NLP analysis (sentiment, entities, keywords)
- ✨ AI summarization with Gemini
- 🌐 Multilingual translation (English, Tamil, Telugu, Hindi)
- 🗣️ Text‑to‑speech audio playback
- 💬 Sidebar chatbot for news queries

🔹 Requirements
Install dependencies from requirements.txt:
streamlit==1.39.0
requests==2.32.3
spacy==3.7.2
google-generativeai==0.8.3
textblob==0.18.0
gTTS==2.5.3
deep-translator==1.11.4


Additionally, download the spaCy English model:
python -m spacy download en_core_web_sm



🔹 Setup Instructions
- Clone or download this project folder.
- Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
- Install dependencies:
pip install -r requirements.txt
- Configure API keys:
- Gemini API: Add your Google Generative AI key in genai.configure(api_key="YOUR_KEY").
- Mediastack API: Add your Mediastack key in MEDIASTACK_API_KEY.

🔹 Running the App
Start the Streamlit server:
streamlit run app.py


Then open the local URL (usually http://localhost:8501) in your browser.

🔹 Usage
- Select country, category, date, and language from the sidebar.
- Click Get News to fetch and process articles.
- View sentiment, entities, keywords, and AI‑generated summaries.
- Listen to audio summaries in your chosen language.
- Use the Ask AI section to query Gemini about recent news.

🔹 Notes
- Ensure you have a stable internet connection (for APIs and translation).
- Audio files (news_audio_X.mp3) are generated locally in the project folder.
- The app uses Unsplash background images for styling.
