print("Wlcome to this app:) ")

print("if you want to run out, type -1. ")

x = input("stu name: ")
y = input("stu family: ")

grades = float(input("Please enter first stu grades: "))

counter = 1

while 1 == 1 :
    new_input = float(input("Please enter next stu grades: "))
    if new_input != -1 :
        grades = grades + new_input
        counter = counter + 1
    else :
        print(x, y, "average is: ", grades/counter)
        break