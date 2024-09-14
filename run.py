import random

# Load words from a file
def load_words (file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f" Error: {file_path} not found.")
        return []

# Choose a random word from a list
def chose_random_word(words):
 
    if len(words) == 0:
        print("Error: words list is empty")
        return None
    return random.choice(words)

def get_user_guess():
    guess = input("Guess a letter: ")
    if len(guess) != 1 or guess.isalpha()==False:
        print("Error: Please enter a single letter.")
        # Calls itself to ask for a new guess in case the user entered more than one letter
        return get_user_guess()
    return guess

# Initialize a game state with a word
def initialize_game(word):
    return {
        "word": word,
        "guessed_letters": [],
        "incorrect_guesses": [],
        "remaining_attempts": 6,
    }




if __name__ == "__main__":

    #testing loading words works"
    words = load_words('./words.txt')
    word = chose_random_word(words)
    game_state=initialize_game(word)
    print(game_state)
    print(words)
    #testing chose_random_word works
    print(word)
    get_user_guess()

 
