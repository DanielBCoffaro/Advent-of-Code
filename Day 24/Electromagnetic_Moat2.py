import re


def bridgeBuilder(currentlink,thegrid):
    # print(thegrid)
    # print(currentlink)
    maxweight=0
    biglist = []
    # if len(thegrid)<1:
    for x in range (0,len(thegrid)):
        if currentlink in thegrid[x]:
            templist=thegrid[:x] + thegrid[x+1:]
            # print(x)
            if thegrid[x][0]==currentlink:
                tempitem=thegrid[x][1]
            else:
                tempitem=thegrid[x][0]

                # print(templist)
            weights= thegrid[x]+bridgeBuilder(tempitem,templist)

            if len(weights) >= maxweight:
              maxweight = len(weights)
              biglist = weights

    return biglist




thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
thegrid = thedata[:-1]

for x in range(0, len(thegrid)):
    thegrid[x]=thegrid[x].split("/")
    thegrid[x][0]=int(thegrid[x][0])
    thegrid[x][1]=int(thegrid[x][1])

print(thegrid[0])
bridge=bridgeBuilder(0,thegrid)
print(bridge)
print(sum(bridge))
print(len(bridge))
