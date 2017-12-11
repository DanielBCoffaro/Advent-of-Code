

data = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
# data = [0, 2, 7, 0 ]
old=[]
steps=0


while True:
    old.append(data[:])
    thedex=data.index(max(data))
    ammount=data[thedex]
    data[thedex]=0
    while ammount>0:
        thedex=thedex+1
        if (thedex >= len(data)):
            thedex=0
        data[thedex]=data[thedex]+1
        ammount=ammount-1
    steps = steps+1
    if data in old:
        old.index(data)
        print ("difference in steps: " +str(steps - old.index(data)))
        # print(old)
        break

print("steps: "+str(steps))
