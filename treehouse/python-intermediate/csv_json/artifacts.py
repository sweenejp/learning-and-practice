import csv

with open("C:/Users/jasweeney/PycharmProjects/treehouse_intermediate/csv_json/cstmc-CSV-en.csv_json",
          newline='') as csv_file:
    art_reader = csv.DictReader(csv_file, delimiter='|')
    rows = list(art_reader)
    for row in rows[1:3]:
        print(row['ObjectName'])
