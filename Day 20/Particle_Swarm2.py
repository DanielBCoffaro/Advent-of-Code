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
for z in range(0,20000):
    for x in range(0,len(thedata)):
        # velocity adjustment


        thedata[x][1][0]=int(thedata[x][1][0])+int(thedata[x][2][0])
        thedata[x][1][1]=int(thedata[x][1][1])+int(thedata[x][2][1])
        thedata[x][1][2]=int(thedata[x][1][2])+int(thedata[x][2][2])

        # position adjustment
        thedata[x][0][0]=int(thedata[x][0][0])+int(thedata[x][1][0])
        thedata[x][0][1]=int(thedata[x][0][1])+int(thedata[x][1][1])
        thedata[x][0][2]=int(thedata[x][0][2])+int(thedata[x][1][2])

    destroy = []
    for x in range(0,len(thedata)):
        for y in range(0,len(thedata)):
            if y > x:
                if thedata[x][0] == thedata[y][0]:
                    destroy.append(y)
                    destroy.append(x)
    destroy=list(set(destroy))
    # print(destroy)
    for x in reversed(destroy):
        # print(x)
        del thedata[x]
    if len(thedata)<thelength:
        thelength=len(thedata)
        # print(thelength)

print(" ")
print(thelength)
