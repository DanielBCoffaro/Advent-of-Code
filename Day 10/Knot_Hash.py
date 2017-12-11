thehash=[]
for x in range(0,5):
    thehash.append(x)

skip=0
current=0
selection=[]
instructions=[3,4,1,5]

for x in range(0,len(instructions)):
    if (current+instructions[x]>len(thehash)):
        selection = thehash[current:]
        selection = selection + thehash[0:(current+instructions[x])-len(thehash)]
        current = (current+instructions[x]-len(thehash))+skip
    else:
        selection=thehash[current:instructions[x]]
        current = (current+instructions[x])+skip



    print(skip)
    print(current)


    skip+=1

    print (selection)
    selection=list(reversed(selection))
    print (selection)
    print ("")
