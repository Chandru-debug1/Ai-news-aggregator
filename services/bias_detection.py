bias_words = ["allegedly", "claims", "reportedly", "sources say", "unconfirmed"]

def detect_bias(text):
    if not text:
        return "Neutral"

    count = sum(word in text.lower() for word in bias_words)

    if count > 2:
        return "Biased"
    return "Neutral"