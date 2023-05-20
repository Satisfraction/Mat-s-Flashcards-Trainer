# Mat-s-Flashcards-Trainer

The "Flashcards Trainer" is a PyQt5-based desktop application that helps users learn and test their knowledge of a subject using flashcards. 

This program was created by Satisfraction and is licensed under the MIT license.

## Functionality

The application loads flashcards from a JSON file (`flashcards.json`) and displays them one by one on the screen. The flashcards file should be located in the same directory as the application. The user can then switch between "Learn Mode" and "Test Mode" to either learn the flashcards or test their knowledge using the flashcards.

In "Learn Mode", the user can view the question and answer of each flashcard by clicking on a button. In "Test Mode", the user is presented with the question of each flashcard and is expected to type in the correct answer. The application keeps track of the user's score and displays it on the screen. The user can also save their score to a file when they exit the application.

The application also requires a key file (`key.txt`) to securely store the user's score. The key file should be created using the `cryptkey.py` script provided in the repository.

## Libraries Used

The application uses the following libraries:
- cryptography
- PyQt5.QtCore
- PyQt5.QtGui
- PyQt5.QtWidgets

## Programming Language

The application is written in Python and uses object-oriented programming principles to create a class called "FlashcardsTrainer", which represents the main window of the application. The class contains various UI elements and functions that handle the logic of the application.

## Documentation and Style

The application is well-documented and adheres to PEP8 style guidelines.