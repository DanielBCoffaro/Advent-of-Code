
thefile  = open("input.txt", "r")
# thedata= thefile.read()

inGarbage = False
skipone= False
thestring=''
sum=0
sumdagarb=0
amnt=0

while True:
    c = thefile.read(1)
    if not c:
        # print( "End of file")
        break
    if not skipone:
        if c=="!":
            skipone = True
            # print("skip")
        elif not inGarbage:
            if c=="<":
                inGarbage = True
                # print("garbage start")
            elif c=="{" :
                amnt=amnt+1
            elif c=="}":
                sum = sum+amnt
                amnt=amnt-1
        elif c==">":
            inGarbage=False
            # print("garbage end")
        else:
            sumdagarb=sumdagarb+1
    else:
        skipone=False


print(sum)
print(sumdagarb)
