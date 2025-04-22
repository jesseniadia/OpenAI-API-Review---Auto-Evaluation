from openai import OpenAI
import os
#print(os.getenv("OPENAI_API_KEY"))

def get_sentiment(text: list) -> list:
    
    """
    Here we're utlizing both system prompt and user prompt to optimize query responses. The function takes in a list of strings and returns a 
    list of sentiments for each string, catergorized as positive, negative, neutral or irrelevant. We use the OpenAI API to classify the 
    sentiments based on the provided text. The function will check if the input is a valid list of strings and will return an error if empty, 
    or otherwise.

    """
    # edge cases 
    
    if not text:
        return "Wrong input. text must be an array of strings."  # reutrn [] for an empyt list 
    
    if text and not all(isinstance(i,str) for i in text):
        return "Wrong input. text must be an array of strings."
        
    system_prompt = """
    You are a helpful assistant that categorizes text reviews into sentiment categories.
    The categories are: positive, neutral, negative, and irrelevant. 
    
    """

    prompt = f"""
    For each line of text in the string below, accurately categorize each of the following reviews with one word only: 'positive', 'neutral', 'negative', and 'irrelevant'. 
    Do not lie. Double check to make sure that you only generate one sentiment per review. 
    Return a frequency of 50 sentiments in total, must be either 'positive', 'neutral', 'negative', or 'irrelevant' for each review.
    Use only a one-word response per line. Do not include any numbers. {text}
    
    """

    client = OpenAI()
    response = client.chat.completions.create( 
        model = "gpt-4o-mini",
        messages = [
            {"role":"system", "content": system_prompt},
            {"role":"user", "content": prompt} #+ "\n".join(text) + "\n"
            ]
    ) 
    
    output = response.choices[0].message.content 
    print(output.split()) #used to access actual content of message
    
    stripd_list = []  # Empty List

    for line in output.strip().split("\n"):    # Loop through each line
        clean = line.strip().lower()           # Remove extra spaces
        if clean in ["positive", "negative", "neutral", "irrelevant"]:  # Extracted Senitments only 
            stripd_list.append(clean)  # Add to cleaned list
        
    return stripd_list  # Done
    
#print(get_sentiment)
