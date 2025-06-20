numbers = [1,3,5,5,9,6,7,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
