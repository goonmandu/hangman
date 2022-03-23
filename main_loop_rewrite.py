word = "verifications"
shown = []
for _ in range(len(word)):
    shown.append("_")

while "".join(shown) != word:
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                shown[i] = word[i]
    print("".join(shown))
