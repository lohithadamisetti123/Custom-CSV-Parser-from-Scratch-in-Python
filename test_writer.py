from custom_csv_writer import CustomCsvWriter
from custom_csv_reader import CustomCsvReader

data = [
    ["name", "age", "comment"],
    ["Alice", 23, "Student"],
    ["Bob, Jr", 25, "Lives in Hyderabad, India"],
    ["Charlie", 30, 'He said "Hello"'],
    ["David", 28, "Line1\nLine2"]
]

writer = CustomCsvWriter("writer_test.csv")
writer.write(data)

print("Written CSV content:\n")

with open("writer_test.csv", "r", encoding="utf-8") as f:
    print(f.read())

print("\nReading back using CustomCsvReader:\n")

reader = CustomCsvReader("writer_test.csv")
for row in reader:
    print(row)
