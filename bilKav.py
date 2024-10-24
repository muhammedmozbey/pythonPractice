#longest word in the array from bilkav quizes
def main():
    arr = ["Hello", "Worldeee", "Muhammed", "is", "here"]

    #currentWord = ""
    longest = ""
    secondLongest = ""
    longestSize = 0
    secondLongestSize = 0

    for i in range(len(arr)):
        currentWord = arr[i]
        currentSize = wordSize(currentWord)
        if currentSize > len(longest):
            longest = currentWord
            longestSize = len(longest)
        elif currentSize == longestSize and currentWord != longest:
            secondLongest = currentWord
            secondLongestSize = len(secondLongest)

    if secondLongest != " " and secondLongestSize == longestSize:
        print(f"Longest words: {secondLongest}, {longest}")
    else:
        print(f"Longest word: {longest}")
def wordSize(word):
    size = 0
    for i in range(len(word)):
        size += 1
    return size
main()
