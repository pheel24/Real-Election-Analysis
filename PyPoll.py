#dependencies
import csv
import os
# variable to load file
file_to_load = os.path.join("resources", "election_results.csv")
# variable to save file
file_to_save=os.path.join("analysis","election_analysis.txt")
#open results and read file
with open(file_to_load) as election_data:
    #read file object
    file_reader=csv.reader(election_data)
    #print header
    headers=next(file_reader)
    print(headers)
    

