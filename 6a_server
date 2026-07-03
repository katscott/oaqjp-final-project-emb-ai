from flask import Flask, render_template, request
import EmotionDetection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    result = EmotionDetection.emotion_detector(text_to_analyze)

    anger_score = result.get("anger")
    disgust_score = result.get("disgust")
    fear_score = result.get("fear")
    joy_score = result.get("joy")
    sadness_score = result.get("sadness")
    dominant_emotion = result.get("dominant_emotion")

    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(debug=True)
