thehash=[]
for x in range(256):
    thehash.append(x)

skip=0
current=0
selection=[]
instruction='183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'
length=[]

for x in range (0,len(instruction)):
    length.append(ord(instruction[x]))
length=length+[17, 31, 73, 47, 23]
print (length)


first=0
second=0

print(thehash)
for i in range (0,64):
    for x in range(0,len(length)):

        for y in range(0,length[x]):
            selection.append(thehash[(current+y)%256])

        selection = list(reversed(selection))

        for y in range(0,length[x]):
            thehash[(current+y)%256]=selection[y]

        current = (current+length[x])+skip
        skip+=1

        current=current%256


thexorlist=[]
for x in range(0,16):
    thexor=thehash[x*16]
    for y in range(1,16):
        thexor=thexor^thehash[y+(16*x)]
    thexorlist.append(thexor)
# thexorlist=[64, 7, 255]
answer=""
for x in range(0,len(thexorlist)):

    answer=answer+('%.2x' % thexorlist[x])
print (answer)
