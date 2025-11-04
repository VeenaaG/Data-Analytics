print("_____Print all numbers between 1to100 divisible by 6 but not by 9_____")
for i in range(1,10):
    if i%6==0 and i%9!=0:
        print(i)
print("_____Sum of all Odd Numbers_____")
sum = 0
for i in range(1,51):
    if i % 2 != 0:
        sum += i
print(sum)
print("_____Count numbers between 1 and 200 are divisible by both 4 and 6_____")
count = 0
for i in range(1,201):
    if i%4 == 0 and i % 6==0:
        count+=1
print("Count: ",count)
print("_____Multiplication table of 1to10_____")
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
print("_____Factorial Of a Number_____")
n1 = int(input("Enter a Number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial: ", fact)
print("_____Prime Or Not_____")
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print("_____Sum Of Digits_____")
num = int(input("Enter a number: "))
sum_digits = 0

for i in str(num):
    sum_digits += int(i)

print("Sum of digits:", sum_digits)
print("_____Count how many numbers between 1 and 500 are perfect cubes")
count = 0
for i in range(1, 501):
    cube_root = round(i ** (1/3))
    if cube_root ** 3 == i:
        count += 1
print("Count of perfect cubes:", count)
print("_____Print the reverse of a number_____")
num = int(input("Enter a number: "))
temp = num
rev = 0
for i in range(len(str(num))):
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)
print("_____Print numbers from 1 to 100 but skip numbers ending with digit 5_____")
for i in range(1, 101):
    if i % 10 == 5:
        continue
    print(i)



