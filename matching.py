import re
def check_aei (text):
  result = re.search(r"a.e.i", text)   #r is a raw string
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

import re
def check_punctuation (text):
  result = re.search(r"[.,!?;:'\"]$", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

import re
result = re.search(r"the","the cow jumps over the moon")