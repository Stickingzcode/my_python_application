def multiplication(table, multiple):
    for table in range(1, 13 + 1):
        for multiple in range(1, 13 + 1):
            print(end= " " f"{table : >3}*{multiple : >3} ={table * multiple : >3}")
        print()

first_user_input = (int(input("Enter your first value: ")))
second_user_input = (int(input("Enter your second value: ")))
print(multiplication(first_user_input, second_user_input))

found = False
names = ["Alaye", "Boma", "Fayrouz", "Baller"]
for name in names:
   if name.startswith("B"):
       print("Found")
   else:
       print("Not found")

x = "Hello World"
def func():
   x = 2
   print(f"Inside 'func', x has the value {x}")
func()
print(f"Outside 'func', x has the value of {x}")


