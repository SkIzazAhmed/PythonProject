import random as rnd

words = input("Enter The Holy Word : ").split()
current_word = words[0]

sentence = [current_word]

for _ in range(10):
    possible_next_words = []

    for i in range(0,len(words)-1):
        if words[i] == current_word:
            possible_next_words.append(words[i+1])

    if len(possible_next_words) > 0:
        next_word = rnd.choice(possible_next_words)
        # print(next_word)
        sentence.append(next_word)
        current_word = next_word
    else:
        break

print("Generated:", " ".join(sentence))
