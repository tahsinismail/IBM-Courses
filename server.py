from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect:
        return "Invalid text! Please try again!"
    else:
        response = emotion_detector(text_to_detect)
        if response['dominant_emotion'] == None:
            return "Invalid text! Please try again!"
        else:
            return (
                f"For the given statement, the system response is 'anger': {response['anger']} "
                f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
                f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
                f"The dominant emotion is {response['dominant_emotion']}.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)