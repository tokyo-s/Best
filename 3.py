path1 = "D:\\programming\\Python\\originale.txt"
path2 = "D:\\programming\\Python\\really_shuffled.txt"

key=''
with open(path2,'r') as f:
    line = f.readline()
    while line:
        with open(path1,'r') as f1:
            line1 = f1.readline()
            while line1:
                print(sorted(line)," ",sorted(line1))
                if(sorted(line)==sorted(line1)):
                    key+=line1
                line1 = f1.readline()
        line = f.readline()

print(key)
