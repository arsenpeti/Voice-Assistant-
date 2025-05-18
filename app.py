import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/")
def home():
    return "🚀 Flask server is running on Render!"


@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    resp.say("Përshëndetje! Faleminderit që na telefonuat.", language='sq')
    return Response(str(resp), mimetype='application/xml')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
