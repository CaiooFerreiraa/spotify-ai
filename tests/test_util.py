import unittest
import random

class TestUtils(unittest.TestCase):
  def test_generate_random_string(self, size=16):
    response = ''
    chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    max_size_chars = len(chars) - 1

    for _ in range(size):
      random_number = random.randint(0, max_size_chars)
      response += chars[random_number]

    self.assertEqual(size, len(response))


if __name__ == "__main__":
  unittest.main()