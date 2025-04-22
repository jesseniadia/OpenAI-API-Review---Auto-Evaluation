# Review Processing

You are a growth analyst at a Vancouver-based consulting firm called [Bernardino Group](https://en.wikipedia.org/wiki/Bernardino_of_Siena#:~:text=Saint%20Bernardino%20is%20the%20Roman,problems%20involving%20the%20chest%20area.). Your manager is spear-heading the completion of a new analytical tool which will automatically label if a review is positive, neutral, negative, or irrelevant (aka [sentiment](https://en.wikipedia.org/wiki/Sentiment_analysis)). The release schedule for this product is ambitious as your company would like to be able to advertise this service to potential clients as soon as possible. You will be kicking off the completion of this first milestone by independently implementing a minimal-viable product. This will be a Python pipeline that ingests review data and interfaces with the Open AI API to automatically label each review.

For example, if you were checking the reviews for a wearable ring from SengLinks that tracks heart rate, the following would be examples of the mentioned sentiment:
* positive: *I love this ring, I use it all the time when working out.*
* neutral: *It's an ok ring. Some features could be better but for the price it's fine.*
* negative: *Absolutely terrible ring. The green light that the ring emitted kept attracting mosquitos.*
* irrelevant: *I like strawberry ice cream because its the best.* 

You are tasked with creating a minimal pipeline that reads a JSON file of reviews and generates an output file that contains one of these sentiment labels for each respective review.

For example, if your input file contains the following array of reviews:
```

[
 "this ring smells weird, don't recomend",
 "I love this ring, I use it all the time when working out.",
 "I will never buy another brand again, I love this ring",
 "It's an ok ring. Some features could be better but for the price its fine.",
 "its a ring",
 "Bought this ring and it came broken. rip-off."
]
```

Your program would output the following list of labels:
```
["negative", "positive", "positive", "neutral", "irrelevant", "negative"]
```

Your company has provided you with a sample of real-world reviews that they've received from customers from 1999-2012 on coconut water. These reviews are listed in the JSON file labeled `reviews.json`

Your company has also provided you an API key **(which you must keep secret)** to interface with this API. You will again utilize test-driven development to complete this project.

**Note** To limit cost anomalies throughout this project, we've set up API restrictions that limit the entire data science cohort to 1500 requests-per-day, 100 requests-per-minute, and 40,000 tokens-per-minute. If you encounter a `429` error when you run your code, this could either mean that your prompt is over the allotted 40,000 tokens or there have been too many requests within the same minute. Please read the section titled **API Limitations** to find out how to work around these limitations.

## Instructions

### Setup

To work on this project you must first configure your `ds` conda environment by following the listed steps below. By the end of these steps, you will have a functioning environment that contains your hidden API key. Please follow these instructions closely or your project will not function correctly.

1) Activate your conda environment via the following terminal command:
```bash
conda activate ds
```

2) Confirm that you see the `(ds)` prompt at the beginning of your environment.

3) Once you've confirmed that you are in your environment, set your given API key to a conda environment variable using the terminal command below:

```bash
conda env config vars set OPENAI_API_KEY="your_api_key"
```

4) Deactivate and reactive your environment by running the following commands in your terminal
```bash
conda deactivate ds
conda activate ds
```

5) Next, install the `openai` package by running the following pip command:
```bash
pip install openai
```

6) Run the `test_package.py` module to check if your openai package is functioning correctly.
```bash
python test_package.py
```

You should see your terminal output `SUCCESS!`. 

