with open("def_paka_1") as d:
    read = d.readlines()
    for line in read:
        line = line.strip()
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace("'", '')
        print(line)
#x.write(line)
  