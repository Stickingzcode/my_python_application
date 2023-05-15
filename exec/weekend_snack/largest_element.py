numbers = [12, 8, 15, 3, 27, 9]
largest_element = numbers[0]
for num in numbers:
    if num > largest_element:
        largest_element = num
print(largest_element)