no=input("Enter a positive integer")
try:
    noInBinary=bin(int(no))[2:]
except:
    print("Enter a Valid Positive Number.")
    exit(1)
print("No in Binary : ",noInBinary)
listWithOnes=[]
for counter,eachNum in enumerate(noInBinary):
    if eachNum=='1':
        listWithOnes.append(counter)
listWithOnesExclFirst=listWithOnes[1:]
listWithDiff=[]
if len(listWithOnes)==1:
    print("Binary Gap is : 0")
    exit(0)
else:
    for i in range(0,len(listWithOnesExclFirst)):
        listWithDiff.append(listWithOnesExclFirst[i]-listWithOnes[i])
print("Binary Gap is : ",max(listWithDiff)-1)
