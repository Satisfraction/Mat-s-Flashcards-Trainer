# Import necessary libraries
from cryptography.fernet import Fernet
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QMessageBox,
)
import atexit
import json

# Create a class for the flashcard trainer
class FlashcardsTrainer(QWidget):
    def __init__(self):
        # Initialize the QWidget
        super().__init__()
        # Set the geometry of the QWidget
        self.setGeometry(100, 100, 1000, 400)

        # Load flashcards from JSON file
        with open("flashcards.json") as f:
            self.flashcards = [json.loads(line) for line in f]

        # Load encryption key
        with open("key.txt", "rb") as f:
            self.key = f.read()

        # Load scores from file
        try:
            with open("scores.txt", "rb") as f:
                fernet = Fernet(self.key)
                decrypted_scores = [
                    int(fernet.decrypt(line.strip()).decode()) for line in f.readlines()
                ]

                # Find highest score
                self.highscore = max(decrypted_scores) if decrypted_scores else 0
        except (FileNotFoundError, ValueError):
            self.highscore = 0

        # Initialize global variables
        self.score = 0
        self.current_card = 0
        self.current_mode = "Learn Mode"

        # Define UI elements and functions
        # Create a QLabel object with text "Welcome to Mat's Flashcard Trainer"
        # Set the alignment of the label to center
        # Set the font size to 36pt, color to #333, and font weight to bold
        self.title_label = QLabel("Welcome to Mat's Flashcard Trainer")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 36pt; color: #333; font-weight: bold;")

        # Create a QLabel object with text "Learn Mode"
        # Set the font size to 18pt, color to #333, and font weight to bold
        self.mode_label = QLabel("Learn Mode")
        self.mode_label.setStyleSheet("font-size: 18pt; color: #333; font-weight: bold;")

        # Create a QLabel object with an empty text
        # Set the font size to 48pt, color to #333, background color to #FFF, border to 2px solid #333, and padding to 20px
        # Set the alignment of the label to center
        self.card_label = QLabel("")
        self.card_label.setStyleSheet("font-size: 48pt; color: #333; background-color: #FFF; border: 2px solid #333; padding: 20px;")
        self.card_label.setAlignment(Qt.AlignCenter)

        # Create a QLineEdit object for user input
        # Disable the user input
        # Set the font size to 24pt, color to #333, border to 2px solid #333, and padding to 10px
        self.answer_entry = QLineEdit()
        self.answer_entry.setEnabled(False)
        self.answer_entry.setStyleSheet("font-size: 24pt; color: #333; border: 2px solid #333; padding: 10px;")

        # Create a QPushButton object with text "Prev"
        # Set the font size to 18pt, color to #FFF, background color to #333, and padding to 10px
        # Connect the clicked signal to the prev_card function
        self.prev_button = QPushButton("Prev")
        self.prev_button.setStyleSheet("font-size: 18pt; color: #FFF; background-color: #333; padding: 10px;")
        self.prev_button.clicked.connect(self.prev_card)

        # Create a QPushButton object with text "Show Answer"
        # Set the font size to 18pt, color to #FFF, background color to #333, and padding to 10px
        # Connect the clicked signal to the show_answer function
        self.switch_button = QPushButton("Show Answer")
        self.switch_button.setStyleSheet("font-size: 18pt; color: #FFF; background-color: #333; padding: 10px;")
        self.switch_button.clicked.connect(self.show_answer)

        # Create a QPushButton object with text "Next"
        # Set the font size to 18pt, color to #FFF, background color to #333, and padding to 10px
        # Connect the clicked signal to the next_card function
        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet("font-size: 18pt; color: #FFF; background-color: #333; padding: 10px;")
        self.next_button.clicked.connect(self.next_card)

        # Create a QPushButton object with text "Switch Mode"
        # Set the font size to 18pt, color to #FFF, background color to #333, and padding to 10px
        # Connect the clicked signal to the switch_mode function
        self.mode_button = QPushButton("Switch Mode")
        self.mode_button.setStyleSheet("font-size: 18pt; color: #FFF; background-color: #333; padding: 10px;")
        self.mode_button.clicked.connect(self.switch_mode)

        # Create a QPushButton object with text "Check Answer"
        # Set the font size to 18pt, color to #FFF, background color to #333, and padding to 10px
        # Connect the clicked signal to the check_answer function
        self.check_button = QPushButton("Check Answer")
        self.check_button.setStyleSheet("font-size: 18pt; color: #FFF; background-color: #333; padding: 10px;")
        self.check_button.clicked.connect(self.check_answer)

        # Create a QLabel object with text "Score: 0"
        # Set the font size to 18pt, color to #333, and font weight to bold
        self.score_label = QLabel("Score: 0")
        self.score_label.setStyleSheet("font-size: 18pt; color: #333; font-weight: bold;")

        # Create a QLabel object with text "Highscore: {self.highscore}"
        # Set the font size to 18pt, color to #333, and font weight to bold
        self.highscore_label = QLabel(f"Highscore: {self.highscore}")
        self.highscore_label.setStyleSheet("font-size: 18pt; color: #333; font-weight: bold;")

        # Create a vertical box layout
        vbox = QVBoxLayout()
        # Add the title label to the vertical box layout
        vbox.addWidget(self.title_label)
        # Add the mode label to the vertical box layout
        vbox.addWidget(self.mode_label)
        # Add the card label to the vertical box layout
        vbox.addWidget(self.card_label)
        # Add the answer entry to the vertical box layout
        vbox.addWidget(self.answer_entry)

        # Create a horizontal box layout
        hbox = QHBoxLayout()
        # Add the previous button to the horizontal box layout
        hbox.addWidget(self.prev_button)
        # Add the switch button to the horizontal box layout
        hbox.addWidget(self.switch_button)
        # Add the next button to the horizontal box layout
        hbox.addWidget(self.next_button)
        # Add the horizontal box layout to the vertical box layout
        vbox.addLayout(hbox)

        # Add the mode button to the vertical box layout
        vbox.addWidget(self.mode_button)
        # Add the check button to the vertical box layout
        vbox.addWidget(self.check_button)
        # Add the score label to the vertical box layout
        vbox.addWidget(self.score_label)
        # Add the highscore label to the vertical box layout
        vbox.addWidget(self.highscore_label)

        # Set the layout of the QWidget to the vertical box layout
        self.setLayout(vbox)

        # Save score to file on exit
        atexit.register(self.save_score_to_file)

        # Show the QWidget
        self.show()

    # Function to show the question of the current flashcard
    def show_question(self):
        self.card_label.setText(self.flashcards[self.current_card]["question"])
        self.switch_button.setText("Show Answer")
        self.switch_button.clicked.disconnect()
        self.switch_button.clicked.connect(self.show_answer)

    # Function to show the answer of the current flashcard
    def show_answer(self):
        self.card_label.setText(self.flashcards[self.current_card]["answer"])
        self.switch_button.setText("Show Question")
        self.switch_button.clicked.disconnect()
        self.switch_button.clicked.connect(self.show_question)

    # Function to move to the previous flashcard
    def prev_card(self):
        if self.current_card < len(self.flashcards) - 1:
            self.current_card -= 1
            self.show_question()

    # Function to move to the next flashcard
    def next_card(self):
        if self.current_card < len(self.flashcards) - 1:
            self.current_card += 1
            self.show_question()

    # Function to switch between learn mode and test mode
    def switch_mode(self):
        if self.current_mode == "Learn Mode":
            self.current_mode = "Test Mode"
            self.switch_button.setEnabled(False)
            self.answer_entry.setEnabled(True)
            self.card_label.setText(self.flashcards[self.current_card]["question"])
        else:
            self.current_mode = "Learn Mode"
            self.switch_button.setEnabled(True)
            self.switch_button.setText("Show Answer")
            self.switch_button.clicked.disconnect()
            self.switch_button.clicked.connect(self.show_answer)
            self.answer_entry.setEnabled(False)
            self.card_label.setText("")
        self.mode_label.setText(self.current_mode)

    # Function to check the user's answer
    def check_answer(self):
        user_answer = self.answer_entry.text()
        correct_answer = self.flashcards[self.current_card]["answer"]
        if user_answer == correct_answer:
            self.card_label.setText("Correct!")
            self.score += 1
        else:
            self.card_label.setText(
                f"Incorrect. The correct answer is {correct_answer}."
            )
        self.answer_entry.clear()
        self.score_label.setText(f"Score: {self.score}")

    # Function to save the user's score to a file
    def save_score_to_file(self):
        user_choice = QMessageBox.question(
            self,
            "Save Score",
            "Do you want to save your score?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if user_choice == QMessageBox.Yes:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encrypted_score = fernet.encrypt(str(self.score).encode())

            with open("scores.txt", "ab") as f:
                f.write(encrypted_score + b"\n")

            with open("key.txt", "wb") as f:
                f.write(key)

            QMessageBox.information(
                self, "Score Saved", "Score saved successfully!"
            )

        else:
            QMessageBox.information(
                self, "Score Not Saved", "Score not saved."
            )

    # Function to save the user's score to a file when the window is closed
    def closeEvent(self, event):
        self.save_score_to_file()
        event.accept()

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    flashcards_trainer = FlashcardsTrainer()
    app.exec_()

