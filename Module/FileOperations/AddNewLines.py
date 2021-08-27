f = open('HelloWorld.txt','a')

f.write('\nLine 7: Hello World')
f.close()

file = open('HelloWorld.txt','r')
print(file.read())
file.close()

