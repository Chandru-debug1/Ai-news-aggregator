import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample dataset (replace with real dataset)
data = pd.read_csv("data/dataset.csv")

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data["text"])

model = LogisticRegression()
model.fit(X, data["label"])

with open("models/fake_news.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained and saved!")