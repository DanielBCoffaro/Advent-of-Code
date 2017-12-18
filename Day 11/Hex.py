import re

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r',', thedata)
thedata[-1]=thedata[-1].replace("\n","")
# print(thedata)

placement=[0,0]
col=True

for x in range (0,len(thedata)):
    if col:
        if thedata[x]=='n':
            placement[1]=placement[1]-1
        if thedata[x]=='ne':
            placement[0]=placement[0]-1
            placement[1]=placement[1]-1
            col= not col
        if thedata[x]=='nw':
            placement[0]=placement[0]+1
            placement[1]=placement[1]-1
            col= not col
        if thedata[x]=='s':
            placement[1]=placement[1]+1
        if thedata[x]=='se':
            placement[0]=placement[0]-1
            col= not col
        if thedata[x]=='sw':
            placement[0]=placement[0]+1
            col= not col
    elif not col:
        if thedata[x]=='n':
            placement[1]=placement[1]-1
        if thedata[x]=='ne':
            placement[0]=placement[0]-1
            col= not col
        if thedata[x]=='nw':
            placement[0]=placement[0]+1
            col= not col
        if thedata[x]=='s':
            placement[1]=placement[1]+1
        if thedata[x]=='se':
            placement[0]=placement[0]-1
            placement[1]=placement[1]+1
            col= not col
        if thedata[x]=='sw':
            placement[0]=placement[0]+1
            placement[1]=placement[1]+1
            col= not col

x = placement[0]
z = placement[1] - (placement[0] - (placement[0]&1)) / 2
y = -x-z

distance=((abs(x-0))+((abs(y-0)))+(abs(z-0)))/2

print (placement)
print (distance)
