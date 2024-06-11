tuple1 = (1,4,9,16,25,36,49,64,81,100)
i=0
while i<= (len(tuple1)-1) :
    if(tuple1[i]==31):
        print("The number 64 is present")
        i+=1
    else:
        i +=1
        continue
print("the number is not present")