import random


# Load words from a file
def load_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


# Choose a random word from a list
def chose_random_word(words):
    if len(words) == 0:
        print("Error: words list is empty")
        return None
    return random.choice(words)


def get_user_guess():
    input_user = input("Guess a letter: ")
    guess = input_user.lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Error: Please enter a single letter.")
        return get_user_guess()
    return guess


# Update game state
def update_game_state(game_state, guess):
    if guess in game_state['word_lower_case']:
        game_state['guessed_letters'].append(guess)
    else:
        game_state['incorrect_guesses'].append(guess)
        game_state['remaining_attempts'] -= 1
    return game_state


# Display word letters with guessed letters
def display_word_letters(word, guessed_letters):
    # converting the list guessed word into a string
    return ''.join([letter if letter in guessed_letters else "_"
                    for letter in word])


def is_word_guessed(word, guessed_letters):
    word_unique_letters = set(word)
    word_to_check = set("".join(guessed_letters))

    if len(word_to_check) == len(word_unique_letters):
        return True


def check_game_over(game_state):
    if is_word_guessed(game_state['word_lower_case'],
                       game_state['guessed_letters']):
        print(f"Congratulations! You've guessed the word: "
              f"{game_state['word_original']}")
        return True
    elif game_state['remaining_attempts'] == 0:
        print(f"Game Over! The word was: {game_state['word_original']}")
        return True
    return False


# Initialize a game state with a word
def initialize_game(word):
    return {
        "word_original": word,
        "word_lower_case": word.lower(),
        "guessed_letters": [],
        "incorrect_guesses": [],
        "remaining_attempts": 6,
    }


def display_game_status(game_state):
    print(f"Word: {display_word_letters(game_state['word_lower_case'], 
                                        game_state['guessed_letters'])}")
    print(f"Incorrect guesses: {', '.join(game_state['incorrect_guesses'])}")
    print(f"Remaining attempts: {game_state['remaining_attempts']}")


def play_hangman(words):
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


