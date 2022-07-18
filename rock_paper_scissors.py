import random

while True:
    user_action = input("Enter a choice : rock, paper, scissors : ")
    possible_choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choice)
    print(f"You chose {user_action} and cuputer choose {computer_choice}")
    if user_action == computer_choice:
        print(f"\nBoth players selected {user_action}!, It's ties.\n")
    elif user_action == "rock":
        if computer_choice == "scissors":
            print("rock smashes scissors!, You win")
        else:
            print("Paper cover rock, You lose")
    elif user_action == "paper":
        if computer_choice == "rock":
            print("paper covers rock!, You win")
        else:
            print("scissors cuts peper , You lose")
    elif user_action == "scissors":
        if computer_choice == "paper":
            print("scissors cuts peper!, You win")
        else:
            print("rock smashes , You lose")
    
    play_again = input("Play again ? (y/n)")
    if play_again.lower() != "y":
        break