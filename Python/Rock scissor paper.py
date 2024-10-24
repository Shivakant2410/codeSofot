import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

rock = r"C:\Users\swara\Desktop\Ai_Tool01\CodeSoft\Python\roxk.png"
paper = r"C:\Users\swara\Desktop\Ai_Tool01\CodeSoft\Python\paper.png"
scissors = r"C:\Users\swara\Desktop\Ai_Tool01\CodeSoft\Python\download.png"

game_images = [rock, paper, scissors]

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw."
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose."

def display_result(user_choice, computer_choice):
    user_img = ImageTk.PhotoImage(Image.open(game_images[user_choice]))
    computer_img = ImageTk.PhotoImage(Image.open(game_images[computer_choice]))

    user_image_label.config(image=user_img)
    user_image_label.image = user_img

    computer_image_label.config(image=computer_img)
    computer_image_label.image = computer_img

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

def user_choice(choice):
    computer_choice = get_computer_choice()
    display_result(choice, computer_choice)

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

user_image_label = tk.Label(root)
user_image_label.pack(side=tk.LEFT, padx=10)

computer_image_label = tk.Label(root)
computer_image_label.pack(side=tk.RIGHT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

image_frame = tk.Frame(root)
image_frame.pack(pady=10)

rock_img = ImageTk.PhotoImage(Image.open(rock).resize((50, 50)))
paper_img = ImageTk.PhotoImage(Image.open(paper).resize((50, 50)))
scissors_img = ImageTk.PhotoImage(Image.open(scissors).resize((50, 50)))

rock_image_label = tk.Label(image_frame, image=rock_img)
rock_image_label.grid(row=0, column=0, padx=10)

paper_image_label = tk.Label(image_frame, image=paper_img)
paper_image_label.grid(row=0, column=1, padx=10)

scissors_image_label = tk.Label(image_frame, image=scissors_img)
scissors_image_label.grid(row=0, column=2, padx=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice(1))
rock_button.grid(row=1, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice(0))
paper_button.grid(row=1, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice(2))
scissors_button.grid(row=1, column=2, padx=10)

root.mainloop()