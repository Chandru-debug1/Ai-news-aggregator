import streamlit as st 
import requests
import spacy
import google.generativeai as genai
from textblob import TextBlob
from datetime import datetime, timedelta
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

# Configure Gemini API
genai.configure(api_key="AIzaSyCn5TSbk7SYU1b1ADykXYvI02xzdVZyd48")

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def translate_text(text, lang):
    """Translate text to the specified language."""
    return GoogleTranslator(source='auto', target=lang).translate(text)

def process_news_content(text, lang):
    """Perform NLP on translated text for consistent multilingual output."""
    if not text:
        return {"sentiment": "Neutral", "entities": [], "keywords": [], "translated_text": ""}

    # Translate to selected language
    translated_text = translate_text(text, lang)

    # Run NLP on translated text
    doc = nlp(translated_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    keywords = [chunk.text for chunk in doc.noun_chunks]
    sentiment_score = TextBlob(translated_text).sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

    return {
        "sentiment": sentiment,
        "entities": entities,
        "keywords": keywords,
        "translated_text": translated_text
    }

def summarize_with_gemini(text, lang):
    """Summarize news using Gemini API and translate it."""
    if not text:
        return "No content available to summarize."
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Summarize in 8-10 lines: {text[:3000]}")
        summary = response.text.strip() if response and response.text else "Failed to summarize."
        return translate_text(summary, lang)
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def generate_speech(text, lang, filename="news_audio.mp3"):
    """Convert text to speech and save as an audio file."""
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename

def get_news_by_country_category_date(country, category, keyword, date):
    """Fetch news based on country, category, keyword, and date using Mediastack API."""
    MEDIASTACK_API_KEY = "46dbbb88980aabc6699a72e1be8c6ffb"
    url = f"http://api.mediastack.com/v1/news?access_key={MEDIASTACK_API_KEY}&countries={country}&categories={category}&keywords={keyword}&date={date}&limit=15"
    response = requests.get(url)
    news_data = response.json()
    return news_data.get("data", [])

# List of major countries
countries = {"United States": "us", "India": "in", "United Kingdom": "gb", "Canada": "ca", "Australia": "au", "None": ""}

# News categories
categories = ["general", "business", "entertainment", "health", "science", "sports", "technology", "politics", "world", "environment", "None"]

# Supported languages
languages = {"English": "en", "Tamil": "ta", "Telugu": "te", "Hindi": "hi"}

# Streamlit UI
st.set_page_config(page_title="AI-Powered News Aggregator", layout="wide")
st.markdown("""
    <style>
    body {
        background-image: url('https://source.unsplash.com/1600x900/?news,technology');
        background-size: cover;
    }
    .main-title {text-align: center; font-size: 36px; font-weight: bold; color: #2E86C1;}
    .sidebar .sidebar-content {background-color: #F2F3F4; padding: 20px;}
    .stButton>button {background-color: #2E86C1; color: white; font-weight: bold; border-radius: 10px;}
    .stSelectbox {border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🤖 AI-Powered News Aggregator with Multilingual Voice 🗣️</h1>", unsafe_allow_html=True)

st.sidebar.header("Select News Preferences")
selected_country = st.sidebar.selectbox("Select a country for top news:", list(countries.keys()))
selected_category = st.sidebar.selectbox("Select news category:", categories)
selected_date = st.sidebar.date_input("Select a date for news:", datetime.today() - timedelta(days=1))
selected_language = st.sidebar.selectbox("Select Language:", list(languages.keys()))

if st.sidebar.button("Get News"):
    country_code = countries[selected_country]
    category_code = selected_category if selected_category != "None" else ""
    lang_code = languages[selected_language]
    articles = get_news_by_country_category_date(country_code, category_code, "", selected_date.strftime("%Y-%m-%d"))

    if not articles:
        st.warning("No news found. Try a different country, category, or date!")
    else:
        for index, article in enumerate(articles):
            st.subheader(article["title"])
            st.write(f"**Source:** {article['source']}")
            st.write(f"**Published At:** {article['published_at']}")
            
            # NLP Processing
            nlp_results_en = process_news_content(article.get("content", "") or article.get("description", ""), "en")
            st.write(f"**Sentiment (English):** {nlp_results_en['sentiment']}")
            st.write(f"**Entities (English):** {nlp_results_en['entities']}")
            st.write(f"**Keywords (English):** {', '.join(nlp_results_en['keywords'])}")

            # Summarization
            st.write("### 📌 Summarized News")
            summary_text = summarize_with_gemini(article.get("content", "") or article.get("description", ""), lang_code)
            st.success(summary_text)
            
            # Generate and play speech
            audio_file = generate_speech(summary_text, lang_code, f"news_audio_{index}.mp3")
            st.audio(audio_file, format="audio/mp3")
            
            st.markdown(f"[Read Full News]({article['url']})")

# AI Chatbot Integration
st.sidebar.subheader("Ask AI about News")
user_query = st.sidebar.text_area("Ask a question about recent news:")
if st.sidebar.button("Ask AI"):
    response = summarize_with_gemini(user_query, "en")
    st.sidebar.write("AI Response:", response)
