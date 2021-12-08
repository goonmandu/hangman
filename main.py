import random


def main():
    with open("randomwords.txt") as f:
        word = random.choice(f).rstrip()
    marked = [None] * len(word)
    tries = 0
    used_letters = []
    has_dash = False
    has_space = False

    for index, letter in enumerate(word):
        if "-" == letter:
            marked[index] = 0
            has_dash = True
        if " " == letter:
            marked[index] = 0
            has_space = True

    MAX_TRIES = marked.count(None)

    print(f"Hangman!\n"
          f"Lives: {MAX_TRIES}❤ | Wrong guesses will cost you 1❤.\n"
          f"Your word is:")

    for index, char in enumerate(marked):
        if char != 0:
            print("_ ", end="")
        else:
            print(f"{word[index]} ", end="")

    if has_dash and has_space:
        print("(Contains dashes and spaces)", end="")
    elif has_dash:
        print("(Contains dashes)", end="")
    elif has_space:
        print("(Contains spaces)", end="")
    print()

    while tries < MAX_TRIES:
        guess = input("\nGuess a letter: ")
        if len(guess) > 1:
            print(f"Only one letter at a time. ({MAX_TRIES - tries}❤)", end="")
            continue
        if guess not in word:
            tries += 1
            used_letters.append(guess)
        for index, letter in enumerate(word):
            if guess == letter:
                marked[index] = 0
        for index, char in enumerate(marked):
            if char != 0:
                print("_ ", end="")
            else:
                print(f"{word[index]} ", end="")
        print(f"({MAX_TRIES - tries}❤)")
        print(f"Banlist: {' '.join(sorted(set(used_letters)))}")
        if marked == [0] * len(word):
            print("\nYou won!")
            exit()
    print(f"\nYou've ran out of lives.\n"
          f"The word was \"{word}.\"")


if __name__ == "__main__":
    main()
    
