

a=1
b=-1
thenum=3
positive=False
seta=True
theamount=2
theamountsave=2
thecounter=2
thecounter2=1


while (thenum != 277678):
    if positive:
        if seta:
            a=a+1
            thenum=thenum+1
            # print("a+")
        else:
            b=b+1
            thenum=thenum+1
            # print("b+")
    else:
        if seta:
            a=a-1
            thenum=thenum+1
            # print("a-")
        else:
            b=b-1
            thenum=thenum+1
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

print("thenum: "+str(thenum))
print("a: "+str(a))
print("b: "+str(b))

print("thecounter: "+str(thecounter))
print("theamount: "+str(theamount))
print("")
