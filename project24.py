import sys
import math

print("Enter a number to factor (or 'QUIT' to quit):")
userInput = int(input(">_ "))

while True:
    if userInput == "QUIT":
        sys.exit()
    factors = []
    for i in range(1, int(math.sqrt(userInput) + 1)):
        if userInput % i == 0:
            factors.append(i)
            factors.append(userInput // i)
    break

for i in sorted(factors):
    print(i, end=" ")
print("")
