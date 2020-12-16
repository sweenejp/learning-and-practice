import csv

with open('teachers.csv_json', 'a') as csv_file:
    field_names = ['first_name', 'last_name', 'subject']
    teach_writer = csv.DictWriter(csv_file, fieldnames=field_names)

    teach_writer.writeheader()
    teach_writer.writerow({
        "first_name": "Jimmy",
        "last_name": "Sweeney",
        "subject": "Biology"
    })