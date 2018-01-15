
thebuffer=[0]
thepos=0
jump=329
print(thebuffer)
for x in range(1,2018):
    # print((thepos+jump)%len(thebuffer))
    thepos=(1+(thepos+jump)%len(thebuffer))
    thebuffer.insert(thepos, x)
print (thebuffer[thepos+1])
