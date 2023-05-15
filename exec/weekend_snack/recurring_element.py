numbers = [12, 8, 15, 3, 27, 9]

def element_occurrence(number, numbers):
    if number in numbers:
        return f"{number} occurs"
    else:
        return f"{number} does not occur"

print(element_occurrence(5,numbers))

print(element_occurrence(12, numbers))