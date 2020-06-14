# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fval = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    sval = line[20:]
    fval = fval + float(sval)
    count = count + 1
print("Average spam confidence:",fval/count)

