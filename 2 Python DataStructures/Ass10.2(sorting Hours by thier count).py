#name = input("Enter file:")
#if len(name) < 1 :
 #   name = "mbox-short.txt"
#handle = open(name)
handle = open('mbox-short.txt')
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
    #print(line1[5])
    hr = line1[5].split(':')
    #print(hr)
    dict1[hr[0]] = dict1.get(hr[0],0) + 1
print(dict1)

lst2 = []
lst2 = sorted(dict1.items())

for i,j in lst2:
    print(i,j)
