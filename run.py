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
    input_user = input("Guess a letter: ")
    guess = input_user.lower()
    if len(guess) != 1 or guess.isalpha()==False:
        print("Error: Please enter a single letter.")
        # Calls itself to ask for a new guess in case the user entered more than one letter
        return get_user_guess()
    return guess

# Update game state
def update_game_state(game_state, guess):
    if guess in game_state['word_lower_case']:
        game_state['guessed_letters'].append(guess)
    else:
        game_state['incorrect_guesses'].append(guess)
        game_state['remaining_attempts'] =  game_state['remaining_attempts'] - 1
    return game_state

# Initialize a game state with a word
def initialize_game(word):
    return {
        "word_original": word,
        "word_lower_case": word.lower(),
        "guessed_letters": [],
        "incorrect_guesses": [],
        "remaining_attempts": 6,
    }




if __name__ == "__main__":

    #testing loading words works"
    words = load_words('./words.txt')
    word = chose_random_word(words)
    game_state=initialize_game(word)
    guess = get_user_guess()
    print(game_state)
    current_game_state=update_game_state(game_state, guess)
    print(current_game_state)   
 
   
