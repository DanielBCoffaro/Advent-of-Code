
thebuffer=[0]
thepos=0
jump=329
thenum=0
print(thebuffer)
for x in range(1,50000001):
    thepos=(1+(thepos+jump)%x)
    if thepos==1:
        thenum=x
print (thenum)
