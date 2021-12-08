import random

with open("randomwords.txt") as f:
    word = random.choice(f).rstrip()

word_set=set(word)
TRIES=6
while word_set and TRIES:
    print(*('_' if letter in word_set else letter for letter in word),
          f'{TRIES=}')
    try:
        word_set.remove(input())
    except KeyError:
        TRIES -= 1
print("You won!" if TRIES else "You died!")
