# pig -> igpay
# latin -> atinlay
# elephant -> elephantyay
# umbrella -> umbrellayay


VOWELS = ('a', 'e', 'i', 'o', 'u')

def main():
    print("Enter your message:")
    message = input("> ").lower()
    latin = pigLatin(message)
    for word in range(len(latin)):
        print(latin[word], sep=" ", end=' ')
    print()


def pigLatin(text):
    word = text.split(" ")
    for u in range(len(word)):
        if word[u].startswith(VOWELS):
            word[u] = word[u] + "yay"
        else:
            word[u] = word[u] + word[u][0]+ "ay"
            word[u] = word[u][1:]
            

    return word



    
if __name__ == "__main__":
    main()