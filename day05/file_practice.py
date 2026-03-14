import csv

with open("contacts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "phone", "email"])
    writer.writerow(["Grant", "555-1234", "grant@email.com"])

with open("contacts.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)