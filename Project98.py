upper = int(input("Enter the Upper Limit:"))
lower = int(input("Enter the Lower Limit:"))
n = int(input("Enter the Number to be divided with:"))

for i in range(lower, upper+1):
    if(i%n == 0):
        print(i)