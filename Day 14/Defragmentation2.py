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
instructio1n='jxqlasbh'
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

que=[]
count=0
for x in range(0,len(thelist)):
    for y in range(0,len(thelist[x])):
        if thelist[x][y]=="1":
            print("here")
            que.append([x,y])
            print(que)
            while que:
                print(que)
                current=que.pop()
                i=current[0]
                j=current[1]
                print(i)
                print(j)
                if i!=0:
                    if thelist[i-1][j]==1:
                        que.append([i-1,j])
                print(i)
                print(j)
                print((len(thelist))-1)
                if i!=(len(thelist))-1:
                    if thelist[i+1][j]==1:
                        que.append([i+1,j])
                if j!=(len(thelist[i]))-1:
                    if thelist[i][j+1]==1:
                        que.append([i,j+1])
                if j!=0:
                    if thelist[i][j-1]==1:
                        que.append([i,j-1])
                thelist[i][j]=="a"
            count+=1
print(count)
