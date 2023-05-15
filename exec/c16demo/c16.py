#name = "Hippopotamus"
#print(name)
#name_reverse = name[::-1]
#print(name_reverse)
#skip_name = name_reverse[0:12:2]
#print(skip_name)


#def currency(dollar:int)->str:
 #   naira = dollar * 750
  #  return f"The naira equivalent of ${dollar} you gave me is #{naira:,.2f}"

#dollar = int(input("Give me money: "))
#print(currency(dollar))

#def multiply(*list):
 #  product = 1
  # for num in list:
   #    product *= num
    #return product


#print(multiply(3, 5, 4, 8))

#add = 0
#for number in range(5):
 #    add += number
#print(add)


#def multiply(x,y):
 #    product = x * y
  #   return product

#num = multiply (2,4)
#print(num)

#def cube(x):
 #    power = x ** 3
  #   return power

#number = cube(4)
#print(number)

#another_number = cube(8)
#print(another_number)

# def greet(name):
#     print(f"Holla! {name}")

# greet("Vickie")

def get_user(**user):
     print(user)

get_user(id = 1, first_name = "Micheal", last_name = "Friday")
