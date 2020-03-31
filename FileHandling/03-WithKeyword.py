# with open('data_2.txt') as file:
#     data = file.read()
#     print(data)

# csv - comma seperated values
import csv

data = [
    {"name":"Sachin", "score":54},
    {"name":"Dhoni", "score":48},
    {"name":"Virat", "score":88}
]

# with open('data.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row.values())

with open('data.csv','r') as file:
    reader = csv.reader(file)
    for item in reader:
        print(item)