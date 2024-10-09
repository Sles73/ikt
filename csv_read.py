import csv
import string

all = ""
# Replace 'utf-8' with the detected encoding if needed
with open('test/C1HKVI01_T_N.csv', mode='r', encoding='utf-8', errors='replace') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        i += 1
        # print(row)
        # print(row[0])
        # for j in row:
        #     print(j)
        if(len(row) >0):
            data = row[0]
            printable = set(string.printable)
            data = ''.join(filter(lambda x: x in printable, data))
            print(data)
            all += data
        if i > 30:
            break

print(all)
