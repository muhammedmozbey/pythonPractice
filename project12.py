"""
if n is even, the next number n is n/2
if n is odd, the next number n is n*3+1
if n is 1, stop. Otherwise, repeat
"""

def main():
    userInput = input("Enter a starting number (greater than 0) or QUIT: ")

    integerInput = int(userInput)

    function(integerInput)

def function(n):
    print(n, end=' ', flush=True)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n, end=' ',flush=True)
        else:
            n = n * 3 + 1
            print(n, end=' ', flush=True)
    return n


if __name__ == "__main__":
    main()