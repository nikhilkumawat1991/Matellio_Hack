import converter_json
def merge_csv():
    import os
    import glob
    import pandas as pd
    os.chdir("Attendance")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    time_sheet=pd.read_csv("combined_csv.csv")
    time_sheet.drop_duplicates(inplace=True)
    time_sheet.to_csv("time_sheet_emp.csv")
    time_sheet.to_json("time_sheet_emp.json")
    converter_json.convert_file()
    
