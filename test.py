import csv

# Data to write to the CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Specify the file name
file_name = "example_semicolon.csv"

# Create and write to the CSV file with a semicolon delimiter
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    # Write the data row by row
    writer.writerows(data)

print(f"CSV file '{file_name}' with semicolon separator created successfully!")
