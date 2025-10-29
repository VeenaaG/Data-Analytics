num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))

avg = (num1+num2+num3)/3
print("Average of three numbers: ",avg)
a = 10
b = 5
print(f"Before Swapping: a={a}, b={b}")
c = b
b = a
a = c
print(f"After Swapping: a={a}, b={b}")
l = list(input("Enter a list"))
typeOfl = type(l)
print(f"Type of the given data: {typeOfl}")
i = int(input("Enter an integer: "))
fl = float(input("Enter a float value: "))
add = i+fl
print(f"AdditionOfIntAndFloat: {add}, Type: {type(add)}")
print("GreatestOfTwoNumbers")
if (num1>num2):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
print("ComparisionOfTwoNumbers")
if (num1==num2):
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is not equal to {num2}")
print("Total and Average of 5 subject marks")
subj1=int(input("Enter a number: "))
subj2=int(input("Enter a number: "))
subj3=int(input("Enter a number: "))
subj4=int(input("Enter a number: "))
subj5=int(input("Enter a number: "))
total = subj1+subj2+subj3+subj4+subj5
average = total/5
print(f"TotalMarks:{total}, AverageOfMarks:{average}")
hours = int(input("Enter number of hours to be converted: "))
min = hours*60
print(f"HoursToMinutes: {hours}hours={min}minutes")
p = int(input("Enter the Principal Amount: "))
r = int(input("Enter Rate Of Interest"))
t = int(input("Enter the Time Period"))
si = (p*r*t)/100
print("Simple Interest: ", si)
length = int(input("Enter the Length of Rectangle"))
breadth = int(input("Enter the breadth of Rectangle"))
area = length * breadth
print("Area of Rectangle: ", area)
number = int(input("Enter a number: "))
if (number>0):
    print("The Number Of Positive")
elif (number == 0):
    print("The Number is Zero")
else:
    print("The Number is Negative")
cost = int(input("The cost of an item: "))
numOfItems = int(input("Number of items: "))
TotalCost = cost*numOfItems
print("TotalCostOfItems: ", TotalCost)
print("___________SMALL CALCULATOR__________")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
x = num1+num2
y = num1-num2
z = num1*num2
q = num1/num2
k = num1%num2
m = num1**2
v = num2**3
print("Addition:{}, Subtraction:{}, Multiplication:{}, Division:{}, Remainder:{}, SquareOfNumber:{}, CubeOfNumber:{}".format(x,y,z,q,k,m,v))





