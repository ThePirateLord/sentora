from flask import Flask, render_template, request, redirect, url_for, flash
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Implement your sentiment analysis logic here
    # Get the input text from the form: request.form['text']
    # Perform sentiment analysis and return the result
    # Example:
    text_to_analyse = request.form['text']
    blob = TextBlob(text_to_analyse)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        result = 'Positive'
    elif polarity < 0:
        result = 'Negative'
    else:
        result = 'Neutral'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

