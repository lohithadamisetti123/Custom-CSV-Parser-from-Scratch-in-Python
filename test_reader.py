from custom_csv_reader import CustomCsvReader

reader = CustomCsvReader("test.csv")

for row in reader:
    print(row)
