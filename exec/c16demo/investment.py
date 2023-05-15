def invest(amount, years):
    interest = (amount * 0.05 * years)
#   return interest += amount

amount = (float(input("Enter the principal amount: ")))
years = (int(input("Enter the number of years: ")))

count = 1
rate = 0.05
while count <= years:
   print(invest(amount, years))
   count += 1

def investment(principal_amount, years):
    rate = 0.05
    try:
        for year in range(1, years + 1):
            roi = principal_amount + rate
            future_value = principal_amount + roi
            principal_amount = future_value
            print(f"year{year} return on investment is {roi:,.2f}, your principal is now {future_value:,.2f}")
    except TypeError:
        return "The amount canot be a string"
    except ValueError:
        return "The value cannot be negative"
#    finally:

investment("a", "f")

