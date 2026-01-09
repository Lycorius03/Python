from bank import value

def test_hello():
  assert value("hello, world") == 0
  assert value("HELLO") == 0
  assert value("hELLo,world") == 0

def test_h():
  assert value("hi, bro") == 20
  assert value("Hi") == 20
  assert value("HEY") == 20

def test_nothing():
  assert value("abababa") == 100

def test_space():
  assert value("   hello world ") == 0

def test_punctation():
  assert value("!hello") == 100

def test_numbers():
  assert value("111hi") == 100