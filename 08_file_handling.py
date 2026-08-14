"""
08 - File Handling
-------------------
Reading from and writing to files on disk. The 'with' statement
(context manager) automatically closes the file for you, even
if an error occurs.
"""

file_path = "notes.txt"

# --- Writing to a file (overwrites if it already exists) ---
with open(file_path, "w") as f:
    f.write("Line 1: Hello, file!\n")
    f.write("Line 2: Python makes file handling easy.\n")

# --- Appending to a file (adds to the end, doesn't overwrite) ---
with open(file_path, "a") as f:
    f.write("Line 3: This line was appended.\n")

# --- Reading the whole file at once ---
with open(file_path, "r") as f:
    content = f.read()
print("--- full content ---")
print(content)

# --- Reading line by line (memory-efficient for large files) ---
print("--- line by line ---")
with open(file_path, "r") as f:
    for line in f:
        print(line.strip())  # .strip() removes the trailing newline

# --- Reading all lines into a list ---
with open(file_path, "r") as f:
    lines = f.readlines()
print("number of lines:", len(lines))

# --- Working with CSV-style data (simple, no external library) ---
csv_path = "students.csv"
students = [
    ("Ada", 400, 4.5),
    ("Bola", 300, 3.8),
    ("Chike", 200, 4.2),
]

with open(csv_path, "w") as f:
    f.write("name,level,cgpa\n")  # header row
    for name, level, cgpa in students:
        f.write(f"{name},{level},{cgpa}\n")

with open(csv_path, "r") as f:
    header = f.readline().strip().split(",")
    print("header:", header)
    for line in f:
        values = line.strip().split(",")
        print(dict(zip(header, values)))

# Cleaning up the demo files
import os
os.remove(file_path)
os.remove(csv_path)
print("Demo files cleaned up.")
