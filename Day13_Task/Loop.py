print("Printing Prime Numbers between 1 and 100")
count=0
for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,end=" ")
        count+=1
print("\nTotal prime numbers =",count)
print("-"*70)
print("Pyramid Number Pattern")
rows=5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
print("-"*70)
print("Electricity Bill Calculator")
units = int(input("Enter units consumed: "))
if units < 100:
    rate = 1.5
elif units <= 200:
    rate = 2.5
elif units <= 300:
    rate = 4.0
else:
    rate = 5.0
bill = units * rate
if bill > 1000:
    bill += bill * 0.10
print(f"Total Bill: ₹{bill}")
print("-"*70)
print("Diamond Star Pattern")
n = 5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
print("-"*70)
print("Multiplication Table (1-10)Grid")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end="")
    print()
print("-"*70)
print("Pascal's Triangle")
n = int(input("Enter a number of rows: "))
for i in range(n):
    print(" "*(n-i),end="")
    num = 1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j) // (j+1)
    print()