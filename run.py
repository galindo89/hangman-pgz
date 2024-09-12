import random


def load_words (file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f" Error: {file_path} not found.")
        return []

def chose_random_word(words):
 
    if len(words) == 0:
        print("Error: words list is empty")
        return None
    return random.choice(words)


def main ():

    #testing loading words works"
    words = load_words('./words.txt')
    if words is None:
        return
    print(words)

main()