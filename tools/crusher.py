import os
import re
import csv
import pandas as pd


document = "documents.csv"
base_filename = "new_doc"


input_dir = ".."
output_dir = "../new"

chunk_size = 100


def main():

    os.makedirs(output_dir, exist_ok=True)

    http_bool = questin_for_links()

    crusher(http_bool)

def questin_for_links():
    answer = input("Do you want to search for value only with links in the document? (y/n)").strip().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return questin_for_links()


def output_filename(index):
    return os.path.join(output_dir, f"{base_filename}_{index}.csv")


def contains_links(row):
    return any(re.search(r'http[s]?://', cell) for cell in row)

def file_maker(file_number, chunk, csv_header):
    with open(output_filename(file_number), 'w', encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(csv_header)
        writer.writerows(chunk)


def crusher(http_bool):
    with open(os.path.join(input_dir, document), 'r', encoding="utf-8", buffering=1024*1024*500) as input_file:

        chunk = []
        file_number = 0

        reader = csv.reader(input_file)
        csv_header = next(reader)

        for row in reader:




            if chunk.__len__() != chunk_size:
                if http_bool:
                    if contains_links(row):
                        chunk.append(row)

                    else:
                        continue
                else:
                    chunk.append(row)

            else:
                file_maker(file_number, chunk, csv_header)

                file_number += 1
                chunk = []
                
                if file_number >= 200:
                    break

        if chunk:
            file_maker(file_number, chunk, csv_header)




if __name__ == "__main__":
    main()