import random

user_score = 0
computer_score = 0

print("This game is repeated five times between you and the system, and the winner is the one who has the most point 🎁 ")

while user_score < 5 and computer_score < 5:

    x = random.randint(1, 3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    else : 
        computer_choice = "scissor"

    user_choice = input("rock, paper or scissor? ")

    print("💻:", computer_choice )
    print("👩🏻‍🚀:", user_choice )

    if computer_choice == "rock" and user_choice == "rock" :
        print("same choice:) ")
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif computer_choice == "rock" and user_choice == "paper" :
        user_score = user_score + 1
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif computer_choice == "rock" and user_choice == "scissor" :
        computer_score = computer_score + 1

    elif computer_choice == "paper " and user_choice == "rock" :
        computer_score = computer_score + 1
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif  computer_choice == "paper " and user_choice == "paper" :
        print("same choice:) ")
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif  computer_choice == "paper " and user_choice == "scissor" :
        user_score = user_score + 1
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)

    elif  computer_choice == "scissor" and user_choice == "rock" : 
        user_score = user_score + 1
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif  computer_choice == "scissor" and user_choice == "paper" :
        computer_score = computer_score + 1
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)
    elif  computer_choice == "scissor" and user_choice == "scissor" :
        print("same choice:) ")
        print("💻 :", computer_score, "👩🏻‍🚀 :", user_score)

print(user_score, computer_score)

if user_score > computer_score :
    print("You win 😎🚬")
elif  user_score < computer_score :
    print("You lose 😝")
else :
    print("You have the same score, if you want play again:) ")
