import csv
import zipfile
import os

def unzip_zip_files(folder_path):
    """Unzips all .zip files within a specified folder.

    Args:
        folder_path (str): Path to the folder containing .zip files.
    """
    paths = []

    for file in os.listdir(folder_path):
        if file.endswith(".zip"):
            file_path = os.path.join(folder_path, file)
            paths.append(file_path)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                print(f"Unzipped {file_path}")
            
            with open(file_path, 'r+') as csvfile:
                csvreader = csv.reader(csvfile)
                csvwriter = csv.writer(csvfile)

                for row in csvreader:
                    new_row = [item.replace('�', '') for item in row]
                    csvwriter.writerow(new_row)
    
    return paths

# Example usage:
folder_path = "test"
paths = unzip_zip_files(folder_path)

print(paths)
for i in paths:
    print(i)


