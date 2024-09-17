import random


def load_words(file_path):
    """
    Loads words from a given file.
    It validates the file path and reads the words from the file.
    """
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


def chose_random_word(words):
    """
    Choses a random word from the list.
    """
    if len(words) == 0:
        print("Error: words list is empty")
        return None
    return random.choice(words)


def get_user_guess():
    """
    Prompts user to guess a letter.
    Asks the user to enter a single letter and validates the input.
    The letter is converted to lowercase and returned if it is a
    valid letter.
    """
    input_user = input("Guess a letter: ")
    guess = input_user.lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Error: Please enter a single letter.")
        return get_user_guess()
    return guess


def update_game_state(game_state, guess):
    """
    Updates the state of the game based on the user's guess.
    Adds the guessed letter to either the list of correct or incorrect guesses.
    Also decreases the number of remaining attempts if the guess is wrong.
    """
    if guess in game_state['word_lower_case']:
        game_state['guessed_letters'].append(guess)
    else:
        game_state['incorrect_guesses'].append(guess)
        game_state['remaining_attempts'] -= 1
    return game_state


def display_word_letters(word, guessed_letters):
    """
    Shows the word with correct guesses and underscore for the remaining unknow
    letters.
    """
    return ' '.join([letter if letter in guessed_letters else "_"
                    for letter in word])


def is_word_guessed(word, guessed_letters):
    """
    Checks if the entire word has been guessed.
    Compares the unique letters in the word with the letters guessed by the
    user. If the number of unique letters in the word is equal to the number of
    correct guessed letters, it returns True, otherwise False.
    """
    word_unique_letters = set(word)
    word_to_check = set("".join(guessed_letters))

    if len(word_to_check) == len(word_unique_letters):
        return True


def check_game_over(game_state):
    """
    Checks if the game is over (win or lose).
    Determines if the game is over by checking if the word has been fully
    guessed or if the player has run out of attempts. Prints the appropriate
    message and returns True if the game is over, otherwise False.
    """
    if is_word_guessed(game_state['word_lower_case'],
                       game_state['guessed_letters']):
        print(f"Congratulations! You've guessed the word: "
              f"{game_state['word_original']}")
        return True
    elif game_state['remaining_attempts'] == 0:
        print(f"Game Over! The word was: {game_state['word_original']}")
        return True
    return False


def initialize_game(word):
    """
    Initializes the game state.
    Sets up the initial game state including the word to guess,
    the list of guessed letters, the incorrect guesses, and the number of
    remaining tries.
    """
    return {
        "word_original": word,
        "word_lower_case": word.lower(),
        "guessed_letters": [],
        "incorrect_guesses": [],
        "remaining_attempts": 6,
    }


def display_game_status(game_state):
    """
    Displays the current game status.
    Shows the current status of the word with guessed letters and underscore
    for theremaining unknown letters. Also displays the incorrect guesses
    and the remaining attempts.
    """
    print(f"Word status: {display_word_letters(game_state['word_lower_case'],
          game_state['guessed_letters'])}")
    print(f"Incorrect guesses: {', '.join(game_state['incorrect_guesses'])}")
    print(f"Remaining attempts: {game_state['remaining_attempts']}")


def play_hangman(words):
    """
    Main function to start and run the hangman game.
    """
    word = chose_random_word(words)
    game_state = initialize_game(word)

    while not check_game_over(game_state):
        display_game_status(game_state)
        guess = get_user_guess()

        if guess in game_state['guessed_letters'] or guess in \
                game_state['incorrect_guesses']:
            print("You've already guessed that letter.")
        else:
            update_game_state(game_state, guess)

    if input("Do you want to play again? (y/n): ").lower() in ["yes", "y"]:
        play_hangman(words)


if __name__ == "__main__":
    words = load_words('./words.txt')
    if words:
        play_hangman(words)
