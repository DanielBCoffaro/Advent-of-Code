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

allthecontain=[]

contain=[0]
x=0
while x < len(contain):
    c = int(contain[x])
    currentones=thedata[c][1:]
    newones=[]
    for y in range(0,len(currentones)):
        if (currentones[y] not in contain):
            # print(contain)
            # print(currentones[y])
            newones.append(currentones[y])
    contain=contain+newones
    newones=[]
    x+=1
allthecontain.append(contain)
print(allthecontain)

run = False
for i in range(1,len(thedata)):
    contain=[]


    if not (any(thedata[i][0] in k for k in allthecontain)):
        # print (str(thedata[i][0])+" - "+str(allthecontain[k]))
        # print(allthecontain)
        contain=[i]
        x=0
        while x < len(contain):
            c = int(contain[x])
            currentones=thedata[c][1:]
            newones=[]
            for y in range(0,len(currentones)):
                if (currentones[y] not in contain):
                    # print(contain)
                    # print(currentones[y])
                    newones.append(currentones[y])
            contain=contain+newones
            newones=[]
            x+=1
        allthecontain.append(contain)
    run = False
    # print(allthecontain)
# print(allthecontain)
print(len(allthecontain))
# print(len(contain0))
