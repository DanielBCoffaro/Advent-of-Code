import re

# rotate right
def rotate90(pattern):
    temppattern=[]
    for x in range(0,len(pattern)):
        temprow=""
        for y in range(0,len(pattern)):
            temprow=temprow+(pattern[y][x])
        temppattern.append(temprow[::-1])
    return temppattern
# rotate right twice
def rotate180(pattern):
    temppattern=pattern
    for x in range(0,2):
        temppattern=rotate90(temppattern)
    return temppattern
# rotate right 3
def rotate270(pattern):
    temppattern=pattern
    for x in range(0,3):
        temppattern=rotate90(temppattern)
    return temppattern
# flip
def flipit(pattern):
    temppattern=[]
    for x in reversed(pattern):
        temppattern.append(x)
    return temppattern
# flip-rotate right
def flipNrotate90(pattern):
    temppattern=flipit(pattern)
    temppattern=rotate90(temppattern)
    return temppattern
# flip-rotate right twice
def flipNrotate180(pattern):
    temppattern=flipit(pattern)
    for x in range(0,2):
        temppattern=rotate90(temppattern)
    return temppattern
# flip-rotate left
def flipNrotate270(pattern):
    temppattern=flipit(pattern)
    for x in range(0,3):
        temppattern=rotate90(temppattern)
    return temppattern

def doesitmatch(pattern,inputPattern):
    if pattern==inputPattern:
        return True
    elif pattern==rotate90(inputPattern):
        return True
    elif pattern==rotate180(inputPattern):
        return True
    elif pattern==rotate270(inputPattern):
        return True
    elif pattern==flipit(inputPattern):
        return True
    elif pattern==flipNrotate90(inputPattern):
        return True
    elif pattern==flipNrotate180(inputPattern):
        return True
    elif pattern==flipNrotate270(inputPattern):
        return True
    else:
        return False


