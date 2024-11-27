import csv_read as r
import csv_unzip as u

folder_path = "./chmu_data/"
file = r.start_csv()

paths = u.clear_to_folder(folder_path)

for i in paths:
    file = r.add_to_csv(i[0],file,i[1])
    

r.write("example.csv",file)