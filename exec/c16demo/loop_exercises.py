# number = 0  # variable declaration and initialization
# while number < 10:  # test condition
# loop body
#    print(number)
#    number += 1  # incrementation

# user_number = float(input("Enter a positive number: "))
# while user_number <= 0:
#  print("You have entered a negative number!")
# user_number = float(input("Enter a positive number: "))
# else:
#    print(f"{user_number * 2}")

# for n in range(3):
#    print("Python")

# word = "Python"
# index = 0

# while index < len(word):
#    print(word[index])
#    index += 1

# for letters in "Python":
#    print(letters)

amount_to_be_shared = float(input("Enter an amount: "))
num_of_people = 2
while num_of_people < 6:
    print(f"{num_of_people} people gets {amount_to_be_shared / num_of_people:,.2f} naira each")
    num_of_people += 1

amount = float(input("Enter an amount: "))
for num_people in range(2, 6):
    print(f"{num_people} persons get {amount / num_people:,.2f} naira each")

for numbers in range(2, 11):
    print(numbers)

number = 2
while number <= 10:
    print(number)
    number += 1