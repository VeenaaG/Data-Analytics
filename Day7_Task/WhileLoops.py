print("_____Print Numbers from 10 down 1_____")
i = 10
while i>=1:
    print(i)
    i-=1
print("_____Sum Of Even Digits_____")
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum += digit
    num //= 10
print("Sum of even digit: ",sum)
print("_____Counting digits in a number_____")
n1 = int(input("Enter a number: "))
count = 0
while n1>0:
    n1 //= 10
    count += 1
print("Number of Digits: ", count)
print("_____Palindrome_____")
n2 = int(input("Enter a number: "))
t = n2
rev = 0
while n2>0:
    digit = n2%10
    rev = rev * 10 + digit
    n2//=10
if t == rev:
    print(t,"is a palindrome number")
else:
    print(t, "is not a palindrome number")
print("____Reverse of a number_____")
n3 = int(input("Enter a number: "))
r = 0
while n3>0:
    digit = n3 % 10
    r = r * 10 + digit
    n3//=10
print("Reversed Number: ",r)
print("_____Fibonacci Series Upto 100_____")
a,b = 0,1
while a<=100:
    print(a)
    a,b = b,a+b
print("_____Power of a number_____")
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
count = 0
while count < exp:
    result *= base
    count += 1
print(f"Power of the given number= {result}")
print("_____Count Divisions_____")
n4 = int(input("Enter a number: "))
count = 0
while n4 >= 1:
    n4/=2
    count+=1
print("Number of divisions: ",count)
print("_____Print the digits from last to first_____")
n5 = int(input("Enter a Number: "))
while n5>0:
    digit = n5 % 10
    print(digit)
    n5//=10
print("_____Sum of Squares of digit_____")
n6 = int(input("Enter a number: "))
sum = 0
while n6>0:
    digit = n6%10
    sum += digit**2
    n6//=10
print("Sum of squares of digit: ",sum)

