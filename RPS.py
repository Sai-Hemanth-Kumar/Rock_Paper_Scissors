import random
options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice, please try again.")
        continue
    computer_choice = random.choice(options)
    print("You chose " + user_choice + " and the computer chose " + computer_choice + ".")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")
    play_again = input("Do you want to play again? (yes/no) : ").lower()
    if play_again != "yes":
        break