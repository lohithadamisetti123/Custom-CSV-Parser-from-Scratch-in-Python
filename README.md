#### ***Custom CSV Reader and Writer (Python)***


**Objective**
---



The goal of this project is to understand how CSV (Comma-Separated Values) files work internally by implementing a custom CSV reader and writer from scratch in Python, without using Python’s built-in csv module.

CSV looks simple, but handling quoted fields, commas inside data, escaped quotes, and newlines is not trivial. By building this project, I learned how real-world CSV parsing works and why standard libraries exist.




**What This Project Does**
---


This project contains two main components:



1.CustomCsvReader

* Reads CSV files one row at a time
* Works as an iterator
* Handles quoted fields
* Handles escaped quotes ("")
* Handles newlines inside quoted fields
* Reads the file in a streaming way (does not load full file into memory)



2.CustomCsvWriter



* Writes list-of-lists data into CSV format
* Automatically adds quotes when required
* Escapes quotes correctly
* Produces CSV files that can be read by standard CSV readers


**Folder Structure**
---

custom\_csv/
│
├── custom\_csv\_reader.py
├── custom\_csv\_writer.py
├── generate\_data.py
├── benchmark.py
├── test\_reader.py
├── test\_writer.py
├── test.csv
└── README.md
---


**How the CSV Reader Works** 

---

* The file is read character by character
* A variable in\_quotes is used to track whether the parser is inside a quoted field
* If the parser is outside quotes:

&nbsp;    , ends a field

&nbsp;    \\n ends a row

* If the parser is inside quotes:

&nbsp;    Commas and newlines are treated as normal characters

* Two double quotes ("") inside quotes are converted into a single quote (")

This logic is implemented using a simple state machine approach.



**How the CSV Writer Works**

---

* Each field is converted to a string
* A field is enclosed in double quotes if it contains:

&nbsp;    a comma

&nbsp;    a double quote

&nbsp;    a newline

* Any existing double quotes inside a field are escaped by doubling them
* Fields are joined using commas and written line by line



**Setup Instructions**
---


1. Make sure Python 3 is installed
2. Place all project files inside one folder
3. Open terminal inside the project folder
4. Run any file using:

&nbsp;     python file\_name.py



**Usage Examples**
---

Reading a CSV File



from custom\_csv\_reader import CustomCsvReader

reader = CustomCsvReader("test.csv")
for row in reader:
    print(row)

 

**Writing a CSV File**

---
from custom\_csv\_writer import CustomCsvWriter



data = \[
\["name", "age", "comment"],
\["Alice", 23, "Student"],
\["Bob, Jr", 25, "Lives in Hyderabad, India"]
]



writer = CustomCsvWriter("output.csv")
writer.write(data)


**Testing**
---


The reader and writer were tested using CSV files that include:

* Commas inside fields
* Double quotes inside fields
* Escaped quotes
* Multi-line fields
* Normal CSV data
* 

Round-trip testing was done by:



1. Writing CSV using CustomCsvWriter
2. Reading the same file using CustomCsvReader
3. Verifying that the output matches the original data


**Benchmarking**
---


A benchmark was performed using a CSV file with 10,000 rows and 5 columns.



Reader Performance

&nbsp;CustomCsvReader: 0.4106 seconds

&nbsp;Python csv.reader: 0.0204 seconds



The custom reader is slower because it is implemented completely in Python, while csv.reader is optimized in C. This performance difference is expected.



Writer Performance

&nbsp;CustomCsvWriter: 0.0258 seconds

&nbsp;Python csv.writer: 0.0246 seconds



The writer performance is very close to the standard library because writing CSV is less complex than parsing it.


**What I Learned From This Project**

---

* Why CSV parsing is harder than it looks
* How quoted fields and escaped characters work
* How iterator-based file reading works in Python
* How to implement a simple state machine
* How Python’s standard libraries are optimized for performance




**Limitations**

---

* The custom reader is slower than the built-in csv.reader
* Error handling for malformed CSV files is minimal
* This implementation focuses on correctness and learning, not production use


**Conclusion**
---


This project helped me understand CSV file handling at a much deeper level than using the built-in library. Implementing the reader and writer manually gave practical experience with file I/O, parsing logic, and performance benchmarking, which are important skills for data engineering.

