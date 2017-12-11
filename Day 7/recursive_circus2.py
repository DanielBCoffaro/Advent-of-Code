import re


def towerbuilder(thedata,tower,number):
    # print (tower)
    # print (thedata)
    dex=0
    thesum=0
    number = number+1
    for x in range(0, len(thedata)):
        if thedata[x][0]==tower:
            dex=x
    if len(thedata[dex])==2:
        # print("The Weight of "+ thedata[dex][0]+" is "+str(thedata[dex][1]))
        return int(thedata[dex][1])
    else:
        valueold=0
        value=0
        for x in range(2,len(thedata[dex])):
            value=towerbuilder(thedata,thedata[dex][-1],number)
            thesum=thesum+value
            thedata[dex]=thedata[dex][:-1]
            if ((x>2)and(valueold!=value)):
                print("error with "+str(number+1)+" and the value is "+ str(value)+" and the old value is "+ str(valueold))
            valueold=value
        thesum= thesum+int(thedata[dex][1])
        # saveit.append([number,thedata[dex][0],thesum])
        print(str(number)+" the sum of "+thedata[dex][0]+" is "+str(thesum))
        number = number+1
    return thesum

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
first=[]
second=[]

for x in range(0, len(thedata)):
    thedata[x]=re.compile('\w+').findall(thedata[x])
thedata = thedata[:-1]
#
# print(thedata)
# print("")

for x in range(0, len(thedata)):
    if (len(thedata[x])>2):
        first.append(thedata[x][0])
        second.append(thedata[x][2:])
# print(first)
# print(second)
theone=''
for x in range (0, len(first)):
    notin=True
    for y in range (0,len(second)):
        if first[x] in second[y]:
            notin=False
    if(notin):
        theone=first[x]
tower=theone
towerbuilder(thedata,theone,0)
