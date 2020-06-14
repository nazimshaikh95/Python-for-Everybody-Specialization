largest = None
smallest = None
while True:
    val = input("Enter Number:")
    if(val == "done"):
          break
    try:
        fval = float(val)
    except:
        print("Invalid Input")
        continue
    if(largest is None):
        largest = fval
    if(smallest is None):
        smallest = fval
    if(fval > largest ):
        largest = fval
    if(fval < smallest ):
        smallest = fval
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
