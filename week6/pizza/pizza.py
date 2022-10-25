from tabulate import tabulate
import sys
import csv
def main():
    check_command_line_arg()
    table = []
    try:
        with open(sys.argv[1], "r") as csv_file:
            read_csv = csv.reader(csv_file)
            for row in read_csv:
                table.append(row)
        # print(table)
        print(tabulate(table[1:], headers=table[0], tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_command_line_arg():
    if(len(sys.argv)) < 2:
        sys.exit("Too few command-line arguments")
    if(len(sys.argv)) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()