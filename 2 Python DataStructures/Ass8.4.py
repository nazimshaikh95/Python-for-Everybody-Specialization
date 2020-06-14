fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	lst.append(line.rstrip())

lst1 = list()
for val in lst:
    lst1 = lst1 + val.split()

lst2 = list()
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        lst2.append(lst1[i])

lst2.sort()
print(lst2)
