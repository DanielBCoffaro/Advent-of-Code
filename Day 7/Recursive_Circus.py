import re

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
first=[]
second=[]

for x in range(0, len(thedata)):
    thedata[x]=re.compile('\w+').findall(thedata[x])

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


print (theone)
