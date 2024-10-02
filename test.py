import csv

# Replace 'utf-8' with the detected encoding if needed
with open('test/C1HKVI01_T_N.csv', mode='r', encoding='utf-8', errors='replace') as file:
    reader = csv.reader(file)
        

    with open('test/C1HKVI01_T_N_test.csv', mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        # Write rows from the original file to the new file
         
        i = 0
        for row in reader:
            writer.writerow(row)
            i += 1
            if i < 30:
                print(row)
