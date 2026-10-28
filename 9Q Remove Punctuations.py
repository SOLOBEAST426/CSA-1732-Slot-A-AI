import string

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print("String without punctuation:", result)
