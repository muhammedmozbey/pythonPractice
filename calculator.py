# command line calculator
def main():
    userInput = input(">_ ").replace(" ", "")
    res = operatorDetect(userInput)
    print(res)


def operatorDetect(inp):
    inp.split()

    if inp[1] == '+':
        return int(inp[0]) + int(inp[2])
    elif inp[1] == '-':
        return int(inp[0]) - int(inp[2])
    elif inp[1] == '/':
        return int(inp[0]) // int(inp[2])
    else:
        return int(inp[0]) * int(inp[2])


if __name__ == "__main__":
    main()




