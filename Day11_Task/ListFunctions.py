print("_____________Adding Two Lists_____________")
l=["good",123,89]
l1=[56,"friend",7]
l2=l+l1
print(l2)

print("_____________Repeating list elements_____________")
l3=l*3
print(l3)

print("_____________Check if an element exists in a list_____________")
li=[50,78,95,25,90]
num=int(input("Enter a number to check: "))
if num in li:
    print(f"{num} exists in the list")
else:
    print(f"{num} not found in the list")

print("_____________Slicing a list_____________")
l5=[1,2,3,4,5,6,7,8,9]
print(l5[:3])
print(l5[-3:])

print("_____________Largest of Two Numbers in a List_____________")
li.sort()
print("Two Largest numbers are: ",li[-1],"and",li[-2])

print("_____________Finding Duplicate elements in a list_____________")
l6=[1,2,3,2,1,4,7,5]
duplicates=[]
for i in l6:
    if l6.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate Elements: ",duplicates)

print("_____________Remove duplicate elements from a list_____________")
unique=[]
for i in l6:
    if i not in unique:
        unique.append(i)
print("List after removing duplicates:", unique)

print("_____________List of Square Numbers from 1 to 10_____________")
squares=[]
for i in range(1,11):
    squares.append(i**2)
print("Squares from 1 to 10: ",squares)
print("_____________Separate even and odd numbers into two lists_____________")
even=[]
odd=[]
for i in l6:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers: ",even)
print("Odd Numbers: ",odd)
print("_____________Finding Common Elements between two lists_____________")
lis1=[1,2,3,4,5]
lis2=[4,5,6,7]
common=[]
for i in lis1:
    if i in lis2:
        common.append(i)
print("Common elements: ",common)
print("_____________Finding Elements present in one list but not in another_____________")
diff=[]
for i in lis1:
    if i not in lis2:
        diff.append(i)
print("Elements in list1 but not in list2:",diff)
print("_____________Removing all occurrences of a specific element from a list_____________")
liss=[1,2,3,2,4,2,5]
x=2
while x in liss:
    liss.remove(x)
print("List after removing all",x,":",liss)
print("_____________Converting a list into a tuple_____________")
print("List: ",l2)
print("Tuple: ",tuple(l2))
print("_____________Finding the Average of list elements_____________")
avg=sum(li)/len(li)
print("Average: ",avg)
print("_____________Counting positive,negative, and zero numbers in a list_____________")
li3=[10,-5,0,3,-2,-1,0,8,9]
p=n=z=0
for i in li3:
    if i>0:
        p+=1
    elif i<0:
        n+=1
    else:
        z+=1
print("Positive: ",p)
print("Negative: ",n)
print("Zero: ",z)
print("_____________Finding product of all elements in a list_____________")
li4=[2,3,4,5]
prod=1
for i in li4:
    prod*=i
print("Product of elements: ",prod)