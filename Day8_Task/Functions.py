print("______Concatenate two Strings______")
s1=input("Enter a string: ")
s2=input("Enter a string: ")
s=s1+s2
print("concatenate string:",s)
print("______To check if a given string contains specified sequence of char values______")
a1=input("Enter a string: ")
a2=input("Enter characters to check: ")
if a2 in a1:
    print(f"{a1} contains {a2}")
else:
    print(f"{a1} doesn't contain {a2}")
print("______To convert all charactrers in a string to lower case______")
string = input("Enter to UpperCase string: ")
print(string.lower())
print("______To Trim any leading or trailing whitespace from a given string______")
s3 = input("Enter a string: ")
print(s3.strip())
print("______To Reverse a String______")
s4 = input("Enter a String: ")
print(s4[::-1])
print("______To Replace all spaces with underscore______")
s5 = input("Enter a String: ")
g = s5.replace(" ","_")
print(g)
print("______To Create a string made of the middle three characters______")
s6 = input("Enter a String: ")
mid = len(s6)//2
h = s6[mid -1: mid +2]
print(h)
print("______To Convert the First and Last letter to capital______")
sr = input("Enter a string: ")
result = ''.join([char for char in sr if not char.isdigit()])
print("String after removing digits:", result)
print("______Length of the string______")
s7 = "Hello World"
print("Length of string:", len(s7))
print("_______To print number of occurrences of a given string with repetition_______")
text = input("Enter a String: ")
word = input("Enter a String: ")
count = text.count(word)
print(f"The word '{word}' occurs {count} times.")
print("________To count number of words in a string_________")
sp = input("Enter a String: ")
words = sp.split()
print("Number of words:", len(words))
print("______To Replace a specified character with another character_______")
spec = "The quick brown fox jumps over the lazy dog"
new_s = spec.replace("d", "f")
print("New String:", new_s)
print("_______To count vowels in a string______")
sk = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in sk if ch in vowels)
print("Number of vowels:", count)
print("____________To check if a string contains only whitespace______________")
s = "   "
if s.isspace():
    print("String contains only whitespace")
else:
    print("String has other characters")
print("____________To remove all digits from a string_____________")
s = "Th3 qu1ck br0wn f0x jum9s 0ver 7he lazy d0g"
result = ''.join([ch for ch in s if not ch.isdigit()])
print("After removing digits:", result)
print("______________To Convert a given string to uppercase using upper()________________")
s = "hello world"
print(s.upper())
print("___________Convert a given string to lowercase using lower()__________")
s = "HELLO WORLD"
print(s.lower())
print("___________Count how many times the letter “a” appears in a string using count()______")
s = "Banana"
print(s.count("a"))
print("___________Check if a string starts with the word “Hello” using startswith()___________")
s = "Hello everyone"
print(s.startswith("Hello"))
print("______________Check if a string ends with “.com” using endswith()______________")
s = "example@gmail.com"
print(s.endswith(".com"))
print("____________Find the position of the word “Python” using find()____________")
s = "I am learning Python programming"
print(s.find("Python"))
print("_________Replace the word “Java” with “Python” using replace()___________")
s = "I love Java programming"
print(s.replace("Java", "Python"))
print("________Remove extra spaces from both sides using strip()________")
s = "   Hello World   "
print(s.strip())
print("____________Capitalize the first letter using capitalize()______________")
s = "python is fun"
print(s.capitalize())
print("___________Split a sentence into words using split()__________")
s = "Python is a great language"
print(s.split())
print("_________Join a list of words using join()___________")
words = ["Python", "is", "fun"]
print(" ".join(words))
print("___________Check if a string has only alphabets using isalpha()___________")
s = "Hello"
print(s.isalpha())
print("__________Check if a string has only numbers using isdigit()___________")
s = "12345"
print(s.isdigit())
print("____________Check if a string has both letters and numbers using isalnum()____________")
s = "abc123"
print(s.isalnum())
print("____________Check if all characters are in lowercase using islower()____________")
s = "hello"
print(s.islower())
print("___________Check if all characters are in uppercase using isupper()__________")
s = "HELLO"
print(s.isupper())
print("___________Swap lowercase to uppercase and vice versa using swapcase()__________")
s = "PyThOn"
print(s.swapcase())
s = "PyThOn"
print(s.swapcase())
print("_________Convert every word’s first letter to uppercase using title()___________")
s = "python string methods"
print(s.title())
print("_________Check if a string contains only spaces using isspace()__________")
s = "   "
print(s.isspace())
print("____________Count the number of vowels in a string____________")
s = "Beautiful day"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowels:", count)
print("__________Check if a given word is a palindrome_________")
s = "madam"
print(s == s[::-1])
print("__________Remove all digits from a given string_________")
s = "Th3 qu1ck br0wn f0x"
print(''.join([ch for ch in s if not ch.isdigit()]))
print("_________Replace all spaces in a sentence with underscores________")
s = "Python is fun"
print(s.replace(" ", "_"))
print("_________Extract only numbers from a mixed string___________")
s = "abc123xyz456"
digits = ''.join([ch for ch in s if ch.isdigit()])
print(digits)
print("__________Find and print words that start with a capital letter__________")
s = "This is a Test Sentence With Capitals"
for word in s.split():
    if word[0].isupper():
        print(word)
print("_________Count how many times each letter occurs________")
s = "banana"
for ch in sorted(set(s)):
    print(ch, ":", s.count(ch))
print("__________Remove all punctuation marks from a sentence__________")
import string
s = "Hello!!! How are you???"
clean = ''.join(ch for ch in s if ch not in string.punctuation)
print(clean)
print("____________Check if an email ends with “@gmail.com”_____________")
email = "example@gmail.com"
print(email.endswith("@gmail.com"))
print("_______Reverse a given string without using slicing______")
s = "Python"
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)
