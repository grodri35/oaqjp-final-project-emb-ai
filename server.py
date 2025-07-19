"""
Flask application for Watson NLP Emotion Detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index():
    """
    Render the main index page with input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Endpoint to detect emotion from provided text.
    """
    text = request.get_json().get("text", "")

    # Handle empty input
    if not text.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text)

    # Handle failed emotion detection
    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    # Construct the response string
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
