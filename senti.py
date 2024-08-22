from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def review_rating(string):
    scores = sid.polarity_scores(string)
    positive = scores['pos']
    negative = scores['neg']
    neutral = scores['neu']
    total = positive + negative

    if total == 0:
        return "Neutral"
    else:
        positive_percentage = (positive / total) * 100
        negative_percentage = (negative / total) * 100
        return {
            "Positive": f"{positive_percentage:.2f}%",
            "Negative": f"{negative_percentage:.2f}%"
        }

review = 'good'
result = review_rating(review)

