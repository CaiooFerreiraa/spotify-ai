import random

def generate_random_string(size: int):
  response = ''
  chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
  max_size_chars = len(chars) - 1
  
  for _ in range(size):
    random_number = random.randint(0, max_size_chars)
    response += chars[random_number]

  return response