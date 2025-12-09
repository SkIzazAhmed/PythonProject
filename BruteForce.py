message = input("Enter The Chyfer: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"


for key in range(1, 26):

    candidate = ""

    for char in message:

        if char in alphabet:

            ind=alphabet.index(char)
            ind=ind-key
            candidate=candidate+alphabet[ind]

            pass

    print(f"Key {key}: {candidate}")

