import os, sys

def editedi(indir):
 #   os.chdir(indir)
    edi = [ i for i in os.listdir(indir) if i.endswith(".edi")]
    return edi
    # files = os.listdir(indir)
    # for file in files:
    #     if file.endswith(".edi"):
    #         yield file

def display_files(path):
    my_files = editedi(path)
    for n in my_files:
#        print(n)
        with open(os.path.join(path, n)) as f, open("cord.txt", "w+") as z:
            reader = f.readlines()
            for lines in reader:
                lines = lines.strip()
                if lines.startswith("LAT"):
                    latname, lat = lines.split("=")
                    lines = n + " " + lat
                if lines.startswith("LONG"):
                   longname, long = lines.split("=")
                   lines = " " + long
                   my_cordinates = n, lat, long
                   for i in my_cordinates:
#                        print(long)
                        print(i)
#       
              
display_files("/home/seismics/MTPY-WINDOWS/PAKA_EDI")




    

