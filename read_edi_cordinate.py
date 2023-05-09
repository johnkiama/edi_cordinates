import os, sys
####################################################################################################################
#This script allows user to read location of individual/batch edi file and plot their location on QGIS or google map
#how to use                                                    
#read_edi_cordinate.py >> name_of_csv_file.csv
#####################################################################################################################
def editedi(indir):
    edi = [ i for i in os.listdir(indir) if i.endswith(".edi")]
    return edi
  
def display_files(path):
    my_files = editedi(path)
    for n in my_files:
#        print(n)
        with open(os.path.join(path, n)) as f, open("cord.txt", "w+") as z:
            reader = f.readlines()
            for lines in reader:
                lines = lines.strip()
                if lines.startswith("LAT"):
                    latname = lines.split("=")
                    lat = latname[1]
                if lines.startswith("LON"): #edi eported from winglink
#                if lines.startswith("LONG"): #edi from mpower or mteditor
                    longname = lines.split("=")
                    long = longname[1]
                    print(n, lat, long)
#user to edit location of edi file 
display_files("/home/seismics/MTPY-WINDOWS/PAKA_EDI")
