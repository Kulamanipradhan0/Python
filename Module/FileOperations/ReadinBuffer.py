def filecount(file):
    f = open(file,'r')
    no_of_records = 0
    for i in f:
        no_of_records += 1
    return no_of_records

buffersize = 2

filename = 'HelloWorld.txt'
line_count = filecount(filename)
counter = (line_count/2)+1

f = open(filename,'r')

for i in range(line_count):
    print(str(i+1)+'. '+f.readline())
    if (i+1) % 2 == 0:
        print ('starting line :'+str((i+2)))