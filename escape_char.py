#s for whitespace w for alpha numeric and underscores
import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

#\d for matching digits,
# \s for matching whitespace characters like space, tab or new line,
# \b for word boundaries
pattern_for_username = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(r"^A.*a$","Australia"))
print(re.search(pattern_for_username,"_minahhh"))

#starts with an uppercase letter, followed by lowercase letter,space ends with .?!
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]+[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True