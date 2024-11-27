import csv



class Table:
    def __init__(self,name):
          self.name = name
          self.columns = []
          self.data = [[]]







def csv_to_table_class(path,tables,limiter=False):
    with open(path) as file:
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
                    
                tables[len(tables)-1].data.append(data.split(";"))
                
                #development breake for smaller printout
                if i > 40 and limiter:
                    break

def printount_tables(tables_in):
    for table in tables_in:

        print(f"Name {table.name}")

        print("headers")
        for i in table.columns:
            print(f"{i} | ", end="")

        for i in table.data:
            print("")
            for j in i:  
                    print(f"{j} | ", end="")

        print("\n---------------------------------------------------\n")

def get_meta(tables):
    for i in tables:
        if i.name == "METADATA":
            print(i.data[1])
            id = i.data[1][0]
            stanice = i.data[1][1]
            zemDelka = i.data[1][4]
            zemSirka = i.data[1][5]
            
        if i.name == "DATA":
            header = i.columns
            data = i.data
            data.pop(0)

    return [id,stanice,zemDelka,zemSirka,header,data]

def make_blob(id,stanice,zemDelka,zemSirka,header,data,mesto,data_old):
    print(f"id: {id}")
    print(f"stanice: {stanice}")
    print(f"zemDelka: {zemDelka}")
    print(f"zemSirka: {zemSirka}")
    print(f"header: {header}")

    
    new_data = [id,stanice,zemDelka,zemSirka,mesto]

    final_data = []
    

    final_data.append(header)
    print(final_data)
    
    print(data)

    for i in data:
        for j in new_data:
            i.append(j)
        final_data.append(i)
        print(i)

    for i in final_data:
        data_old.append(i)

    return data_old





def start_blob(id,stanice,zemDelka,zemSirka,header,data,mesto):
    new_columns = ["id","stanice","zemepisna delka", "zemepisna sirka", "mesto"]
    for i in new_columns:
        header.append(i)
    
    final_data = []
    final_data.append(header)
    print(final_data)

    return final_data
    
 
def write(file_name,data):
    # Create and write to the CSV file with a semicolon delimiter
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        # Write the data row by row
        writer.writerows(data)

def start_csv(r_path):
    tables = []
    csv_to_table_class(r_path,tables,True)
    #printount_tables(tables)
    meta = get_meta(tables)
    file = start_blob(*meta,"Plzen")
    return file

def add_to_csv(path,old_data):
    tables = []
    csv_to_table_class(path,tables,True)
    #printount_tables(tables)
    meta = get_meta(tables)
    new_data = make_blob(*meta,"Plzen",old_data)
    return new_data




if __name__ == "__main__":
    paths = ['./test/C1HKVI01_T_N_clear.csv', './test/C1HRAS01_T_N_clear.csv']
    
    file = start_csv(paths[0])

    

    for i in paths:
        file = add_to_csv(i,file)

    write("example.csv",file)
    


