# CSV docs: https://python-adv-web-apps.readthedocs.io/en/latest/csv.html#introduction-to-csv-files

import csv
from config import CONST


class LearnCSV:
    def __init__(self, path=CONST.CSV_PATH):
        self.csv_file = path

    def reading_from_csv_file(self):
        with open(self.csv_file, encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, quotechar='|')
            for row in spamreader:
                print(', '.join(row))

    def writing_to_csv(self, data: list):
        with open(self.csv_file, mode='a', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, quotechar='|')
            spamwriter.writerows(data)

    def reading_csv_into_dict(self):
        with open(self.csv_file, encoding='utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile, quotechar='|')
            for row in spamreader:
                print(row)

    def writing_to_csv_from_dict(self, headers: list, data: dict):
        with open(self.csv_file, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    c = LearnCSV()
    # c.reading_from_csv_file()
    c.writing_to_csv([['1', '2', '3'], ['4', '5', '6']])
    # c.reading_csv_into_dict()
