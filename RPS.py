player_score = 0
computer_score = 0


choice = input("Rock, Paper, Scissors?")
print(choice)

while player_score and computer_score <= 3:
    if choice == "rock":
        print("Rock")
    elif choice == "paper":
        print("Paper")
    elif choice == "scissors":
        print("Scissors")
    else:
        print("Select an option")





