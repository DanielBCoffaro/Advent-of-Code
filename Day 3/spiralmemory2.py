

a=1
b=-1
thenum=2
positive=False
seta=True
theamount=2
theamountsave=2
thecounter=2
thecounter2=1
stored={'0,0':1, '1,0':1, '1,-1':2}

def thenumber(a,b):
    print(str(a)+str(b))
    thesum=0

    if (stored.get(str(a-1)+","+str(b))):
        thesum = thesum+(stored.get(str(a-1)+","+str(b)))
        print("1 "+str(thesum))
    if (stored.get(str(a-1)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a-1)+","+str(b+1)))
        print("2 "+str(thesum))
    if (stored.get(str(a-1)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a-1)+","+str(b-1)))
        print("3 "+str(thesum))
    if (stored.get(str(a)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a)+","+str(b+1)))
        print("4 "+str(thesum))
    if (stored.get(str(a)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a)+","+str(b-1)))
        print("5 "+str(thesum))
    if (stored.get(str(a+1)+","+str(b))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b)))
        print("6 "+str(thesum))
    if (stored.get(str(a+1)+","+str(b+1))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b+1)))
        print("7 "+str(thesum))
    if (stored.get(str(a+1)+","+str(b-1))):
        thesum = thesum+(stored.get(str(a+1)+","+str(b-1)))
        print("8 "+str(thesum))
    print ("the sum: "+str(thesum))
    print ("")
    return thesum


while True:
    print(stored)
    if positive:
        if seta:
            a=a+1
            stored[str(a)+","+str(b)] = thenumber(a,b)
        else:
            b=b+1
            stored[str(a)+","+str(b)] = thenumber(a,b)
    else:
        if seta:
            a=a-1
            stored[str(a)+","+str(b)] = thenumber(a,b)

        else:
            b=b-1
            stored[str(a)+","+str(b)] = thenumber(a,b)

    theamount=theamount-1

    if theamount==0:
        thecounter=thecounter-1
        thecounter2=thecounter2-1
        theamount=theamountsave
        seta=not seta
        if (thecounter==0):
            theamount=theamountsave+1
            theamountsave=theamount
            thecounter=2
        if (thecounter2==0):
            thecounter2=2
            positive= not positive
    if stored[str(a)+","+str(b)]>277678:
        print(stored[str(a)+","+str(b)])
        break
