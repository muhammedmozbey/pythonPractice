print("Enter a number:")
n = int(input(">_ "))

output = []

i = 2
while i <= n:
    if n % i ==0:
        output.append(i)
        n //= i
    else:
        i += 1
print(output)

