import random

computer_number  = random.randint(10, 40)

for i in range(15) :

    user_number = int(input("enter your guess: "))

    if computer_number == user_number:
        print("You win 🎉 ")
        print("you wwin after", i, "try")
        break

    elif computer_number > user_number :
        print("go up! 👆🏽")

    elif computer_number < user_number :
        print("go down 👇🏽 ")

