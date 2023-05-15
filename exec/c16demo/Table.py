print(f"number\t\tsquare_of_numbers\t\tcube_of_numbers")
for num in range(0,11):
    print(f'{num:<2}\t\t{num ** 2:>10}\t\t{num ** 3:>20}')