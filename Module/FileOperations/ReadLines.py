f = open('HelloWorld.txt','r')
i=0
for lines in f:
    i=i+1;
    print(str(i)+". "+lines)

f.close()