num1=int(input("Enter a number: "))
print("_____Positive/Zero/Negative_____")
if num1>0:
    print("The number is positive")
elif num1==0:
    print("The number is zero")
else:
    print("The number is negative")
print("_____Odd Or Even_____")
if num1%2 == 0:
    print(num1," It's an Even Number")
else:
    print(num1," Its an Odd number")
print("_____Eligible To Vote_____")
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You aren't eligible to vote")
print("_____Pass/Fail_____")
mark = int(input("Enter your Mark: "))
if mark>=35:
    print("You've passed the Examination")
else:
    print("You've failed the Examination")
print("_____Largest Of Two Numbers_____")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("Both the numbers are equal")
print("_____Displaying Grades_____")
m = int(input("Enter your Total Marks out of 100: "))
if 90>m and m<=100:
    print("Grade A")
elif 70>m and m<=90:
    print("Grade B")
elif 50>m and m<=70:
    print("Grade C")
elif 35>m and m<=50:
    print("Grade D")
else:
    print("Fail")
print("_____Day Name Based on Numbers_____")
number = int(input("Enter a number from 1-7 to predict the day of week: "))
if number==1:
    print("Sunday")
elif number==2:
    print("Monday")
elif number==3:
    print("Tuesday")
elif number==4:
    print("Wednesday")
elif number==5:
    print("Thursday")
elif number==6:
    print("Friday")
elif number==7:
    print("Saturday")
else:
    print("Invalid Number, enter number from 1 to 7")
print("_____Alphabet/Digit/Special_Character_____")
s = input("Enter a character: ")
if s.isalpha():
    print(f"{s} is an alphabet")
elif s.isdigit():
    print(f"{s} is a digit")
else:
    print(f"{s} is a special character")
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
print("_____Temperature_____")
temp = input("Enter the temperature type: ")
if temp == "Hot":
    print("Stay Hydrated")
elif temp == "Warm":
    print("Make some smoothies and cold coffees")
elif temp == "Cool":
    print("Take a nap, have some fries!")
elif temp == "Cold":
    print("Don't forget to put on your sweater")
else:
    print("Invalid Temperature")
print("_____Positive and Even_____")
p = int(input("Enter a number: "))
if p>0:
    if p%2==0:
        print("The Number is positive and even")
    else:
        print("It's an odd number")
else:
    print("It's neither a positive number nor an even number")
print("_____Login System_____")
username = input("Enter your name: ")
password = input("Enter your password: ")
u = "Merlin"
p = "12345"
if u == username:
    if p == password:
        print("Login was successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")
print("_____Eligible For Job or Not_____")
age = int(input("Enter your age: "))
exp = input("Do you have experience (type yes/no): ")
if age>18:
    if exp == "yes":
        print("You are eligible for the job")
    else:
        print("You must have experience")
else:
    print("You must be above 18")
print("_____Leap year or not_____")
y = int(input("Enter a year: "))
if (y%4==0):
    if(y%100 != 0) or (y%400 == 0):
        print(f"{y} is a Leap Year")
    else:
        print(f"{y} is not a Leap year")
else:
    print(f"{y} is not a Leap year")
print("_____Qualification for Scholarship_____")
marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))
if marks>85:
    if attendance>=90:
        print("You Qualify for the scholarship!")
    else:
        print("You need at least 90% attendance")
else:
    print("You need at least 85 marks")

