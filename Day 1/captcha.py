


text = input("input key: ")
thesum=0
for x in range(0, len(text)):
    if x==(len(text)-1):
        if (text[0])==(text[x]):
            thesum = thesum+int(text[x])
    if (x<(len(text)-1)):
        if (text[x])==(text[x+1]):
            thesum = thesum+int(text[x])

print(thesum)
