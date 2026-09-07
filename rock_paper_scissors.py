#!/usr/bin/env python3
"""
Rock Paper Scissors - v1.0
--------------------------
A desktop Rock-Paper-Scissors game built using Tkinter.
Key Concepts Learned:
  1. Random choice generation using Python's `random` module.
  2. Managing multiple state variables for score tracking.
  3. Decoupling core game logic from UI representation.
"""

import random
import tkinter as tk

# ---- Constants ----
MOVES = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️",
}

# Win rules dictionary (key: winner, value: beaten move)
WINNING_RULES = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

# ---- Application State ----
score_player = 0
score_computer = 0
score_draws = 0


def determine_winner(player_move, computer_move):
    """
    Compares two moves and returns the result.
    Returns: "player", "computer", or "draw".
    Pure game logic decoupled from the GUI.
    """
    if player_move == computer_move:
        return "draw"
    elif WINNING_RULES[player_move] == computer_move:
        return "player"
    else:
        return "computer"


def play(player_move):
    """
    Triggered when a move button is clicked.
    1. Selects a random move for the computer.
    2. Determines the winner.
    3. Updates scores and UI labels.
    """
    global score_player, score_computer, score_draws

    computer_move = random.choice(list(MOVES.keys()))
    result = determine_winner(player_move, computer_move)

    if result == "player":
        score_player += 1
        result_text = "You Won! 🎉"
    elif result == "computer":
        score_computer += 1
        result_text = "You Lost 😅"
    else:
        score_draws += 1
        result_text = "It's a Draw! 🤝"

    move_label.config(
        text=f"You: {MOVES[player_move]}   VS   Computer: {MOVES[computer_move]}"
    )
    result_label.config(text=result_text)
    update_score_display()


def update_score_display():
    """Updates the score label with current values."""
    score_label.config(
        text=f"You: {score_player}   |   Computer: {score_computer}   |   Draws: {score_draws}"
    )


def reset_score():
    """Resets scores and UI messages to default state."""
    global score_player, score_computer, score_draws
    score_player = score_computer = score_draws = 0
    update_score_display()
    move_label.config(text="Choose your move!")
    result_label.config(text="")


# ---- Color Palette (Dark Theme) ----
COLOR_BG = "#1e1e2e"
COLOR_TEXT = "#ffffff"
COLOR_BTN = "#313244"
COLOR_RESET = "#f38ba8"
COLOR_RESET_TEXT = "#1e1e2e"

# ---- UI Setup ----
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("420x360")
window.resizable(False, False)
window.configure(bg=COLOR_BG)

title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg=COLOR_BG,
    fg=COLOR_TEXT,
)
title_label.pack(pady=(16, 8))

move_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 14),
    bg=COLOR_BG,
    fg=COLOR_TEXT,
)
move_label.pack(pady=4)

result_label = tk.Label(
    window, text="", font=("Arial", 16, "bold"), bg=COLOR_BG, fg=COLOR_TEXT
)
result_label.pack(pady=4)

# Container frame for action buttons
button_frame = tk.Frame(window, bg=COLOR_BG)
button_frame.pack(pady=16)

for move_name, emoji in MOVES.items():
    tk.Button(
        button_frame,
        text=f"{emoji}\n{move_name}",
        font=("Arial", 14, "bold"),
        width=6,
        height=3,
        bg=COLOR_BTN,
        fg=COLOR_TEXT,
        bd=0,
        activebackground=COLOR_BTN,
        relief="flat",
        command=lambda m=move_name: play(m),
    ).pack(side="left", padx=8)

score_label = tk.Label(
    window,
    text="You: 0   |   Computer: 0   |   Draws: 0",
    font=("Arial", 12),
    bg=COLOR_BG,
    fg=COLOR_TEXT,
)
score_label.pack(pady=(20, 8))

tk.Button(
    window,
    text="Reset Score",
    font=("Arial", 11, "bold"),
    bg=COLOR_RESET,
    fg=COLOR_RESET_TEXT,
    bd=0,
    relief="flat",
    command=reset_score,
).pack(pady=4)

window.mainloop()