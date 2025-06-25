import os
import re
import csv
import pandas as pd

# File and folder settings
document = "documents.csv"
base_filename = "new_doc"
input_dir = ".."
output_dir = "../new"
chunk_size = 100


# Entry point
def main():
    os.makedirs(output_dir, exist_ok=True)
    http_bool = ask_for_link_filter()
    process_file(http_bool)


# Ask if filtering by links is needed
def ask_for_link_filter():
    answer = input("Do you want to search for value only with links in the document? (y/n): ").strip().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return ask_for_link_filter()


# Build output file path
def output_filename(index):
    return os.path.join(output_dir, f"{base_filename}_{index}.csv")


# Check if row contains a link
def contains_links(row):
    return any(re.search(r'http[s]?://', cell) for cell in row)


# Save chunk to a CSV file
def file_maker(file_number, chunk, csv_header):
    df = pd.DataFrame(chunk, columns=csv_header)
    df.to_csv(output_filename(file_number), index=False, encoding="utf-8")


# Process the input file and create output chunks
def process_file(http_bool):
    with open(os.path.join(input_dir, document), 'r', encoding="utf-8", buffering=1024 * 1024 * 500) as input_file:
        chunk = []
        file_number = 0

        reader = csv.reader(input_file, delimiter='\t')
        csv_header = next(reader)

        for row in reader:
            if len(chunk) != chunk_size:
                if http_bool:
                    if contains_links(row):
                        chunk.append(row)
                else:
                    chunk.append(row)
            else:
                file_maker(file_number, chunk, csv_header)
                file_number += 1
                chunk = []

        if chunk:
            file_maker(file_number, chunk, csv_header)


if __name__ == "__main__":
    main()
