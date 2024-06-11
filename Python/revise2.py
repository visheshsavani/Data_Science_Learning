'''
print("this is the practise session\n")
a = 100

while(a>0):
    print("2 * ",a,"= ",(2*a))
    a = a -1

for i in range(1,101):
    print("2 * ",a,"= ",(2*a))
    a = a -1

for i in range (1,6):
    j =0
    while(j<i):
        print(j+1,end=" ")
        j= j+1
    print()    

a = int(input("enter the num : "))
sum  =0
for i in range(1,a+1):
    sum +=i
print(sum)

numbers = [12,75,150,180,145,525,50]
for i in numbers:
    if(i>500):
        break
    if((i%5)==0 and (i<=150)):
        print(i)
'''
'''num = 75869
count = 0
while(num > 0):
     num = num//10 ##floor division 
     count +=1
print(count)
'''
'''k = 6
for i in range(0,6):  
    for j in range(k,1,-1):
        print(j-1,end=" ")
    k = k-1
    print()
    '''
