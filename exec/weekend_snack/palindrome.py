def palindrome(name_set):
    first_lower = name_set.lower()
    low = first_lower

    swap_list = first_lower[::-1]
    if swap_list == low: print(name_set + " is a palindrome")
    if swap_list != low: print(name_set + " is not a palindrome")

name_set = "madam"
print(palindrome(name_set))