
def main():
    print("L3375P34]< (leetspeek)\nEnter your message:")
    userMessage = input(">_ ").lower()
    leetspeak = leetSpeak(userMessage)
    for word in leetspeak:
        print(word, end="")
    print(" ")

def leetSpeak(text):
    charMapping = {
    'a': '4', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '|=', 'g': '6', 'h': '#',
    'i': '1', 'j': '_|', 'k': '|<', 'l': '1', 'm': '|\/|', 'n': '|\|', 'o': '0', 'p': '|>',
    'q': '0_', 'r': '|2', 's': '5', 't': '7', 'u': '|_|', 'v': '\/', 'w': '\^/', 'x': '><',
    'y': '`/', 'z': '2'}
    leetspeak = []
    for i in range(len(text)):
        if text[i] in charMapping:
            leetspeak.append(charMapping[text[i]])
        else:
            leetspeak.append(text[i])
    return leetspeak
main()

