"""
05 - Data Structures (list, tuple, dict, set)
-----------------------------------------------
Python's built-in collection types for storing groups of data.
"""

# --- LIST: ordered, mutable (changeable), allows duplicates ---
tasks = ["design", "code", "test"]
tasks.append("deploy")           # add to the end
tasks.insert(1, "plan")          # insert at a specific index
tasks.remove("test")             # remove by value
last_task = tasks.pop()          # remove and return the last item
print("tasks:", tasks)
print("removed last task:", last_task)
print("slice tasks[0:2]:", tasks[0:2])   # slicing: [start:stop]
print("length:", len(tasks))

# --- TUPLE: ordered, immutable (cannot be changed after creation) ---
coordinates = (6.5244, 3.3792)  # e.g. Lagos latitude/longitude
lat, lon = coordinates           # unpacking
print("lat:", lat, "lon:", lon)
# coordinates[0] = 10  # <-- this would raise a TypeError, tuples are immutable

# --- DICT: key-value pairs, unordered before 3.7 but insertion-ordered since ---
student = {
    "name": "Opeoluwa",
    "level": 400,
    "department": "Computer Engineering",
}
student["cgpa"] = 4.5            # add a new key
print("student:", student)
print("name:", student.get("name"))
print("phone:", student.get("phone", "not provided"))  # safe lookup with default

for key in student:
    print(f"{key} -> {student[key]}")

# --- SET: unordered, unique elements only, useful for de-duplication ---
skills_a = {"python", "sql", "git"}
skills_b = {"python", "kotlin", "docker"}
print("union:", skills_a | skills_b)          # combine, no duplicates
print("intersection:", skills_a & skills_b)   # common elements
print("difference:", skills_a - skills_b)     # in a but not in b

numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_with_dupes)
print("unique_numbers:", unique_numbers)

# --- Nested structures: a list of dicts is a very common pattern ---
employees = [
    {"name": "Ada", "role": "Backend Dev"},
    {"name": "Bola", "role": "Frontend Dev"},
]
for emp in employees:
    print(f"{emp['name']} works as a {emp['role']}")
