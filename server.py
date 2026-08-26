''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
# Import the sentiment_analyzer function from the package created
# Import the json library for formatting

from flask import Flask, render_template, request
from custanalysis.SentimentAnalysis import text_to_analyze
import json

# Initiate the flask app
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Extract text 
    text = request.args.get('textToAnalyze')

    # Pass only if text is not empty
    if(text):
        # Call our Method else throw Exception 
        try:
            analyzed_text = return text_to_analyze(text)
            formatted_response = json.loads(analyzed_text)
            return formatted_response['documentSentiment']['label']
        except Exception as e:
            return {"Error": "Something Went Wrong"}, 400    

    # Handle Exception if text is empty  
    return {"Error": "Empty String found"}, 422    

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug = True)
