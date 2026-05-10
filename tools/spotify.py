import urllib.error
import urllib.request
from langchain.tools import tool

@tool
def list_music_for_gender(gender: str):
  """Lista 5 músicas do gênero do usuário
  
  Args:
    gender: Gênero do usuário
  """

@tool
def list_music_for_artist(artist: str):
  ...

@tool
def indicate_music(gender: str):
  ...

@tool
def list_playlist(user: str):
  ...


  