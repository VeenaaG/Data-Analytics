print("__________Reversing a given list__________")
l = [100,200,300,400,500]
print(l[::-1])
print("__________Concatenating two lists__________")
list1 = ["Hello","Madam"]
list2 = ["Dear","Sir"]
list3 = list1+list2
print(list3)
print("__________Removing empty strings from the list of strings__________")
list4=["Pen","","Pencil","Eraser","","Scale"]
for i in list4:
    if i=="":
        list4.remove("")
print(list4)
print("________________Converting String to List________________")
str1=input("Enter a String: ")
print(list(str1))
print("____________Check if a list contains an element___________")
list5=[1,2,3,'a','b','c']
n = input("Enter an element to check: ")
if n in list5:
    print(f"{n} is present in the list")
else:
    print(f"{n} is not present in the list")
print("________________Removing all elements from a list____________________")
l1=["kit",45,78.9,True]
print("Before Removing all elements",l1)
del l1
print("______________Counting the occurrence of a specific object in a list______________")
pets=['dog','cat','fish','fish','cat']
print(f"Number of cat present: {pets.count("cat")}")
print(f"Number of fish present: {pets.count("fish")}")
print("_____________Length of a list_______________")
lis=["P","A","K",78]
count=0
for i in lis:
    count+=1
print("Length of the list: ",count)
print("_____________Inserting a value at a specified index_______________")
pets.insert(3,"dog")
print(pets)
print("_____________Clone/Copy a list_______________")
a = ["Kitten",67,"Wool",4,90]
b=a.copy()
print(b)
print("_____________Extending a list_______________")
a.extend(pets)
print(a)
print("_____________Removing Duplicates from a list______________")
li = [3,2,2,1,1,1]
new_list=list(set(li))
print("List without duplicates: ",new_list)
print("__________________Finding the index of the 1st matching element____________________")
index = li.index(1)
print("Index of first matching element(1): ",index)
print("_________________Create a list of 5 numbers__________________")
numbers = [10, 20, 30, 40, 50]
print(numbers)
print("_________________Finding the length of a list___________________")
print("Length of list:", len(numbers))
print("__________________Accessing Elements using +ve and -ve indexing__________________")
numbers = [10, 20, 30, 40, 50]
print("First element (positive index):", numbers[0])
print("Last element (negative index):", numbers[-1])
print("__________________Updating__________________")
numbers = [10, 20, 30, 40, 50]
numbers[2] = 99
print("Updated list:", numbers)
print("__________________Deleting an element__________________")
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print("After deletion:", numbers)
print("_________________Appending a new element___________________")
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print("After appending:", numbers)
print("__________________Insert an element__________________")
numbers = [10, 20, 30, 40, 50]
numbers.insert(2, 25)
print("After insertion:", numbers)
print("__________________Removing an element__________________")
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print("After removing 30:", numbers)

print("_________________Removing the last element___________________")
numbers = [10, 20, 30, 40, 50]
numbers.pop()
print("After popping last element:", numbers)

print("__________________Clearing all the elements__________________")
numbers = [10, 20, 30, 40, 50]
numbers.clear()
print("After clearing:", numbers)

print("__________________Printing all the elements of a list using a for-loop__________________")
numbers = [10, 20, 30, 40, 50]
for n in numbers:
    print(n)

print("___________________Finding the sum of all elements_________________")
numbers = [10, 20, 30, 40, 50]
print("Sum:", sum(numbers))

print("__________________Finding maximum and minimum values using max() and min()__________________")
numbers = [10, 20, 30, 40, 50]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print("_________________Counting how many times an element appears___________________")
numbers = [10, 20, 30, 20, 40, 20]
print("20 appears", numbers.count(20), "times")

print("_________________Finding the index of a specific element using index()___________________")
numbers = [10, 20, 30, 40, 50]
print("Index of 30:", numbers.index(30))

print("______________Reversing a List using reverse()______________")
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("Reversed list:", numbers)

print("______________Sorting a list in ascending and descending order______________")
numbers = [50, 10, 30, 20, 40]
numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

print("______________Copying one list to another______________")
numbers = [10, 20, 30, 40, 50]
copy_list = numbers.copy()
print("Copied list:", copy_list)

print("______________Print only Even numbers of a list______________")
numbers = [10, 15, 20, 25, 30, 35]
for n in numbers:
    if n % 2 == 0:
        print(n)

print("______________Print only Odd numbers of a list______________")
numbers = [10, 15, 20, 25, 30, 35]
for n in numbers:
    if n % 2 != 0:
        print(n)
