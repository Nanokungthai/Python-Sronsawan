num = int(input("enter quantity of data : "))
numtotal = []
for i in range(num): 
    data = int(input("enter data : ")) 
    numtotal += [data]    
numtotal.sort()
print(numtotal)