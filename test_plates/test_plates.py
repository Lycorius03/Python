from plates import is_valid

def test_heads_two():
  assert is_valid("114514") == False

def test_longth():
  assert is_valid("L") == False
  assert is_valid("Lycorius") == False

def test_check_illegal():
  assert is_valid("Lyc 5") == False

def test_head_zero():
  assert is_valid("Lyc07") == False

def test_numbers_position():
  assert is_valid("Lyc5c") == False

def test_correct():
  assert is_valid("Lyc555") == True