from textblob import TextBlob

def analyze_sentiment(text):
    if not isinstance(text, unicode):
        text = text.decode('utf-8')
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


def emotion_read(text):
    polarity, subjectivity = analyze_sentiment(text)
    # print("Polarity:", polarity, "Subjectivity:", subjectivity)  # test need

    if polarity > 0.75:  # very positive
        rate = 80
        volume = 0.5
    elif 0.5 < polarity <= 0.75:
        rate = 60
        volume = 0.4
    elif 0.25 < polarity <= 0.5:  # positive
        rate = 40
        volume = 0.3
    elif 0 < polarity <= 0.25:
        rate = 20
        volume = 0.2
    elif -0.25 < polarity <= 0:
        rate = 0
        volume = 0.1
    elif -0.5 < polarity <= -0.25:  # negative
        rate = -20
        volume = 0
    elif -0.75 < polarity <= -0.5:
        rate = -40
        volume = -0.1
    else:  # very negative
        rate = -60
        volume = -0.3

    return rate, volume