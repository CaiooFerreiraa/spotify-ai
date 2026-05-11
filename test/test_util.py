import unittest
import random

class TestUtils(unittest.TestCase):
  def test_generate_random_string(self, size=16):
    response = ''
    chars = "1234567890!@#$%&qwertyuiopasdfghjklzxcvbnm=QWERTYUIOPASDFGHJKLZXCVBNM"
    max_size_chars = len(chars)

    for _ in range(size):
      random_number = random.randint(1, max_size_chars)
      response += chars[random_number]

    self.assertEqual(size, len(response))


if __name__ == "__main__":
  unittest.main()