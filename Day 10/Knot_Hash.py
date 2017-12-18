thehash=[]
for x in range(256):
    thehash.append(x)

skip=0
current=0
selection=[]
instructions=[183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88]

first=0
second=0

print(thehash)
# print("")

for x in range(0,len(instructions)):

    for y in range(0,instructions[x]):
        selection.append(thehash[(current+y)%256])

    selection = list(reversed(selection+selection2))

    for y in range(0,instructions[x]):
        thehash[(current+y)%256]=selection[y]

    current = (current+instructions[x])+skip
    skip+=1

    current=current%256

print (thehash[0]*thehash[1])
