import matplotlib.pyplot as plt
import os

def make_plot(sentiments: list) -> list:
    """
    Counts and plots a bar chart showing number of each sentiment type.
    - X-axis: Sentiment categories
    - Y-axis: Frequency
    - Neon-colored bars
    Returns a list:
        [sentiment_counts (dict), most_common (str), most_common_count (int)]
    Saves bar chart to 'images/custom_sentiment_counts.png'.
    """
              
    # Count each sentiment from the list
    #data =()
    pos_count = sentiments.count("positive")
    neg_count = sentiments.count("negative")
    neu_count = sentiments.count("neutral")
    irr_count = sentiments.count("irrelevant")

    # Store the counts in a dictionary
    sentiment_counts = { 
        "positive": pos_count,
        "negative": neg_count,
        "neutral": neu_count,
        "irrelevant": irr_count
    }

    # Most common sentiment
    most_common = max(sentiment_counts, key=sentiment_counts.get)
    most_common_count = sentiment_counts[most_common]

    # Color for each sentiment
    colors = ["#39FF14", "#FF073A", "#FFFF33", "#FF10F0"]

    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=colors)
    ax.set_title("Sentiment Analysis Results")
    ax.set_xlabel("Sentiment Category")
    ax.set_ylabel("Sentiment Frequency")

    # Save png.
    fig.savefig("images/custom_sentiment_counts.png")

    # Print for write-up
    print("Sentiment counts:", sentiment_counts)
    print("Most common sentiment:", most_common, "appeared", most_common_count, "times")

    return [sentiment_counts, most_common, most_common_count]

# Example input: replace with 50 review labels
sentiments = [
    "positive", "positive", "neutral", "negative", "positive",
    "irrelevant", "neutral", "positive", "positive", "negative"
]

# Capture results
results = make_plot(sentiments)

# Results for write-up
counts = results[0]
top_sentiment = results[1]
top_count = results[2]

