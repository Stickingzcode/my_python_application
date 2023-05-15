def calculate_numbers(enter_list):
    count_male = 0
    count_female = 0
    for i in enter_list:
        if i.lower() == ("male"):
            count_male += 1
            if i.lower() == ("female"):
                count_female += 1
    print(f"[Male = {count_male}], [Female = {count_female} ]")
