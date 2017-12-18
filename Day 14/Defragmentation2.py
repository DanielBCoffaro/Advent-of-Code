import sys

def numberchanger(x,y,thenum):

    try:
        thelist[x][y]=thenum
    except:
        print(x)
        print(y)



    try:
        # print(str(x)+" "+str(y))
        # print("y-1>=0:")
        if thelist[x][y-1]=='a':
            numberchanger(x,(y-1),thenum)
    except:
        print(x)
        print(y)

    try:
        # print(str(x)+" "+str(y))
        # print("y+1<len(thelist[x]):")
        if thelist[x][y+1]=='a':
            numberchanger(x,(y+1),thenum)
    except:
        print(x)
        print(y)
    try:
        # print(str(x)+" "+str(y))
        # print("x+1<len(thelist):")
        if thelist[x+1][y]=='a':
            numberchanger((x+1),y,thenum)
    except:
        print(x)
        print(y)
    try:
        # print(str(x)+" "+str(y))
        # print("x-1>=0:")
        if thelist[x-1][y]=='a':
            numberchanger((x+1),y,thenum)
    except:
        print(x)
        print(y)


number=0
instructio1n='jxqlasbh-'
thelist=[]
for w in range(0,128):
    thehash=[]
    for x in range(256):
        thehash.append(x)

    skip=0
    current=0
    selection=[]
    length=[]

    instruction=instructio1n+str(w)
    # print(instruction)
    for x in range (0,len(instruction)):
        length.append(ord(instruction[x]))
    length=length+[17, 31, 73, 47, 23]

    first=0
    second=0

    # print(thehash)
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
    answer=bin(int(answer, 16))[2:]
    thelist.append(answer)
thenumber=0

thenum=1

for x in range (0,len(thelist)):
    thelist[x]=thelist[x].replace('1','a')
    thelist[x]=list(thelist[x])

for x in range (0,len(thelist)):
    for y in range(0,len(thelist[x])):
        if thelist[x][y]=='a':
            numberchanger(x,y,thenum)
            thenum+=1
sys.stdout = open("file.txt", "w+")
for x in range (0,len(thelist)):
    print ("the num:"str(thenum))
