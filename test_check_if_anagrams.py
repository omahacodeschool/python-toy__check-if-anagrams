def are_anagrams(string1, string2):
  # I initially thought about the possibility of having to compare each possible iteration of the string.  That sounded ridiculous if the strings are long.
  # Strings don't sort easily, it seems.  Could i turn the strings into lists?
  #note: make them all the same size.  Was getting error if it is a list?
  # I had a problem when just trying to modify the strings as is, so giving them a new object name helps
  lowerstring1 = string1.lower()
  lowerstring2 = string2.lower()
  string_1 = list(lowerstring1)
  string_2 = list(lowerstring2)
  # sort them?
  string_1.sort()
  string_2.sort()
  if string_1 == string_2:
    return True
  else:
    return False
 # This is not what I would consider pretty code, but it passes all the tests!
 # I ran into a lot of problems.  I made two version of the code that would work correctly for all False returns
 # I initially tried to sort them while as strings, that didn't work either! I had to look up how to split it up, and that is when I read up enough to know that lists might be the way to go.
 

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