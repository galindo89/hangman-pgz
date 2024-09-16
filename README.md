# Hangman Game

A simple command-line Hangman game implemented in Python. The player guesses letters to figure out a randomly chosen word before they run out of attempts. The game features user-friendly interaction, error handling, and a win/loss message upon completion. This project is aimed at demonstrating basic Python skills such as loops, conditionals, and file handling.

## CONTENTS

- [Hangman Game](#hangman-game)
  - [CONTENTS](#contents)
  - [Introduction](#introduction)
    - [Purpose of the project](#purpose-of-the-project)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Game Flow](#game-flow)
    - [Features](#features)
      - [Core Features](#core-features)
      - [Future Implementations](#future-implementations)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment on Heroku](#deployment-on-heroku)

## Introduction

### Purpose of the project

The purpose of this project is to build a simple command-line game of Hangman in Python, where a user attempts to guess a word one letter at a time. The game provides feedback on each guess, tracks the number of incorrect guesses, and ends when the player either successfully guesses the word or runs out of attempts.

This project showcases basic programming constructs such as loops, conditionals, functions, and error handling in Python.

## User Experience (UX)

### User Stories

- As a user, I want to start a game and have a randomly chosen word to guess.
- As a user, I want feedback on each guess to see if I’m correct or incorrect.
- As a user, I want to know how many incorrect guesses I have remaining.
- As a user, I want the game to end and display whether I won or lost.
- As a user, I want the option to play again once the game ends.

## Design

### Game Flow

The game starts by loading a list of words from a file. A word is randomly chosen, and the user is prompted to guess letters. Each correct guess reveals the positions of the letter in the word, while each incorrect guess reduces the number of remaining attempts. The game ends when the word is fully guessed or the player runs out of attempts.

### Features

#### Core Features

- **Random Word Selection:** A random word is chosen from a list in `words.txt`.
- **Guessing Letters:** Users can input letters one by one to try and guess the word.
- **Feedback on Guesses:** Correct letters are revealed, and incorrect guesses are tracked.
- **Endgame Messages:** The game displays a win or loss message when the game ends.
- **Replay Option:** After the game ends, the user is given the option to play again.

#### Future Implementations

- Add difficulty levels with different word lengths and numbers of attempts.
- Implement ASCII art for the hangman to visually represent incorrect guesses.
- Add categories for words (e.g., animals, countries) to choose from before starting the game.

## Technologies Used

### Languages Used

- **Python 3.** The entire project is written in Python using basic programming constructs such as loops, functions, and conditionals.

### Frameworks, Libraries & Programs Used

- **Python's `random` module:** To randomly select a word from the list.
- **Python’s built-in `open()` function:** To read the words from the `words.txt` file.
- **Heroku:** For deploying the command-line game to the cloud.
- **Command Line Interface (CLI):** The game runs directly in the terminal/command prompt.

## Deployment & Local Development

### Deployment on Heroku

The Hangman game has been deployed to Heroku, allowing users to play the game via the command-line interface directly from a cloud platform.

To access the deployed game, visit the following link:

[Play Hangman on Heroku](https://hangman-pgz-54aa0040764b.herokuapp.com/)