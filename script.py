import sys
import csv
from tabulate import tabulate

def load_csv_data(filename, delimiter=','):
    lines = []
    try:
        with open(filename) as file:
            csvreader = csv.reader(file, delimiter=delimiter)
            for row in csvreader:
                lines.append(row)
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    return lines

def sort_data(data, column):
   try:

       if column >= len(data[0]):
        print("Invalid column index for sorting")
        return data

       sorted_data = [data[0]] + sorted(data[1:], key=lambda x: x[column])
       return sorted_data
   except IndexError:
       sys.exit("List index is Out of range please put the index in between 1 to 12 ")

def filter_data(data, column, value):
    if column >= len(data[0]):
        print("Invalid column index for filtering")
        return data

    filtered = [data[0]]
    for row in data[1:]:
        if row[column].strip() == value:
            filtered.append(row)
    return filtered

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py filename.csv")

    filename = "airtravel.csv"

    if not filename.endswith(".csv"):
        print("File is not a csv file")
        sys.exit()
    try:
        delimiter = input("Enter the delimiter (default is comma): ")
        if not delimiter:
            delimiter = ','

        lines = load_csv_data(filename, delimiter)
        headings = lines[0]
    except TypeError:
        sys.exit("delimiter must be a 1-character string")


    print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    while True:
        choice = input("\nDo you want to:\n"
                       "1. Sort data\n"
                       "2. Filter data\n"
                       "3. Exit\n"
                       "Enter your choice: ")

        if choice == '1':  # Converted to string for proper comparison
            column = int(input("Enter the column index to sort by: "))
            lines = sort_data(lines, column)
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

        elif choice == '2':  # Converted to string for proper comparison
            column = int(input("Enter the column index to filter by: "))
            value = input("Enter the value to filter for: ")
            lines = filter_data(lines, column, value)
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

        elif choice == '3':  # Converted to string for proper comparison
            sys.exit("Exiting the program.")

        else:
            print("Invalid choice. Please choose again.")
