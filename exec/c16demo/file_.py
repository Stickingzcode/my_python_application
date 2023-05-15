file = open("student_records.txt", mode='w')
file.write("001 mariam 75\n")
file.write("002 sultan 76\n")
file.write("003 david 75\n")
file.write("004 torin 75\n")
file.close()

with open("record2.txt", mode='w') as file:
    file.write("005 hyelnati 75\n")
    file.write("006 segun 76\n")
    file.write("007 esther 75\n")

with open("record2.txt", mode='a') as file:
    file.write("017 ladi 76\n")

file1 = open('record2.txt', mode='r')
file2 = open('record3.txt', mode='w')

with file1, file2:
    for record2 in file1:
        sn, name, score = record2.split()
        if sn != "015":
            file2.write(record2)
        else:
            new_record = ' '.join([sn, "Oluwadurotimi", score])
            file2.write(name + "\n")

with open("product.txt", mode='w') as file:
    file.write("010 always 150\n")
    file.write("011 mouse 540\n")
    file.write("012 ring 300\n")
    file.write("013 earbuds 1900\n")
    file.write("014 biro 350\n")

with open("record2.txt", mode='r') as records:
    for record in records:
        num, name, score = record.split()
        print(f"{num:<10} {name: <10} {score: >10}")
