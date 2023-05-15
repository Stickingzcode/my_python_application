import json
# serialization: converting a python object to a javascript object-a JASON format
records = {"student_records": [
               {"id": 1, "name": "ebuka", "age": 43},
                {"id": 2, "name": "dele", "age": 45},
                {"id": 3, "name": "ola", "age": 34}
            ]
           }
# the rec is an alias to the statement inside the parenthesis,
# it tells json.dump to dump the records object inside the json file.
with open("records.json", mode='w') as rec:
    json.dump(records, rec)
# deserialization
with open("records.json", mode='r') as rec2:
    print(json.dumps(json.load(rec2), indent=4))