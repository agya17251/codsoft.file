import tkinter as tk
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to update the result and scores
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    
    if winner == "tie":
        result_text.set(result_text.get() + "\nIt's a tie!")
    elif winner == "user":
        result_text.set(result_text.get() + "\nYou win!")
        user_score += 1
    else:
        result_text.set(result_text.get() + "\nYou lose!")
        computer_score += 1
    
    score_text.set(f"Score - You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    score_text.set("Score - You: 0, Computer: 0")

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Variables to hold text for results and scores
result_text = tk.StringVar()
score_text = tk.StringVar()
score_text.set("Score - You: 0, Computer: 0")

# User score and computer score
user_score = 0
computer_score = 0

# UI Elements
tk.Label(root, text="Choose your move:", font=('Arial', 14)).pack(pady=10)

tk.Button(root, text="Rock", command=lambda: play('rock'), width=15, height=2).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play('paper'), width=15, height=2).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play('scissors'), width=15, height=2).pack(pady=5)

tk.Label(root, textvariable=result_text, font=('Arial', 12), justify='center').pack(pady=10)
tk.Label(root, textvariable=score_text, font=('Arial', 12), justify='center').pack(pady=10)

tk.Button(root, text="Reset Game", command=reset_game, width=15, height=2, bg='red', fg='white').pack(pady=20)

# Start the main loop
root.mainloop()
