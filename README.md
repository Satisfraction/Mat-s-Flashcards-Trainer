# Mat-s-Flashcards-Trainer

Dies ist ein einfaches Programm zum Lernen von Flashcards. Es lädt Flashcards aus einer JSON-Datei und ermöglicht es dem Benutzer, durch die Karten zu navigieren und die Antworten anzuzeigen.

Voraussetzungen:
Um das Programm zu verwenden, benötigen Sie eine JSON-Datei mit Ihren Flashcards und eine Verschlüsselungsdatei.

Die JSON-Datei, flashcards.json, mit den Flashcards kann mit Mat's Flashcard Creator erstellt werden. (https://github.com/Satisfraction/Mat-s-Flashcard-Creator)

Die Verschlüsselungsdatei kann mit dem in diesem Repository enthaltenen Python-Code cryptkey.py erstellt werden.

Installation:
Laden Sie die flashcards.json-Datei und die key.txt-Datei in das Programmverzeichnis, sofern bereits vorhanden.

Erstellen Sie die key.txt-Datei, wenn Sie sie noch nicht haben, indem Sie cryptkey.py ausführen. (Diese wird zum Ver-/Entschlüsseln der score.txt Datei benötigt)

Führen Sie das Programm aus, indem Sie MatsFlashcardTrainer.py ausführen.

Verwendung:
Das Programm startet im "Learn Mode". Sie können zwischen "Learn Mode" und "Test Mode" wechseln, indem Sie auf den "Switch Mode"-Button klicken.

Im "Learn Mode" können Sie durch Ihre Flashcards navigieren, indem Sie auf den "Prev"- oder "Next"-Button klicken. Die Antwort wird durch Klicken auf die Schaltfläche "Show Answer" angezeigt.

Im "Test Mode" wird die Antwort in einem Textfeld eingegeben. Klicken Sie auf "Check Answer", um Ihre Antwort zu überprüfen. Wenn Sie richtig antworten, wird Ihre Punktzahl um eins erhöht. Sie können Ihre Punktzahl jederzeit beim beenden des Programms speichern.

Autor:
Mat's Flashcards Trainer wurde von Satisfraction entwickelt.

Lizenz:
Dieses Programm ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.
