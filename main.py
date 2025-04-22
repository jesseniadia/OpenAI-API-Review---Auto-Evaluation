from label import get_sentiment
from visualize import make_plot

import json

def run(filepath: str):
    """
    Function to run main.py takes a file path as input and reads JSON reviews file, extracts sentiments, 
    returns a list of strings for each review and vizualizes distribution of sentiments.
    
    Args: filepath (str): JSON file path containing reviews.
    
    Returns:
        list: Function returns a list of sentiments generated from our OpenAI API call.
    """
    # open the json object
    with open (filepath, "r") as file:
        data = json.load(file) # converts JSON object data into Python dictionary

    # extract the reviews from the json file
    cus_rev_list = data["results"] #check if data is empty

    # get a list of sentiments for each line using get_sentiment
    real_sentiments = get_sentiment(cus_rev_list)
        
    # plot a visualization expressing sentiment ratio
    make_plot(real_sentiments)
    
    # return sentiments
    return real_sentiments 

if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
    