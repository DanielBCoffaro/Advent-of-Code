

a=1
b=-1
thenum=2
positive=False
seta=True
theamount=2
theamountsave=2
thecounter=2
thecounter2=1
stored={'0,0':1, '1,1':1, '-1,1':2}

def thenumber(a,b):

    thesum=0

    if (stored.get(str(a+1)+","+str(b))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b)))
    if (stored.get(str(a)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a)+","+str(b+1)))
    if (stored.get(str(a)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a)+","+str(b-1)))
    if (stored.get(str(a+1)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b+1)))
    if (stored.get(str(a-1)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a-1)+","+str(b-1)))
    if (stored.get(str(a+1)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b-1)))
    if (stored.get(str(a-1)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a-1)+","+str(b+1)))
    print (thesum)
    print ("")
    return thesum


while (len(stored)<10):
    print(stored)
    if positive:
        if seta:
            a=a+1
            # thenum=thenum+1
            # print(stored.get(str(a+1)+","+str(b)))
            stored[str(a)+","+str(b)] = thenumber(a,b)
             # print("a+")
        else:
            b=b+1
            # thenum=thenum+1
            stored[str(a)+","+str(b)] = thenumber(a,b)
            # print("b+")
    else:
        if seta:
            a=a-1
            # thenum=thenum+1
            stored[str(a)+","+str(b)] = thenumber(a,b)
            # print("a-")
        else:
            b=b-1
            # thenum=thenum+1
            stored[str(a)+","+str(b)] = thenumber(a,b)
            # print("b-")


    theamount=theamount-1


    if theamount==0:
        thecounter=thecounter-1
        thecounter2=thecounter2-1
        theamount=theamountsave
        seta=not seta
        # print("switch the a")
        if (thecounter==0):
            theamount=theamountsave+1
            theamountsave=theamount
            thecounter=2
        if (thecounter2==0):
            thecounter2=2
            positive= not positive
            # print("switch positve")
print(abs(a)+abs(b))

    # print("thenum: "+str(thenum))
    # print("a: "+str(a))
    # print("b: "+str(b))
    #
    # print("thecounter: "+str(thecounter))
    # print("theamount: "+str(theamount))
    # print("")
