student_record = [{"id": 1, "name": "Sultan", "score": (78, 48, 56)}, {"id": 2, "name": "Adeyanju", "score": (89, 65, 67)},
                  {"id": 3, "name": "Vickie", "score": (98, 78, 46)}, {"id": 4, "name": "Ayobami", "score": (69, 54, 34)},
                  {"id": 5, "name": "Rotimi", "score": (90, 80, 70)}]
print(f"The list of students' record is: ", student_record, end=' ')
add_record = [{"id": 6, "name": "Ola", "score": (65, 37, 68)}, {"id": 7, "name": "Goat", "score": (74, 68, 90)}]
student_record.append(add_record)
print(f"The updated list of records is: ", student_record)
student_record.remove(student_record[3])
print(f"The recent list is: ", student_record, end=' ')