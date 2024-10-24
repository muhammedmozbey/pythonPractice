#not exactly what it should be
def main():
    print("eNtEr YoUr MeSsAgE:")
    userInput = input(">_ ")
    spongeBobbed = spongeBob(userInput)
    print(spongeBobbed)

def spongeBob(text):
    spongeBob = ""
    for i in range(len(text)):
        if text[i].isupper() and i + 1 < len(text):
            newLetter = text[i + 1].lower()
            spongeBob += text[i] + newLetter
            continue
        elif text[i].islower() and i + 1 < len(text):
            newLetter = text[i + 1].upper()
            spongeBob += text[i] + newLetter
            continue
    return spongeBob

if __name__ == "__main__":
    main()


'''
import random
def main():
    print("eNtEr YoUr MeSsAgE:")
    userInput = input(">_ ")
    spongeBobbed = spongeBob(userInput)
    print(spongeBobbed)

def spongeBob(text):
    spongeBob = ""
    useUpper = False
    for char in message:
        if not char.isalpha():
            spongeBob += char
            continue
        if useUpper:
            spongeBob += char.upper()
        else:
            spongeBob += char.lower()
        if random.randint(1, 100):
            useUpper = not useUpper
    return spongeBob

if __name__ == "__main__":
    main()
'''