def breakitup(pattern,therules):

    if len(pattern[0])%2==0:
        size=int(len(pattern[0]))
        newpattern=[]
        thepattern=[]
        for x in range(0, size, 2):
            print("clear pattern")
            partpattern=[]
            for y in range(0, size, 2):
                partpattern=([pattern[x][y]+pattern[x][y+1],pattern[x+1][y]+pattern[x+1][y+1]])
                print(partpattern)
                for i in range(0,len(therules)):
                    if (doesitmatch(partpattern,therules[i][0])):
                        print(therules[i][1])
                        newpattern.append(therules[i][1])
            print(newpattern)


        for l in range(0,len(thepattern)):
            print(thepattern[l])
        print()



        if halfSize==1:
            part1=pattern
            for l in range(0,len(part1)):
                print(part1[l])
            print()
            for x in range(0,len(therules)):
                if (doesitmatch(pattern,therules[x][0])):
                    return therules[x][1]
        else:
            for y in range(0,halfSize):
                part1.append(pattern[y][:halfSize])
                part2.append(pattern[y][halfSize:])
            for y in range(halfSize,size):
                part3.append(pattern[y][:halfSize])
                part4.append(pattern[y][halfSize:])

            for l in range(0,len(part1)):
                print(part1[l])
            print()
            for l in range(0,len(part2)):
                print(part2[l])
            print()
            for l in range(0,len(part3)):
                print(part3[l])
            print()
            for l in range(0,len(part4)):
                print(part4[l])
            print()

            for x in range(0,len(therules)):
                if (doesitmatch(part1,therules[x][0])):
                    part1=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part2,therules[x][0])):
                    part2=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part3,therules[x][0])):
                    part3=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part4,therules[x][0])):
                    part4=therules[x][1]
                    break

            for l in range(0,len(part1)):
                print(part1[l])
            print()
            for l in range(0,len(part2)):
                print(part2[l])
            print()
            for l in range(0,len(part3)):
                print(part3[l])
            print()
            for l in range(0,len(part4)):
                print(part4[l])
            print()



            firsthalf=[]
            secondhalf=[]
            for x in range (0,len(part1)):
                firsthalf.append(part1[x]+part2[x])
            for x in range (0,len(part1)):
                secondhalf.append(part3[x]+part4[x])
            return firsthalf+secondhalf
    elif len(pattern[0])%3==0:
        thirdSize=int(len(pattern[0])/3)
        size=len(pattern[0])
        if thirdSize==1:
            # for l in range(0,len(part1)):
            #     print(part1[l])
            # print()
            for x in range(0,len(therules)):
                if (doesitmatch(pattern,therules[x][0])):
                    return therules[x][1]
        else:
            part1=[]
            part2=[]
            part3=[]
            part4=[]
            part5=[]
            part6=[]
            part7=[]
            part8=[]
            part9=[]
            for y in range(0,thirdSize):
                part1.append(pattern[y][:thirdSize])
                part2.append(pattern[y][thirdSize:thirdSize*2])
                part3.append(pattern[y][thirdSize*2:])
            for y in range(thirdSize,(thirdSize*2)):
                part4.append(pattern[y][:thirdSize])
                part5.append(pattern[y][thirdSize:thirdSize*2])
                part6.append(pattern[y][thirdSize*2:])
            for y in range((thirdSize*2),size):
                part7.append(pattern[y][:thirdSize])
                part8.append(pattern[y][thirdSize:thirdSize*2])
                part9.append(pattern[y][thirdSize*2:])

            for x in range(0,len(therules)):
                if (doesitmatch(part1,therules[x][0])):
                    part1=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part2,therules[x][0])):
                    part2=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part1,therules[x][0])):
                    part3=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part4,therules[x][0])):
                    part4=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part5,therules[x][0])):
                    part5=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part6,therules[x][0])):
                    part6=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part7,therules[x][0])):
                    part7=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part8,therules[x][0])):
                    part8=therules[x][1]
                    break
            for x in range(0,len(therules)):
                if (doesitmatch(part9,therules[x][0])):
                    part9=therules[x][1]
                    break


            firstthird=[]
            secondthird=[]
            thirdthird=[]
            for x in range (0,len(part1)):
                firstthird.append(part1[x]+part2[x]+part3[x])
            for x in range (0,len(part1)):
                secondthird.append(part4[x]+part5[x]+part6[x])
            for x in range (0,len(part1)):
                thirdthird.append(part7[x]+part8[x]+part9[x])
            return firstthird+secondthird+thirdthird
    else:
        print("error")


    for l in range(0,len(part1)):
        print(part1[l])
    print()
    for l in range(0,len(part2)):
        print(part2[l])
    print()
    for l in range(0,len(part3)):
        print(part3[l])
    print()
    for l in range(0,len(part4)):
        print(part4[l])
    print()
    wait = input("PRESS ENTER TO CONTINUE.")
    for l in range(0,len(part5)):
        print(part5[l])
    print()
    for l in range(0,len(part6)):
        print(part6[l])
    print()
    for l in range(0,len(part7)):
        print(part7[l])
    print()
    for l in range(0,len(part8)):
        print(part8[l])
    print()
    for l in range(0,len(part9)):
        print(part9[l])
    print()
    wait = input("PRESS ENTER TO CONTINUE.")

    for x in range(0,len(therules)):
        if (doesitmatch(pattern,therules[x][0])):
            pattern=therules[x][1]
            # print(pattern)
            temppattern=[]
            # print("Size "+str(int(size)))
            for i in range(0,int(size)):
                for y in range(0,len(therules[x][1])):
                    temprow = (therules[x][1][y])*int(size)
                    # print("therules: "+ str(therules[x][1][y]))
                    # print("temprow: "+ str(temprow))
                    temppattern.append(temprow)
            pattern=temppattern
            break
    for l in range(0,len(pattern)):
        print(pattern[l])
    print()



thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
therules = thedata[:-1]

for x in range(0,len(therules)):
    therules[x]=therules[x].strip().strip().split("=>")
    for y in range(0,len(therules[x])):
        therules[x][y]=therules[x][y].strip().strip().split("/")

pattern=[".#.","..#","###"]
# pattern=["###.#.#.#","#...#.#.#","#.###.#.#",".#.##.#.#",".#.##.#.#",".#..#.#.#","##.##.#.#",".####.#.#",".#..#.#.#"]


# for l in range(0,len(pattern)):
#     print(pattern[x])
# print()
for i in range(5):
    for l in range(0,len(pattern)):
        print(pattern[l])
    print()
    pattern=breakitup(pattern,therules)



thesum=0
for row in pattern:
    thesum=row.count("#")+thesum
print(thesum)
