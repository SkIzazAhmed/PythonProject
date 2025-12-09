import random


target = list(input("Enter the target word: "))
len1=len(target)

current = list("a"*len1)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet=alphabet+alphabet.upper()

attempts = 0


def get_random_char():

    return random.choice(alphabet)

for i in range(len1):
    while True:
        if(current[i]==target[i]):
            break
        else:
            r=get_random_char()
            current[i]=r
        print(" | | ".join(current),"|")


