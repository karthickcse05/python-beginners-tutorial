numbers = [5,6,5,6,8,4,3,4,2]
without_duplicate_numbers = []

for number in numbers:
    if number not in without_duplicate_numbers:
        without_duplicate_numbers.append(number)
print(without_duplicate_numbers)