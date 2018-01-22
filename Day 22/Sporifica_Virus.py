import re
import math

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
thegrid = thedata[:-1]

for x in range(0, len(thegrid)):
    thegrid[x]=list(thegrid[x])

# location=[math.ceil(len(thegrid)/2),math.ceil(len(thegrid)/2)]
location=[12,12]
print(location)
node=thegrid[location[0]][location[1]]
direction="U"
howmany=0


# for x in range(0, len(thegrid)):
#     print(thegrid[x])
# print (location)
# print (node)
# print()

for i in range(10000):
    node=thegrid[location[0]][location[1]]

    # print(node)

    if node=="#":
        #infected
        thegrid[location[0]][location[1]]="."
        if direction=="U":
            direction="R"
        elif direction=="R":
            direction="D"
        elif direction=="D":
            direction="L"
        elif direction=="L":
            direction="U"
        else:
            print("ERROR")
    elif node==".":
        #clean
        thegrid[location[0]][location[1]]="#"
        howmany+=1
        if direction=="U":
            direction="L"
        elif direction=="R":
            direction="U"
        elif direction=="D":
            direction="R"
        elif direction=="L":
            direction="D"
        else:
            print("ERROR")
    else:
        print("ERROR")

    if direction=="U":
        if location[0]==0:
            thegrid.insert(0,["."]*len(thegrid[0]))
        else:
            location[0]=location[0]-1
    elif direction=="R":
        if location[1]==len(thegrid[0])-1:
            for x in range(0,len(thegrid)):
                thegrid[x].append(".")
            location[1]=location[1]+1
        else:
            location[1]=location[1]+1
    elif direction=="D":
        if location[0]==len(thegrid)-1:
            thegrid.append(["."]*len(thegrid[0]))
            location[0]=location[0]+1
        else:
            location[0]=location[0]+1
    elif direction=="L":
        if location[1]==0:
            for x in range(0,len(thegrid)):
                thegrid[x].insert(0,".")
        else:
            location[1]=location[1]-1
    else:
        print("ERROR")
    # before=thegrid[location[0]][location[1]]
    # thegrid[location[0]][location[1]]="0"
    # for x in range(0, len(thegrid)):
    #     print("".join(thegrid[x]))
    # print (direction)
    # print (location)
    # print()
    # thegrid[location[0]][location[1]]=before
print(howmany)
