#names = []
#count = 0
# while count < 4:
#    name = input("Enter a name: ")
#    if len(name) <= 10 and len(name) > 0:
#        names.append(name)
#    count += 1
#print(names)
#value = 'Programming'
#for letters in value:
#    print(letters, end='  ')
#print(20, 30, 34, 57, sep='')
#total = 0
#for number in [2, -3, 4, 76, 68]:
#    total = total + number
#print(total)
#for x in range(1, 10):
#   print(x)
#total = 0
#for x in range(1_000):
#    total = total + x
#print('total is: ', total)

total = 0
grade_counter = 0
grades = [75, 68, 79, 94, 83, 47, 98, 85, 3, 94]
for grade in grades:
    total += grade
    grade_counter += 1
average = total / grade_counter
print(f'Class average is: ', average)

total = 0
grade_counter = 0
while grade_counter < 3:
    grade = int(input('Enter the grades: '))
    print(grade)
    grade_counter += 1
total += grade
print(f'the average of the scores you have entered is: ', {total/3})

principal = 1_000
rate = 0.05
# number of years is 10
for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:<2} {amount:>10.2f}')




