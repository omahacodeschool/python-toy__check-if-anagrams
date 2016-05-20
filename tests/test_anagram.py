from .context import lib

def test_answer():
  string1 = "search"
  string2 = "chaser"
  assert lib.are_anagrams(string1, string2)