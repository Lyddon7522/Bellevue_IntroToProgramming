i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

numbers = [1, 3, 5, 7, 9]
target = 3
i = 0

# While to search target in numbers
while i < len(numbers):
    # Check the number
    if numbers[i] == target:
        print("Found the number!")
        break
    i = i + 1

# Else condition run when while loop run completely
else:
    print("Number not found.")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)