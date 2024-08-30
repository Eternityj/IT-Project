from textblob import TextBlob


def analyze_sentiment(text):
    if not isinstance(text, unicode):
        text = text.decode('utf-8')
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


def emotion_read(text):
    polarity, subjectivity = analyze_sentiment(text)
    print("Polarity:", polarity, "Subjectivity:", subjectivity)  # test need

    if polarity > 0.75:  # very positive
        rate = 280
        volume = 90
    elif 0.5 < polarity <= 0.75:
        rate = 240
        volume = 80
    elif 0.25 < polarity <= 0.5:  # positive
        rate = 210
        volume = 70
    elif 0 < polarity <= 0.25:
        rate = 190
        volume = 60
    elif -0.25 < polarity <= 0:
        rate = 170
        volume = 50
    elif -0.5 < polarity <= -0.25:  # negative
        rate = 160
        volume = 40
    elif -0.75 < polarity <= -0.5:
        rate = 140
        volume = 30
    else:  # very negative
        rate = 130
        volume = 20

    return rate, volume

def A(text):
    polarity, subjectivity = analyze_sentiment(text)
    print("Polarity:", polarity, "Subjectivity:", subjectivity)  # test need


    if polarity > 0.75:
        rate = 320
        volume = 90
    elif 0.5 < polarity <= 0.75:
        rate = 300
        volume = 80
    elif 0.25 < polarity <= 0.5:
        rate = 270
        volume = 70
    elif 0 < polarity <= 0.25:
        rate = 240
        volume = 60
    elif -0.25 < polarity <= 0:
        rate = 210
        volume = 50
    elif -0.5 < polarity <= -0.25:
        rate = 180
        volume = 40
    elif -0.75 < polarity <= -0.5:
        rate = 160
        volume = 30
    else:
        rate = 140
        volume = 20

    return rate, volume

