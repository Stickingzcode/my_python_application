# def doubles(user_number: int):
#  twice =  user_number * 2
#    return twice


# user_number = (int(input("Enter a small number: ")))
# count = 1
# while count <= 3:
#    print(doubles(user_number))
#    count += 1

def doubles(number: int):
    return number * 2

#
# # user_number = (int(input("enter a small number: ")))
# count = 1
# while count <= 3:
#     user_number = doubles(user_number)
#     print(user_number)
#     count += 1

amount = (int(input("Enter the amount to invest: ")))
years = (int(input("Enter the number of years: ")))
# rate = 0.05
# for year in range(1, years + 1):
#    roi = amount * rate
#   new_principal = amount + roi
#    amount = new_principal
#   print(f"year{year} return on Investment is {roi:,.2f}, principal is now {new_principal:,.2f}")

# def  investment(amount, years):
# rate = 0.05
# for year in range(1, years + 1):
#    roi = amount * rate
#    new_principal = amount + roi
#    amount = new_principal
#    return f"year{year} return on Investment is {roi:,.2f}, principal is now {new_principal:,.2f}"

def investment(amount, years):
    count = 1
    rate = 0.05
    while count <= years:
        roi = amount * rate
        new_principal = amount + roi
        amount = new_principal
        print(f"year{years} return on Investment is {roi:,.2f}, principal is now {new_principal:,.2f}")
        count += 1
investment(amount, years)