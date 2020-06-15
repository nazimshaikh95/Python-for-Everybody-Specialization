import re
lst = list()
one = list()
numbers = list()
#line = "hello najju how 45 are you 32 jhfbvh dmbfsjh sjfbsf fwjeg 12 34 1234 jshfjg brghehg jgbe 234 14"
handle = open('regex_sum_443280.txt','r')
sum = 0
count = 0
for i in handle:
    one = i.split()
    #print(one)
    for j in one:
        try:
            no = int(j)
            numbers.append(no)
            count = count + 1
            sum = sum + no
        except:
            continue
print('Count = ',count,'Sum = ',sum)
print(numbers)
