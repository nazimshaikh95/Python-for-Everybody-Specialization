import re
handle = open('regex_sum_443280.txt','r')
sum = 0
valCount = 0
for i in handle:
    i = i.rstrip()
    x = re.findall('[0-9]+',i)
    for j in x:
        try:
            no = int(j)
            sum = sum + no
            valCount = valCount + 1
        except:
            continue
print('Values =',valCount,'\nSum =',sum)
