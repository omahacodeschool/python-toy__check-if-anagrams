def are_anagrams(str1, str2):
  # Make sure all characters in both strings are lowercase
  str1 = str1.lower()
  str2 = str2.lower() 
  # Create 2 empty lists
  l1 = []
  l2 = []
  # Add each character of srt1 to one of the empty lists and each character of 
  # str2 to the other empty list
  for i in str1:
	  l1.append(i)
  for i in str2:
	  l2.append(i)
  # Sort the lists so that the elements are in alphabetical order
  l1.sort()
  l2.sort()
  # See if the 2 lists are equal
  return l1==l2

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