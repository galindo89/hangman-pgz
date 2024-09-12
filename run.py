

def load_words (file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('File not found')
        return []


def main ():

    #testing loading words works"
    words = load_words('./words.txt')
    if words is None:
        return
    print(words)

main()