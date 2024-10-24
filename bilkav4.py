print("Enter a sentence")
text = input(">_ ")

arr = []

for i in text.split():
    arr.append(i)

print(len(arr))