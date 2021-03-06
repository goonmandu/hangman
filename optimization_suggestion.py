import random

with open("randomwords.txt") as f:
    word = random.choice(f.readlines()).rstrip()

word_set=set(word)
TRIES=len(word)
while word_set and TRIES:
    print(*('_' if letter in word_set else letter for letter in word),
          f'{TRIES=}')
    try:
        word_set.remove(input())
    except KeyError:
        TRIES -= 1
print("You won!" if TRIES else "You died!")
