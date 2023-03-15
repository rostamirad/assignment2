import random

while True :
    print("enter + for roll the dice and - for exit:")
    x = input()
    if x == "+" :
        cube_face = random.randint(1, 6)
        print("🎲 : ", cube_face)
        if cube_face == 6 :
            print("You win! 🎉")
            y = input("enter + for your prize:) ")
            if y == "+":
                z = random.randint(1, 6)
                print("Your prrize is 🎲 : ", z)

    elif x == "-" :
        break

