print("Task1: STUDENT MARKS ANALYSIS")
students = [
    ("Alice",(85,90,78)),
    ("Bob",(75,80,82)),
    ("Charlie",(95,88,92))
]
#To print marks for each subject using nested loop
for s_name,marks_tuple in students:
    marks_output = f"{s_name:} "
    for i in range(len(marks_tuple)):
        mark=marks_tuple[i]

        marks_output+=f"Subject{i+1}: {mark} "

    if i < len(marks_tuple) - 1:
        marks_output+=","
    print(marks_output)
# To calculate average Marks
    avg_mark = sum(marks_tuple) / len(marks_tuple)
    print(f" Average Marks:{avg_mark:.2f}")
# To find Highest mark
    highest_mark = max(marks_tuple)
    print(f" Highest Mark: {highest_mark}\n")
# Adding a new student
new_student = ("David",(88,76,90))
students.append(new_student)

for s_name,marks_tuple in students:
    marks_output = f"{s_name:} "
    for i in range(len(marks_tuple)):
        mark=marks_tuple[i]

        marks_output+=f"Subject{i+1}: {mark} "

    if i < len(marks_tuple) - 1:
        marks_output+=","
    print(marks_output)

    avg_mark = sum(marks_tuple) / len(marks_tuple)
    print(f" Average MArks:{avg_mark:.2f}")

    highest_mark = max(marks_tuple)
    print(f" Highest Mark: {highest_mark}\n")

print("-"*70)
print("Task2: Grocery Store Inventory")
inventory = [
    ["Fruits",["Apple","Banana", "Mango"]],
    ["Vegetables",["Carrot","Tomato","Spinach"]],
    ["Dairy",["Milk","Cheese","Yogurt"]]
]
for c in inventory:
    c_name = c[0]
    items_list = c[1]
    print(f"Category:{c_name}")
    for item in items_list:
        print(f" -{item}")
print("-"*70)
#Add and Removing Elements
inventory[0][1].append("Orange")
inventory[1][1].remove("Spinach")
print("Inventory Updated: Orange Added to Fruits and Spinach removed from Vegetables.")
#Counting Items
print("\n---Item Count According to Category---")
for c_list in inventory:
    cat_name = c_list[0]
    i_list = c_list[1]

    item_count = len(i_list)
    print(f"The '{cat_name}' category has {item_count} items.")
#Updated Inventory
print("\n---Final Updated Inventory---")
for category_list in inventory:
    category_name = category_list[0]
    items_list=category_list[1]
    print(f"Category:{category_name}")
    for items in items_list:
        print(f" -{items}")