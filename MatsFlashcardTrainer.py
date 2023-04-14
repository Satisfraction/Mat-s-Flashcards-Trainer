from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import atexit
import json

# Load flashcards from JSON file
with open('flashcards.json') as f:
    flashcards = [json.loads(line) for line in f]

from cryptography.fernet import Fernet

# Load encryption key
with open('key.txt', 'rb') as f:
    key = f.read()

# Load scores from file
try:
    with open('scores.txt', 'rb') as f:
        fernet = Fernet(key)
        decrypted_scores = [int(fernet.decrypt(line.strip()).decode()) for line in f.readlines()]

        # Find highest score
        highscore = max(decrypted_scores) if decrypted_scores else 0
except (FileNotFoundError, ValueError):
    highscore = 0

# Initialize global variables
score = 0
current_card = 0
current_mode = 'Learn Mode'

# Define UI elements and functions
def show_question():
    card_label.config(text=flashcards[current_card]['question'])
    switch_button.config(text='Show Answer', command=show_answer)

def show_answer():
    card_label.config(text=flashcards[current_card]['answer'])
    switch_button.config(text='Show Question', command=show_question)

def prev_card():
    global current_card
    if current_card > 0:
        current_card -= 1
        show_question()

def next_card():
    global current_card
    if current_card < len(flashcards) - 1:
        current_card += 1
        show_question()

def switch_mode():
    global current_mode
    if current_mode == 'Learn Mode':
        current_mode = 'Test Mode'
        switch_button.config(state='disabled')
        answer_entry.config(state='normal')
        card_label.config(text=flashcards[current_card]['question'])
    else:
        current_mode = 'Learn Mode'
        switch_button.config(state='normal', text='Show Answer', command=show_answer)
        answer_entry.config(state='disabled')
        card_label.config(text='')

        mode_label.config(text=current_mode)

def check_answer():
    global score
    user_answer = answer_entry.get()
    correct_answer = flashcards[current_card]["answer"]
    if user_answer == correct_answer:
        card_label.config(text="Correct!")
        score += 1
    else:
        card_label.config(text=f"Incorrect. The correct answer is {correct_answer}.")
    answer_entry.delete(0, tk.END)
    score_label.config(text=f"Score: {score}")

def save_score_to_file(score):
    root = tk.Tk()
    root.withdraw()
    user_choice = messagebox.askyesno('Save Score', 'Do you want to save your score?')
    if user_choice:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_score = fernet.encrypt(str(score).encode())

        with open('scores.txt', 'ab') as f:
            f.write(encrypted_score + b'\n')

        with open('key.txt', 'wb') as f:
            f.write(key)

        messagebox.showinfo('Score Saved', 'Score saved successfully!')
    else:
        messagebox.showinfo('Score Not Saved', 'Score not saved.')

    root.destroy()

def exit_handler():
    save_score_to_file(score)

atexit.register(exit_handler)

def center_window(root, width=1400, height=800):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
center_window(root, 1400, 800)
root.title('Mat´s Flashcards Trainer')
root.config(bg='#f2f2f2', padx=20, pady=20)

# create a label widget to display the title
title_label = tk.Label(root, text='Welcome to\nMat´s Flashcard Trainer', font=("Verdana", 20), bg='#F3EFEF')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# create a label widget to display the actual mode
mode_label = tk.Label(root, text='Learn Mode', font=("Verdana", 14))
mode_label.grid(row=1, column=0, columnspan=3, pady=10)

# create a label widget to display the "question/answer" flashcard
card_label = tk.Label(root, text='', font=('Arial', 32), bg='#E1DADA', padx=20, pady=20)
card_label.grid(row=2, column=0, columnspan=3, pady=20)
card_label.configure(justify='center')

# create a entry widget for the answer entry
answer_entry = tk.Entry(root, state='disabled', width=40)
answer_entry.grid(row=3, column=0, columnspan=3, pady=10)
answer_entry.configure(justify='center')

# create button widget for the "previous" button
prev_button = tk.Button(root, text='Prev', command=prev_card, bg='#FFCD5C', fg='#3D3D3D', padx=10, pady=10)
prev_button.grid(row=4, column=0, pady=10)

# create button widget for the "switch" button
switch_button = tk.Button(root, text='Show Answer', command=show_answer, bg='#FFCD5C', fg='#3D3D3D', padx=10, pady=10)
switch_button.grid(row=4, column=1, pady=10)

# create button widget for the "next" button
next_button = tk.Button(root, text='Next', command=next_card, bg='#FFCD5C', fg='#3D3D3D', padx=10, pady=10)
next_button.grid(row=4, column=2, pady=10)

# create button widget for the "mode" button
mode_button = tk.Button(root, text='Switch Mode', command=switch_mode, bg='#FFCD5C', fg='#3D3D3D', padx=10, pady=10)
mode_button.grid(row=5, column=1, pady=10)

# create button widget for the "check answer" button
check_button = tk.Button(root, text='Check Answer', command=check_answer, bg='#FFCD5C', fg='#3D3D3D', padx=10, pady=10)
check_button.grid(row=6, column=0, columnspan=3, pady=10)

# create a label widget to display the actual score
score_label = tk.Label(root, text='Score: 0', font=('Gothik', 16))
score_label.grid(row=7, column=1)

# create a label widget to display the highscore
highscore_label = tk.Label(root, text=f"Highscore: {highscore}", font=('Gothik', 20))
highscore_label.grid(row=8, column=1)

# set the column weights to make the buttons appear in the center
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()
