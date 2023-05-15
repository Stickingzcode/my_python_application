list_of_food = ["rice", "beans", "garri", "rice"]
def duplicate(list_of_food):
    my_set = set(list_of_food)
    if len(list_of_food) != my_set:
        return "Duplicate"
    else:
        return "No duplicate"
print(duplicate(list_of_food))

def obtain_duplicate(food):
    set_of_food = []
    over_sized = []
    for food_item in food:
        if food_item not in set_of_food:
            set_of_food.append(food_item)
        else:
            over_sized.append(food_item)
    print(set_of_food)
    print(over_sized)

print(obtain_duplicate(list_of_food))
list_number =[1, 1, 4, 8, 8, 6, 5, 4]

print(obtain_duplicate(list_number))