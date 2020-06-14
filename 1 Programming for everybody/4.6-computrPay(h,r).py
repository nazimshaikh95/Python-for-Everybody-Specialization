def computepay(h,r):
    if h<=40:
        ans1 = h * r
    else:
        ans1 = h * r
        ans1 = ans1 - (h - 40) * r        #subtract extra hourly rate more than 40
        ans1 = ans1 + (h - 40) * r * 1.5  #add extra hourly rate with rate 1.5 times
    return ans1
h = float(input("Enter Hours:"))
r = float(input("Enter Rate Per Hours:"))
ans = computepay(h,r)
print("Pay",ans)
