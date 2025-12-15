import random
import string

def random_string(length=8):
    letters = string.ascii_letters + string.digits + " ,\""
    return ''.join(random.choice(letters) for _ in range(length))

def generate_row(num_cols=5):
    return [random_string(random.randint(5, 15)) for _ in range(num_cols)]

def generate_csv(file_name="benchmark.csv", num_rows=10000, num_cols=5):
    from custom_csv_writer import CustomCsvWriter

    writer = CustomCsvWriter(file_name)
    data = [generate_row(num_cols) for _ in range(num_rows)]
    writer.write(data)
    print(f"{file_name} with {num_rows} rows generated successfully.")

if __name__ == "__main__":
    generate_csv()
