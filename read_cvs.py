import csv

with open("question.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    for row in csv_reader:
        print(row[0])
        question = ()