These instructions have been based off of documentation from the [OpenAI API](https://platform.openai.com/docs/libraries?desktop-os=windows&language=python). 

There are three Python files and one markdown file which you will modify in this repository to complete this project:
* cleaner.py
* metrics.py
* main.py
* writeup.md

The files with the prefix test_ (i.e. test_package.py, test_label.py, test_visualize.py, and test_run.py) are intended for you to test your code to ensure that all project requirements are complete. Do not modify the code in these files. Otherwise, you will not be able to check that your code is functioning correctly.

Lastly, remove any **ellipses** or **pass** keywords that you come across in your code. These are placeholder values.

### label.py

This module contains a function that you will implement to interface with the `gpt-4o-mini` language model. It will take in a list of string reviews, and pass this list to the open ai API via the `chat.completions.create()` method.

While the `prompt` variable has been created for you, you will generate your own `system_prompt` which will influence the large-language-models output. Use the following [guide](https://platform.openai.com/docs/guides/prompt-engineering) to determine your system prompt. Some general tips from this guide include:
* Provide examples to help the model generate correct labels
* Provide helpful context-setting (e.g. "You are an expert in interpreting human sentiment across cultures.")

Since this prompt will most likely be a multi-line string, we recommend using triple-quoted strings to generate this prompt.

This function will return the output of the large language model expressed as a list of sentiments with no extraneous blank lines (ex: `["positive", "positive", "negative", ...]`)

However, this function should return a string that states `"Wrong input. text must be an array of strings."` if an empty list is provided or if a list containing incorrect data-types is passed. 

To test this module, open a terminal in VSCode. Go to the Terminal tab in the top menu and select "New Terminal." Then run the following command:

```
python test_label.py
```

We recommend working on this module **first**. Be sure to write up a docstring when you've completed this function!

**Note**: You are limited to working with the `gpt-4o-mini` model. If you utilize any other model, your API call will not function correctly.

### visualize.py

This module contains a function that you will implement to count how many times each sentiment (`positive`, `neutral`, `negative`, and `irrelevant`) appears, which you will then plot as an appropriate data visualization. Be sure to save this image into the folder titled `images/`. Look back to your notes to determine which plot you should use for this analysis.

This function is not required to return any values. Be sure to complete the docstring for this function as well.

To test this module, run the following command in your terminal:

```
python test_visualize.py
```

**Note**: Ensure that any images this function generates are saved within the `images/` folder.

### main.py

This module will utilize all the functions you've written to run a comprehensive pipeline in one function named `run()`. Note that your initial data is a `JSON` object, so you must determine the appropriate file i/o and dictionary operations to access the list of reviews within this object.

This function will return the list of sentiments you've generated from your OpenAI API call.

To test this module on your available data files, you will run the following command in your terminal:

```
python test_run.py
```

### writeup.md

This file contains 3 analytical questions you will answer based on the visualizations your code generates.

## API Limitations

As each API call entails a cost based on token size, we've limited the number of tokens that our project can process in one minute, as well as the number of requests that we can make in one minute as well as in one day.

If you are encountering a `429` error, read the error message carefully to determine which next actions you should take. If your error message mentions:

**Tokens-Per-Minute (TPM) (40,000 limit)**

Then you should:
* Potentially modify your system prompt so that your input string size is greatly less than 40,000 tokens and the output token size is minimal (50 tokens).
* Wait one minute for the token "budget" to reset as too many users are making large token submissions at once

**Requests-Per-Minute (RPM) (100 limit)**

Then you should:
* Wait one minute for the request "budget" to reset as too many users are making requests

**Requests-Per-Day (RPD) (1500 limit)**

Then you should:
* Wait till the next day for the request "budget" to reset as we've hit the limit for requests for the day.

Most importantly, this should motivate you to **only run tests when needed**. Do not make API calls unless you've ensured that all proper parameters are in place for you to receive a meaningful response from OpenAI. 

## Submission 

The due date for this project is `04/21`.

To begin work on this project, you will download this template code and push it to your GitHub repository. 

Be sure to test as you code in order to verify that your functions are working correctly. If you see that all of your tests are evaluating to a green check-mark (✅) for a specific module, that means your code is ready to go, and you can move on to the next challenge.

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

#   O p e n A I - A P I - R e v i e w - - - A u t o - E v a l u a t i o n  
 #   O p e n A I - A P I - R e v i e w - - - A u t o - E v a l u a t i o n  
 