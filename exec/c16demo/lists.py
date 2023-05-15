#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for num in numbers:
#    if num % 2 != 0:
#        print(num)

lists = [33, 25, 42, 12, 67, 34, 15]
for i in range(len(lists)):
    for j in range(i + 1, len(lists)):
        if lists[i] > lists[j]:
            lists[i], lists[j], = lists[j], lists[i]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd_num(lst):
    odd = []
    for n in lst:
        if n % 2 != 0:
            odd.append(n)
    return odd

#print(odd_num(list_1))
# or
def odd_value(n):
    if n % 2 != 0:
        return n
print(list(filter(odd_value, list_1)))

