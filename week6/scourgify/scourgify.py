import sys
import csv
def main():
    check_command_line_arg()
    output = []
    try:
        with open(sys.argv[1], "r") as csv_file:
            csv_read = csv.DictReader(csv_file)
            for row in csv_read:
                split_name = row["name"].split(",")
                output.append({"first":split_name[1].lstrip(), "last":split_name[0], "house":row["house"]})
            # print(output)
        with open(sys.argv[2], "w") as output_file:
            csv_write = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            csv_write.writerow({"first" : "first", "last" : "last", "house" : "house"})
            for row in output:
                csv_write.writerow({"first" : row["first"], "last" : row["last"], "house" : row["house"]})
    except FileNotFoundError:
        print("File Not Exist")






def check_command_line_arg():
    if(len(sys.argv)) < 3:
        sys.exit("Too few command-line arguments")
    if(len(sys.argv)) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()