text = open("/Users/izaz/Documents/PythonFiles/TestLinefile.txt","r")
alphabet = "abcdefghijklmnopqrstuvwxyz"

counts = [0] * 26 

for i in text:
    for words in i.split():
        for char in words.lower():
            if char in alphabet:
                ind=alphabet.index(char)
                counts[ind]=i.count(char)
                print(counts)
                pass

print("Frequency Graph:")

for i in range(26):

    if counts[i] > 0:
        print(alphabet[i],"--","#"*counts[i])
        pass