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
    path = []


    for file in os.listdir(folder_path):
        if file.endswith(".zip"):
            file_path = os.path.join(folder_path, file)
            #print(file_path)
            path.append(file_path.replace(".zip",""))
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                print(f"Unzipped {file_path}")

    return path


def clear_to_folder(folder_path):
    paths = unzip_zip_files(folder_path)
    clear_path_list = []

    for i in paths:
        old_path = i
        new_path = old_path.replace(".csv","_clear.csv")
        f = open(new_path, "a")
        clear_path_list.append(new_path)
        write = read_replace_wrongs(old_path)
        #print(write)
        f.write(write)
        f.close()
        #os.remove(old_path)

    return clear_path_list

if __name__ == "__main__":
    destination = "./chmu_data_test"

    for folder in os.listdir(destination):
        print("\n" + folder)
        folder_path = os.path.join(destination, folder)
        paths = clear_to_folder(folder_path)
        
    
    