
'''print("Do you want to (e)ncrypt or (d)ecrypt?")
decision = input("> ")
if decision == "e":
    print("Please enter the key (0 to 25) to use")
    number = int(input("> "))
    print("Enter the message to encrypt")
    message = input("> ").upper()
    for i in range(len(message)):
        ascii = ord(message[i])
        new_ascii= ((ascii - ord('A') + number) % 26) + ord('A')
        print(chr(new_ascii), end="")
    print()
elif decision == "d":
    print("Please enter the key (0 to 26) to use")
    number = int(input("> "))
    print("Enter the message to encrypt")
    message = input("> ").upper()
    for i in range(len(message)):
        ascii = ord(message[i])
        new_ascii= ((ascii - ord('A') - number) % 26) + ord('A')
        print(chr(new_ascii), end="")
    print()
else: 
    print("Invalid decision")'''


#prints with spaces 

print("Do you want to (e)ncrypt or (d)ecrypt?")
decision = input("> ")

if decision == "e":
    print("Please enter the key (0 to 25) to use")
    number = int(input("> "))

    print("Enter the message to encrypt")
    message = input("> ").upper()

    encrypted = ""
    for i in range(len(message)):
        if message[i].isalpha():
            ascii = ord(message[i])
            new_ascii= ((ascii - ord('A') + number) % 26) + ord('A')
            encrypted += chr(new_ascii)
        else:
            encrypted += message[i]
    print(encrypted)
elif decision == "d":
    print("Please enter the key (0 to 26) to use")
    number = int(input("> "))

    print("Enter the message to encrypt")
    message = input("> ").upper()

    decrypted = ""
    for i in range(len(message)):
        if message[i].isalpha():
            ascii = ord(message[i])
            new_ascii= ((ascii - ord('A') - number) % 26) + ord('A')
            decrypted += chr(new_ascii)
        else:
            decrypted += message[i]
    print(decrypted)
    
else: 
    print("Invalid decision")