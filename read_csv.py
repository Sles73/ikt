import csv

paths = ['./test/C1HKVI01_T_N_clear.csv', './test/C1HRAS01_T_N.csv']

tables = []


class Table:
     def __init__(self,name):
          self.name = name
          self.columns = []
          self.data = [[]]





with open(paths[0]) as file:
        reader = csv.reader(file)
        i = 0
        new_segment = True
        new_header = False
        for row in reader:
            i += 1
            if (len(row) == 0):
                new_segment = True
                continue

            data = row[0]

            if data[0] == "#":
                 continue
            
            if new_segment:
                 print(len(tables))
                 tables.append(Table(data))
                 new_segment = False
                 new_header = True
                 continue

            if new_header:
                 tables[len(tables)-1].columns = data.split(";")
                 new_header = False
                 continue
                 


            #print(data)
            tables[len(tables)-1].data.append(data.split(";"))
            

            



            # print(row)
            # print(row[0])
            # for j in row:
            #     print(j)
            

            if i > 40:
                 break

        
for table in tables:

    print(f"Name {table.name}")

    print("headers")
    for i in table.columns:
        print(f"{i} | ", end="")

    for i in table.data:
        print("")
        for j in i:  
                print(f"{j} | ", end="")


    print("\n---------------------------------------------------\n")