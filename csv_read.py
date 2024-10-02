import csv

# Replace 'utf-8' with the detected encoding if needed
with open('test/C1HKVI01_T_N.csv', mode='r', encoding='utf-8', errors='replace') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)