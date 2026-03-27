import pickle

# Load trained model + vectorizer
with open("models/fake_news.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict_fake_news(text):
    if not text:
        return "Unknown"

    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]

    return "Fake" if prediction == 1 else "Real"