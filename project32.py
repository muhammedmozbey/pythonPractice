def main():
    while True:
        userInput = input("Do you want to know how to keep a gullible person busy for hours? Y/N\n").lower()
        if userInput == "y" or userInput == "yes":
            continue
        elif userInput == "n" or userInput == "no":
            break
        else:
            print(f'"{userInput}" is not a valid yes/no response')
    print("Thank you. Have a great day!")

if __name__ == "__main__":
    main()
