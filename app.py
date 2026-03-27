import streamlit as st
from services.news_service import get_news
from services.sentiment_service import analyze_sentiment
from services.summarizer_service import summarize
from services.translation_service import translate
from services.audio_service import text_to_speech
from services.bias_detection import detect_bias
from services.fake_news_model import predict_fake_news

st.set_page_config(page_title="AI News Aggregator", layout="wide")

st.title("🧠 AI News Aggregator")

category = st.selectbox("Select Category", ["technology", "business", "sports", "health"])
language = st.selectbox("Translate to", ["en", "ta", "hi"])

news_data = get_news(category)

if news_data and "data" in news_data:
    for article in news_data["data"][:5]:
        title = article["title"]
        description = article["description"] or ""

        st.subheader(title)
        st.write(description)

        # Sentiment
        sentiment = analyze_sentiment(description)
        st.write(f"**Sentiment:** {sentiment}")

        # Bias Detection
        bias = detect_bias(description)
        st.write(f"**Bias:** {bias}")

        # Fake News Prediction
        fake = predict_fake_news(description)
        st.write(f"**Fake News:** {fake}")

        # Summary
        if st.button(f"Summarize: {title}"):
            summary = summarize(description)
            st.success(summary)

        # Translation
        if st.button(f"Translate: {title}"):
            translated = translate(description, language)
            st.info(translated)

        # Audio
        if st.button(f"🔊 Play Audio: {title}"):
            file = text_to_speech(description)
            st.audio(file)

        st.markdown("---")