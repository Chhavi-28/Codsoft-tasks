#ROCK PAPER SCISSOR GAME
import random
print("🪨📄✂️ ......Welcome to Rock Paper Scissor Game.....🪨📄✂️")
choices = ['rock', 'paper', 'scissor']
user_wins = 0
computer_wins = 0
rounds = int(input("Enter number of rounds you want to play: "))
for round in range(rounds):
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("You win this round!")
        user_wins += 1
    else:
        print("Computer wins this round!")
        computer_wins += 1
print(f"Score after {rounds} rounds - You: {user_wins}, Computer: {computer_wins}")
if user_wins > computer_wins:
    print("Congratulations! You won the game! 🎉")
elif user_wins < computer_wins:
    print("Computer won the game! Better luck next time! 🤖")
else:
    print("The game is a tie! 🤝")
print("Thank You For Playing Rock Paper Scissor Game 🪨📄✂️")
