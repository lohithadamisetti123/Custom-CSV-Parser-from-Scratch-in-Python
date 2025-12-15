import timeit
import csv
from custom_csv_reader import CustomCsvReader
from custom_csv_writer import CustomCsvWriter

def benchmark_reader(file_name="benchmark.csv"):
    def custom_read():
        reader = CustomCsvReader(file_name)
        for _ in reader:
            pass

    def csv_read():
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for _ in reader:
                pass

    custom_time = timeit.timeit(custom_read, number=1)
    csv_time = timeit.timeit(csv_read, number=1)

    print(f"CustomCsvReader: {custom_time:.4f} seconds")
    print(f"csv.reader: {csv_time:.4f} seconds")

def benchmark_writer(data, file_name_custom="custom_out.csv", file_name_csv="csv_out.csv"):
    def custom_write():
        writer = CustomCsvWriter(file_name_custom)
        writer.write(data)

    def csv_write():
        with open(file_name_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    custom_time = timeit.timeit(custom_write, number=1)
    csv_time = timeit.timeit(csv_write, number=1)

    print(f"CustomCsvWriter: {custom_time:.4f} seconds")
    print(f"csv.writer: {csv_time:.4f} seconds")

def load_benchmark_data(file_name="benchmark.csv"):
    reader = CustomCsvReader(file_name)
    return [row for row in reader]

if __name__ == "__main__":
    print("Benchmarking Reader...")
    benchmark_reader()

    print("\nLoading data for writer benchmark...")
    data = load_benchmark_data()

    print("Benchmarking Writer...")
    benchmark_writer(data)
