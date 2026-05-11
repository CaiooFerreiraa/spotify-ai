import unittest
from urllib.parse import urlencode
from utils.generateRandomString import generate_random_string

class TestApi(unittest.TestCase):
  REDIRECT_URI = "http://127.0.0.1:8080/callback"

  def test_login(self):
    client_id = "dfhjwegfwfgdhj"

    state = generate_random_string(16)
    scope = "user-read-private user-read-email"

    params = urlencode({
      "response_type": "code",
      "client_id": client_id,
      "scope": scope,
      "redirect_uri": self.REDIRECT_URI,
      "state": state
    })

    self.assertEqual()
