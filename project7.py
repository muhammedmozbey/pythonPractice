print("Enter the encrypted Caesar cipher message to hack.")
message = input("> ").upper()

for key in range(7):
    decrypted = ""
    for i in range(len(message)):
        if message[i].isalpha():
            ascii = ord(message[i])
            new_ascii= ((ascii - ord('A') - key) % 26) + ord('A')
            decrypted += chr(new_ascii)
        else:
            decrypted += message[i]
        if len(decrypted) == len(message):
            print(f"Key #{key}: {decrypted}", end="")
    print()
       


    