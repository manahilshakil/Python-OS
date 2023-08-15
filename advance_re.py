#add +1 before the number
import re
def transform_record(record):
  new_record = re.sub(r",(\d{3}-)", r",+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

#look for words with 3 or more vowels
import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiouAEIOU]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

# turn python comments into C comments
import re
def transform_comments(line_of_code):
  result = re.sub(r"(#+)(?![\"'\\n]|''')", r"//", line_of_code)
  return result

print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"

#convert number into another format
import re
def convert_phone_number(phone):
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345