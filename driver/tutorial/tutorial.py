#max function
numbers = [0, 7, 1, 10, 50, 0]
largest = 0
for x in range(len(numbers)):
    if numbers[x] > largest:
        largest = numbers[x]
else:
    print(largest)