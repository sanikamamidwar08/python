numbers=(1,4,8,6,7,0,5)
count_odd=0
count_even=0
r=0
for x in numbers:
    r=x%2
    if r!=0:
        print(x,"is odd.")
        count_odd+=1
    else:
        print(x,"is even.")
        count_even+=1
print("Total odd numbers=",count_odd)
print("Total odd numbers=",count_even)
    