import random

print("Enter your name:")
player_name = input("> ")
print(f"Hello, {player_name}", "\nPress Enter to continue" )


rating = {}



# get player's score from rating dict
player_score = rating.get(player_name, 0)

options = input().split(",")
print("Okay, let's start", "\nMake your choice: rock,paper or scissors? \n>")

while True:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input()

    if player_choice == "!exit":
        print("Bye!")
        break
    elif player_choice == "!rating":
        print(f"Your rating: {player_score}")
    elif player_choice not in options:
        print("Invalid input")
    else:
        # determine the winner
        idx = options.index(player_choice)
        half = len(options) // 2
        if computer_choice == player_choice:
            print(f"There is a draw ({computer_choice})")
            player_score += 50
        elif idx < half:
            if computer_choice in options[idx + 1:idx + half + 1]:
                print(f"Sorry, but computer chose {computer_choice}")
            else:
                print(f"Well done. Computer chose {computer_choice} and failed")
                player_score += 100
        else:
            if computer_choice in options[idx - half:idx]:
                print(f"Well done. Computer chose {computer_choice} and failed")
                player_score += 100
            else:
                print(f"Sorry, but computer chose {computer_choice}")

# update player's score in rating dict
rating[player_name] = player_score

# write updated scores to file
with open("rating.txt", "w") as f:
    for name, score in rating.items():
        f.write(f"{name} {score}\n")
