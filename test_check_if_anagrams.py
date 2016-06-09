def are_anagrams(str1, str2):
  list1 = list(str1.lower())
  list2 = list(str2.lower())
  list1.sort()
  list2.sort()
  var = cmp(list1, list2)

  if var == 0:
    return True
  else:
    return False
  

# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_simple_anagram():
  string1 = "ah"
  string2 = "ha"
  assert are_anagrams(string1, string2)

def test_complex_anagram():
  string1 = "senator"
  string2 = "treason"
  assert are_anagrams(string1, string2)

def test_anagram_with_numbers():
  string1 = "c378ty6op"
  string2 = "py7tc6o38"
  assert are_anagrams(string1, string2)

def test_empty_strings():
  string1 = ""
  string2 = ""
  assert are_anagrams(string1, string2)

def test_anagram_with_capital_letters():
  string1 = "sEaRcH"
  string2 = "chaser"
  assert are_anagrams(string1, string2)

def test_barely_not_an_anagram():
  string1 = "bird"
  string2 = "drip"
  assert are_anagrams(string1, string2) == False

def test_not_an_anagram():
  string1 = "dismiss"
  string2 = "excavate"
  assert are_anagrams(string1, string2) == False