# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, conditionals, and user input. Students will practice controlling program flow while creating a simple interactive game.

## 📝 Tasks

### 🛠️ Game Setup and Guessing Logic

#### Description
Create the core Hangman game loop. The program should choose a secret word, prompt the player to guess letters, and reveal the current progress as the game continues.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the player
- Show the hidden word using an `_ _ _` style display
- Prevent already-guessed letters from being counted again

### 🛠️ Win and Loss Handling

#### Description
Add the game-ending rules and feedback so the player knows when the round is over.

#### Requirements
Completed program should:

- Track incorrect guesses remaining
- End the game when the word is fully guessed or attempts run out
- Display a win message when the player solves the word
- Display a lose message that reveals the secret word
