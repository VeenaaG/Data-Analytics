print("_____Printing numbers from 1 to 20_____")
for i in range(1,21):
    print(i)
print("_____Printing all even numbers from 2 to 50_____")
for i in range(2,51,2):
    print(i)
print("_____Printing all odd numbers from 1 to 50_____")
for i in range(1,50,2):
    print(i)
print("_____Printing square of numbers from 1 to 15_____")
for i in range(1,16):
    print(i*i)
print("_____Printing cube numbers from 1 to 10_____")
for i in range(1,11):
    print(i*i*i)
print("_____Printing numbers from 10 down to 1 in reverse order_____")
for i in range(10,0,-1):
    print(i)
print("_____Multiplication Table of 5_____")
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
print("_____Printing All Characters of a string one by one_____")
string = "ScopeTechSolutions"
for i in string:
    print(i)
print("_____Printing Numbers divisible by 3 between 1 and 30_____")
for i in range(1,31):
    if i%3==0:
        print(i)