f = open("country.txt","r")
data = f.readlines()
f.close()
f = open("country1.txt","w")
for line in data:
    arr = line.split("    ")
    string = arr[0]+"-"+arr[1]
    print(string)
    f.write(string)
f.close()