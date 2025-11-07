print("_________Right Triangle__________")
for i in range(6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
print("_________Left Triangle__________")
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("________________Square_________________")
for i in range(1,4):
    for j in range(1,5):
        print("*",end=" ")
    print()
print("________________Eight Structure________________")
for i in range(7):
    for j in range(5):
        if (i in {0,3,6} and j in {1,2,3}) or (j in {0,4} and i not in {0,3,6}):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("____________Hollow Square______________")
for i in range(4):
    for j in range(4):
        if (i in {1,2} and j in {1,2}):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
print("_________Hollow Right Triangle__________")
for i in range(6):
    for j in range(1,i+1):
        if j==1 or i==6-1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("_____________Inverse Right Triangle_______________")
for i in range(7,0,-1):
    for j in range(0,7-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
print("_________Inverse Left Triangle__________")
for i in range(7,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("______________Increasing Number Triangle_______________")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("______________Decreasing Number Triangle_______________")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("___________Right Aligned Increasing Numbers_____________")
for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
print("___________Right Aligned Decreasing Numbers_____________")
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
print("___________Alphabet Triangle____________")
ch = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("____________Repeated Alphabet Triangle____________")
ch = 65
for i in range(1,6):
    for j in range(i):
        print(chr(ch),end=" ")
    print()
    ch+=1
print("____________Continuous Alphabet Triangle___________")
ch = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
