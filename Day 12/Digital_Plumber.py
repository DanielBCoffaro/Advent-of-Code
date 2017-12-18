import re


thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
thedata = thedata[:-1]

for x in range(0, len(thedata)):
    thedata[x]=thedata[x].split()
    thedata[x]= [thedata[x][0]]+thedata[x][2:]
    for y in range(0, len(thedata[x])):
        thedata[x][y]=re.sub('[^0-9]','', thedata[x][y])
        thedata[x][y]=int(thedata[x][y])

contain0=[0]
x=0
while x < len(contain0):
    c = int(contain0[x])
    currentones=thedata[c][1:]
    newones=[]
    for y in range(0,len(currentones)):
        if (currentones[y] not in contain0):
            # print(contain0)
            # print(currentones[y])
            newones.append(currentones[y])
    contain0=contain0+newones
    newones=[]
    x+=1
print(contain0)
print(len(contain0))
