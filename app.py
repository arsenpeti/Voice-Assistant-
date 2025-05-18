from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/")  # ✅ This is the new main route
def home():
    return "🚀 Flask server is running!"


@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    resp.say("Përshëndetje! Faleminderit që na telefonuat.", language='sq')
    return Response(str(resp), mimetype='application/xml')


if __name__ == "__main__":
    app.run(port=5000)
