import re

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
thedata = thedata[:-1]


acel=[]
for x in range(0,len(thedata)):
    thedata[x]=thedata[x].strip().split(", ")
    thedata[x][0]=thedata[x][0][3:-1]
    thedata[x][1]=thedata[x][1][3:-1]
    thedata[x][2]=thedata[x][2][3:-1]
    thedata[x][0]=thedata[x][0].strip().split(",")
    thedata[x][1]=thedata[x][1].strip().split(",")
    thedata[x][2]=thedata[x][2].strip().split(",")
print(thedata[0])
# print(thedata[0][0])
# print(thedata[1][0])
# print(thedata[2][0])
thelength=len(thedata)
for z in range(0,100):
    positions = {}
    delete = []
    for i, d in enumerate(thedata):
        # velocity adjustment
        thedata[i][1][0]=int(thedata[i][1][0])+int(thedata[i][2][0])
        thedata[i][1][1]=int(thedata[i][1][1])+int(thedata[i][2][1])
        thedata[i][1][2]=int(thedata[i][1][2])+int(thedata[i][2][2])
        # position adjustment
        thedata[i][0][0]=int(thedata[i][0][0])+int(thedata[i][1][0])
        thedata[i][0][1]=int(thedata[i][0][1])+int(thedata[i][1][1])
        thedata[i][0][2]=int(thedata[i][0][2])+int(thedata[i][1][2])

        if tuple(d[0]) in positions:
            delete += [i, positions[tuple(d[0])]]
        else:
            positions[tuple(d[0])] = i
            print (positions)
    thedata = [d for i, d in enumerate(thedata) if i not in delete]
    print(len(thedata))
