f = open("countries.txt","r")
data = f.readlines()
f.close()
countries = []
f = open("country.txt","w")
for line in data:
    for i in line.split("option"):
        if len(i.split(">")[-1]) > 1:
            f.write(i.split(">")[-1].split("</")[0])
            # exit()
            f.write("\n")
f.close()