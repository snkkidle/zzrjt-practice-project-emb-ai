# This file is for functions for sentiment analysis
# import requests library
import requests

# Import json library for parsing the response text
import json

# Analyzer URL Constant
ANALYZER_URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

# Headers Constant
HEADERS = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

# Function to analyze sentiment of text, inputs a text data and outputs sentiment text
def text_to_analyze(text):
    # Prepare the input Json
    inputJson = {"raw_document" : { "text" : text }}
    
    # Make the request call
    response = requests.post(ANALYZER_URL, json = inputJson, headers = HEADERS)
    if(response.status_code == 200):
        analyzed_text = response.text
        formatted_response = json.loads(analyzed_text)
        return formatted_response['documentSentiment']['label']
    
    # Handle Exception    
    raise Exception("Something Went Wrong")