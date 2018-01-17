import re

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
thedata = thedata[:-1]

coord=[thedata[0].index('|'),0]
letters=[]
direction="d"
steps=0
while True:
    steps+=1
    if direction =="d":
        coord[1]+=1
    elif direction =="u":
        coord[1]=coord[1]-1
    elif direction =="l":
        coord[0]=coord[0]-1
    elif direction =="r":
        coord[0]+=1

    # print("the direct: "+str(direction))
    # print("the coord: "+str(coord))
    # print("the current: "+str(thedata[coord[1]][coord[0]]))

    if thedata[coord[1]][coord[0]]=="+":
        if direction =="d" or direction =="u":
            if thedata[coord[1]][coord[0]-1]!=" ":
                direction="l"
            elif thedata[coord[1]][coord[0]+1]!=" ":
                direction="r"
            else:
                print("error")
        elif direction =="l" or direction =="r":
            if thedata[coord[1]-1][coord[0]]!=" ":
                direction="u"
            elif thedata[coord[1]+1][coord[0]]!=" ":
                direction="d"
            else:
                print("error")
    elif thedata[coord[1]][coord[0]]==" ":
        print("break")
        break
    elif thedata[coord[1]][coord[0]]!="|" and thedata[coord[1]][coord[0]]!="-":
        letters.append(thedata[coord[1]][coord[0]])
        print("added")
        print(" ")


print(steps)
print(''.join(letters))
