import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    if computer_pick == user_input:
        print("you both chose the {}".format(computer_pick))
        continue
    print("Comtuper picked {}.".format(computer_pick))
    
    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins +=1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("computer won!")
        computer_wins +=1
    
    else:
        print("you lost!")
        computer_wins +=1

print("your score: {}".format(user_wins))
print("computer score: {}".format(computer_wins))



print("Bye")