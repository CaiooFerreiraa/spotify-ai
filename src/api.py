from socket import gethostname, gethostbyname
from os import getenv
from flask import Flask, jsonify, make_response, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

HOSTNAME = gethostname()
PORT = 8080
IP = gethostbyname(HOSTNAME)

@app.route("/health", methods=["GET"])
def health_server():
    return make_response(
        jsonify({
            "status": "online",
        }),
        200
    )

@app.route("/message", methods=["POST"])
def send_message(msg: str):
  ...

@app.route("/auth", methods=["POST", "GET"])
def authorization_user():
  ...

@app.route("/login", methods=["GET"])
def login():
  client_id = getenv.CLIENT_ID
  redirtect_url = f"http://{IP}:{PORT}/callback"


@app.route("/callback", methods=["GET"])
def callback():
  ...

if __name__ == "__main__":

    app.run(
        host=IP,
        port=PORT,
        debug=True
    )