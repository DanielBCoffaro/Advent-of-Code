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
print(thedata[0][2][0])
print(thedata[0][2][1])
print(thedata[0][2][2])

thesmallestaccel=(abs(int(thedata[0][2][0]))+abs(int(thedata[0][2][1]))+abs(int(thedata[0][2][2])))
theparticle=0
print(thesmallestaccel)
for x in range(0,len(thedata)):
    if((abs(int(thedata[x][2][0]))+abs(int(thedata[x][2][1]))+abs(int(thedata[x][2][2])))<=thesmallestaccel):
        thesmallestaccel=(abs(int(thedata[x][2][0]))+abs(int(thedata[x][2][1]))+abs(int(thedata[x][2][2])))
        theparticle=x
        print(str(x)+" "+str(thesmallestaccel)+" "+str((abs(int(thedata[x][1][0]))+abs(int(thedata[x][1][1]))+abs(int(thedata[x][1][2])))))

print(theparticle)
