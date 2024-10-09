import zipfile
import os
import csv
import string

def read_replace_wrongs(path):
    everithing= ""
    with open(path, mode='r', encoding='utf-8', errors='replace') as file:
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
                #print(data)
                everithing += data + "\n"
            else:
                everithing += "\n"
        
        return everithing

def unzip_zip_files(folder_path):
    """Unzips all .zip files within a specified folder.

    Args:
        folder_path (str): Path to the folder containing .zip files.
    """
    paths = []

    for file in os.listdir(folder_path):
        if file.endswith(".zip"):
            file_path = os.path.join(folder_path, file)
            print(file_path)
            paths.append(file_path.replace(".zip",""))
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                print(f"Unzipped {file_path}")
    
    return paths

# Example usage:
folder_path = "./test/"
paths = unzip_zip_files(folder_path)
print(paths)


for i in paths:
    f = open(i.replace(".csv","_v2.csv"), "a")
    write = read_replace_wrongs(i)
    print(write)
    f.write(write)
    f.close()
