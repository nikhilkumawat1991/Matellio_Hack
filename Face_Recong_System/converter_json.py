import csv
import json, shutil
#import os
#os.chdir("Attendance")
path="/home/pi/Desktop/Face_Recong_System/Attendance/"
def convert_file(csv_file=path+"time_sheet_emp.csv"):
    with open(csv_file, encoding="utf-8") as csvfile:
        csvReader = csv.DictReader(csvfile)
        with open(path+"check.log", 'w') as file:
            file.write("")
        for rows in csvReader:
            var = {}
            var["Id"]=rows["Id"]
            var["Name"]=rows["Name"]
            var["Time"]=rows["Time"]
            #print(rows)
            f = open(path+"check.log", "a")
            f.write(str(dict(var)).replace("'", '"')+"\n")
            f.close()
    shutil.copy2(path+'check.log',path+'text.log')
    

convert_file()
