import random


def game(state):
    arr = ["rock", "paper", "scissors"]
    system = arr[random.randint(0, 2)]

    if state == system:
        return "Game is Draw"
    else:
        if (
            (state == "rock" and system == "paper")
            or (state == "paper" and system == "scissors")
            or (state == "scissors" and system == "rock")
        ):
            return f"You lose! the system choose {system}"
        else:
            return f"You Win! the system choose {system}"


print("WELCOME TO THE ROCK PAPER SCISSORS GAME")
print("_" * 10)

choices = {1: "rock", 2: "paper", 3: "scissors"}

while True:
    user = int(
        input("Enter your choice (0-3) \n 0. Exit\n 1. Rock\n 2. Paper\n 3. Scissors")
    )

    if user == 0:
        print("Thanks for playing")
        break
    elif user in choices:
        result = game(choices[user])
        print(result)
