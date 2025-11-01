print("_____Data Types_____")
x = input("Enter a string: ")
y = int(input("Enter an integer: "))
c = float(input("Enter a decimal: "))
d = bool(input("Enter a boolean: "))
e = list(input("Enter a list: "))
print(f"{x} is a {type(x)}")
print(f"{y} is a {type(y)}")
print(f"{c} is a {type(c)}")
print(f"{d} is a {type(d)}")
print(f"{e} is a {type(e)}")
print("_____Variables_____")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My Name is {name} and my age is {age}.")
print("_____Sum,Diff,Prod,Quotient_____")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(f"Sum of {num1} and {num2} is: {num1+num2}")
print(f"Difference of {num1} and {num2} is: {num1-num2}")
print(f"Product of {num1} and {num2} is: {num1*num2}")
print(f"Quotient of {num1} and {num2} is: {num1/num2}")
print("_____Combining String and Integer_____")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My Name is {name} and my age is {age}.")
print("_____Arithmetic Operators_____")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
avg = (n1+n2+n3)/3
print(f"Square of {n1} is: {(n1**2)}")
print(f"Cube of {n2} is: {(n2**3)}")
print(f"Average of {n1,n2,n3} is: {avg}")
print("_____Relational Operators_____")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("a > b: ", a>b)
print("a < b: ", a<b)
print("a == b: ", a==b)
print("a != b: ",a!=b)
print("a >= b: ", a>=b)
print("a <= b: ", a<=b)
print("_____Logical Operators_____")
if n1>0 and n1%2==0:
    print("The number is positive and even")
elif n1<0 or n1==0:
    print("The number is either negative or zero")
else:
    print("The number is odd")
print("_____Swapping Two Variables using Arithmetic Operator_____")
print(f"Before Swapping a:{a}, b:{b}")
a = a+b
b = a-b
a = a-b
print(f"After Swapping a:{a}, b:{b}")
print("_____Greater/Equal_____")
if n1>n2:
    print(f"{n1} is greater than {n2}")
elif n2>n1:
    print(f"{n2} is greater than {n1}")
else:
    print(f"{n1} is equal to {n2}")
print("_____Even/Odd_____")
if num1%2 == 0:
    print(num1," It's an Even Number")
else:
    print(num1," Its an Odd number")
print("_____Positive/Zero/Negative_____")
if num1>0:
    print("The number is positive")
elif num1==0:
    print("The number is zero")
else:
    print("The number is negative")
print("_____Displaying Grades_____")
m = int(input("Enter your Total Marks out of 100: "))
if 90>=m:
    print("Grade A")
elif 75>m and m<=89:
    print("Grade B")
elif 50>m and m<=74:
    print("Grade C")
else:
    print("Fail")
print("_____Leap year or not_____")
y = int(input("Enter a year: "))
if (y%4==0):
    if(y%100 != 0) or (y%400 == 0):
        print(f"{y} is a Leap Year")
    else:
        print(f"{y} is not a Leap year")
else:
    print(f"{y} is not a Leap year")
print("_____Eligible To Vote_____")
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print(f"{18-age} years are left to become eligible.")
print("_____Largest Among Three Numbers_____")
n1 = int(input("Enter a Number: "))
n2 = int(input("Enter a Number: "))
n3 = int(input("Enter a Number: "))
if (n1>=n2) and (n1>=n3):
    largest = n1
elif (n2>=n1) and (n2>=n3):
    largest = n2
else:
    largest = n3
print(f"The Largest among the three is {largest}")
print("_____Positive and Even_____")
p = int(input("Enter a number: "))
if p>0:
    if p%2==0:
        print("The Number is positive and even")
    else:
        print("It's an odd number")
else:
    print("It's neither a positive number nor an even number")
print("_____Age Classification_____")
age = int(input("Enter your age: "))
if age<13:
    print("Child")
else:
    if age<= 19:
        print("Teen")
    else:
        if age<=59:
            print("Adult")
        else:
            print("Senior Citizen")
print("_____Vowel/Consonant_____")
ch = input("Enter an alphabet: ")
vowel = ['a','e','i','o','u','A','E','I','O','U']
if ch in vowel:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Please enter a valid alphabet")
print("_____Pass/Fail_____")
s1 = int(input("Enter your Maths Mark: "))
s2 = int(input("Enter your Science Mark: "))
s3 = int(input("Enter your Social Mark: "))
total = s1+s2+s3
if s1>=40 and s2>=40 and s3>=40:
    print("Pass")
    avg = total/3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")



