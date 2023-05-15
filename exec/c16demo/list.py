doubles = {}
for a in range(1, 11):
    doubles[a] = a ** 2
print(doubles)

# dictionary
doubles = {a: a ** 2 for a in range(1, 11)}
print(doubles)

# tuple
doubles = (a ** 2 for a in range(1, 11))
print(doubles)

# generator
from sys import getsizeof
double = [a ** 2 for a in range(1000000)]
doubles = (a ** 2 for a in range(1000000))
print(getsizeof(doubles))
print(getsizeof(double))


def fizzbuzz(number):
    number = int(input("Enter a number: "))
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
# higher order function; map is a builtin keyword
list2 = [ 1, 2, 3, 4, 5, 6 ]
def square(num):
    return num ** 2

ans = list(map(square, list2))
print(ans)

num = input("Enter a number")
def square(num: int):
    num_square = num ** 2
    return num_square

print(square())

