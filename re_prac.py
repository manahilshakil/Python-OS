import re
result = re.search(r"the","the cow jumps over the moon")
print(result)

print(re.search(r"[a-z]way","the end of the highway"))

print(re.search(r"cat|dog","a sentence with cats."))

#defining a function that finds code and returns it as a string value
list = re.findall(r"[0-9]","your passcode is 38928")
def code_finder(list):
    code = " "
    for num in list:
        code += str(num)

    print(code)

code_finder(list)