from twttr import shorten

def test_lowercase():
  assert shorten("adieu") == "d"

def test_uppercase():
  assert shorten("ADIEU") == "D"

def test_numbers():
  assert shorten("test1") == "tst1"

def test_punctuation():
  assert shorten("Hello, world!") == "Hll, wrld!"