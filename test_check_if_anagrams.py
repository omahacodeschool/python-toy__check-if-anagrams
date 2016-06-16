def are_anagrams(str1, str2):
  #Create list of all characters in first string in lowercase (when applicable).
  sort1 = sorted(str1.lower())
  
  #Create list of all characters in second string in lowercase (when applicable).
  sort2 = sorted(str2.lower())
  
  #Create match variable to store result of comparing the two lists. 
  match = cmp(sort1, sort2)
  
  #If the 
  #variable resolves to 0, program returns "True" indicating the lists match exactly, otherwise
  #the program returns False.
  return True if match == 0 else False







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