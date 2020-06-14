count = 0
total = 0
while True:
    val = input("Enter Number:")
    if(val == "done"):
          break
    try:
        fval = float(val)
    except:
        print("Invalid Input")
        continue
    count = count + 1
    total = total + fval
print(total , count , total/count)
