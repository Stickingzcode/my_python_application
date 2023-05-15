score = (float(input("Enter your score: ")))
while score != range(0, 100):
    print("Enter a valid score: ")

if 0 <= score <= 40:
    print("F: Fail")
else:
    if 40 >= score <= 49:
        print("D: Pass")
    else:
        if 50 >= score <= 69:
            print("C: Credit")
        else:
            if 70 >= score <= 79:
                print("B: Upper Credit")
            else:
                if 80 >= score <= 100:
                    print("A: Excellent!")
                else:
                    score = (float(input("Enter your score: ")))
