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
        rate = 300
        volume = 70
    elif 0.5 < polarity <= 0.75:
        rate = 260
        volume = 50
    elif 0.25 < polarity <= 0.5:  # positive
        rate = 230
        volume = 40
    elif 0 < polarity <= 0.25:
        rate = 210
        volume = 30
    elif -0.25 < polarity <= 0:
        rate = 190
        volume = 20
    elif -0.5 < polarity <= -0.25:  # negative
        rate = 180
        volume = 10
    elif -0.75 < polarity <= -0.5:
        rate = 160
        volume = 0
    else:  # very negative
        rate = 130
        volume = -20

    return rate, volume