amount = int(input('Enter your price: '))
print(amount)

def discount(amount):
    discounted_amount = amount - ((10 / 100) * amount)
    return discounted_amount

print(f'your discount is: {discount(amount)}')


count = 0
number_of_trials = 5
lucky_number = 5
while count != number_of_trials:
    user_input = int(input('enter a lucky number: '))
    print(user_input)
    if user_input == lucky_number:
        print('Congratulations!, you are a WINNER')
        break
    else:
        print('oops! try again')
    count += 1
print('izz gone!')





