


text = input("input key: ")
thesum=0
for x in range(0, len(text)):
    otherside =int((len(text)/2)+x)
    print(otherside)
    print(x)
    if ((otherside)>(len(text)-1)):
        if(text[otherside-(len(text))]==text[x]):
            thesum = thesum+int(text[x])
            print("more")
    else:
        if(text[x]==(text[otherside])):
            thesum = thesum+int(text[x])
            print("less")




    # if x==(len(text)-1):
    #     if (text[0])==(text[x]):
    #         thesum = thesum+int(text[x])
    # if (x<(len(text)-1)):
    #     if (text[x])==(text[x+1]):
    #         thesum = thesum+int(text[x])

print("result: "+str(thesum))
