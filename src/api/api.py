from socket import gethostname, gethostbyname
from os import getenv
from urllib.parse import urlencode
from flask import Flask, jsonify, make_response, request, redirect
from dotenv import load_dotenv
import requests
from src.utils.generateRandomString import generate_random_string
import base64
load_dotenv()

app = Flask(__name__)

HOSTNAME = gethostname()
PORT = 8080
IP = "127.0.0.1"
REDIRECT_URI = f"http://{IP}:{PORT}/callback"

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
  client_id = getenv("CLIENT_ID")

  state = generate_random_string(16)
  scope = "user-read-private user-read-email"

  params = urlencode({
    "response_type": "code",
    "client_id": client_id,
    "scope": scope,
    "redirect_uri": REDIRECT_URI,
    "state": state
  })

  return redirect(f"https://accounts.spotify.com/authorize?{params}")

@app.route("/callback", methods=["GET"])
def callback():
  redirect_uri = REDIRECT_URI

  client_id = getenv("CLIENT_ID")
  server_id = getenv("SERVER_ID")

  code = request.args.get("code") or None
  state = request.args.get("state") or None
  string_ids = f"{client_id}:{server_id}"
  encoded = base64.b64encode(string_ids.encode("utf-8")).decode("utf-8")

  if (state == None):
    redirect("/#?error=state_mismatch")
  else:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded}"
    }

    data = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers=headers,
        data=data
    )

    return jsonify(response.json()), response.status_code

    

if __name__ == "__main__":
  app.run(
    host=IP,
    port=PORT,
    debug=True
  )