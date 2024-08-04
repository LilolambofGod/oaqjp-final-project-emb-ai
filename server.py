''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : 
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created: 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''define the function '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
   
    # Check if the emotion_prediction is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
        # Return a formatted string with the sentiment label and score
    else:
        return "For the given statement, the system response is {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
