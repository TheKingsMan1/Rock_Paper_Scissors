import random

while True:
    user_choice = ["rock", "paper", "scissors"]
    possible_choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choice)
    print(f"Choose a item : {possible_choice}")
    if user_choice == computer_choice:
        print(f"\nYou choosed {user_choice}, computer choose {computer_choice}!, It's ties.\n")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("rock smashes scissors!, You win")
        else:
            print(" , You lose")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper rock!, You win")
        else:
            print(" , You lose")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("scissors cut peper!, You win")
        else:
            print(" , You lose")
    
    play_again = input("Play again ? (y/n)")
    if play_again.lower() != "y":
        break