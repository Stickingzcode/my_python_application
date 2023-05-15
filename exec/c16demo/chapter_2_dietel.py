counter = 0
total = 0
while counter < 3:
    grades = int(input('Enter your grades: '))
    print(grades)
    counter += 1
    total += grades
print(f'total score equals: ', total)
average = total / 3
print(f'the average scores of students is: {average:.2f}')

counter = 0


# jonah = 22
# print(f"dividing 22 marbles among 4 friends result in: {22 / 4} marbles each")
#
# bacteria = 200
# print(f"Hours \t Bacteria")
# for num in range(0, 20, 5):
#     new_bacteria = 200 * (2 ** num)
#     # System.out.printf("%5s%n%8s%n", "hours", "new-bacteria");
#
#     print(f'{num:>2} \t\t{new_bacteria:<10,.3f}')
# bacteria = 200
# print(f'Hours \t Bacteria')
# for num in range(0, 20, 5):
#     new_bacteria = 200 * (2 ** num)
#     print(f'{num:<2} \t\t{new_bacteria:>13,.3f}')
#
# # computer's character set: indicating the integer representation
# Tom = ord("T") + ord("o") + ord("m")
# Jim = ord("J") + ord("i") + ord("m")
# print(Tom)
# print(Jim)
# if Tom > Jim:
#     print('Tom goes first.')
# else:
#     print('Jim goes first.')
#
# x = 2
# y = 3
# print('x =', x)
# print('Value of', x, '+', x, 'is', (x+x))
# print('x =')
# print((x + y), '=', (y + x))
#
# number = int(input("Input a number between 1 and 10\n"))
# square = number * number
# print(square)
#
# w = -5
# z = 0
# a = 2
# b = 7.5
# c = 5
# print((w - a), (z+a), (b*a), (c/a), (w//a), (a**a))
#
# odd_number = int(input("Enter a number: \n"))
# if odd_number % 2 != 0:
#     print("You have entered an odd number")
# else:
#     print("you have entered an even number")
# print("Display the name O'Brien")
