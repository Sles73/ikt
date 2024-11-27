import csv_read as r
import csv_unzip as u
import os

destination = "./data/"
file = r.start_csv()

# paths = u.clear_to_folder(folder_path)

# print(paths)

# for i in paths:
#     file = r.add_to_csv(i[0],file,i[1])

for folder in os.listdir(destination):
        print("\n" + folder)
        folder_path = os.path.join(destination, folder)
        paths = u.clear_to_folder(folder_path)

        for i in paths:
            print(i)
            file = r.add_to_csv(i,file,folder)

r.write("output.csv",file)