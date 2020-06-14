name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

lst = []
for i in handle:
    lst.append(i)

lst1 = []
for line in lst:
    if line.startswith('From '):
       lst1.append(line.rstrip())
#print(lst1)
        
dict1 = dict()
for line in lst1:
    line1 = line.split()
    #print(line1[1])
    dict1[line1[1]] = dict1.get(line1[1],0) + 1
print(dict1)

bigword = None
bigcount = None
for bigw,bigc in dict1.items():
    if bigcount is None or bigc > bigcount :
        bigcount = bigc
        bigword = bigw
print(bigword,bigcount)
