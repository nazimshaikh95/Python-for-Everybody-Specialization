fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
for i in fh:
    if i.startswith('From '):
        lst.append(i)

lst1 = list()
for j in lst:
    line = j.split()
    lst1.append(line[1])
for k in lst1 :
    print(k)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
