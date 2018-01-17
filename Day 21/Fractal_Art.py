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
    print("start")
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
        # wait = input("PRESS ENTER TO CONTINUE.")
        return False


def breakitup(pattern):
    if len(pattern[0])%2==0:
        size=len(pattern[0])/2
        temppattern=[pattern[0][:2],pattern[1][:2]]
    elif len(pattern[0])%3==0:
        size=len(pattern[0])/3
        temppattern=[pattern[0][:3],pattern[1][:3],pattern[2][:3]]
    else:
        print("error")
    return(size, temppattern)





thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
therules = thedata[:-1]

for x in range(0,len(therules)):
    therules[x]=therules[x].strip().strip().split("=>")
    for y in range(0,len(therules[x])):
        therules[x][y]=therules[x][y].strip().strip().split("/")

pattern=[".#.","..#","###"]

# for x in range(0,len(pattern)):
#     print(pattern[x])
# print()
print(pattern)

broken=breakitup(pattern)
size=broken[0]
pattern=broken[1]
temppattern=[]
print(pattern)


for x in range(0,len(therules)):
    if (doesitmatch(pattern,therules[x][0])):
        pattern=therules[x][1]
        temppattern=[]
        for y in range(0,int(size)):
            temprow=[]
            for z in range(0,int(size)):
                temprow = therules[x][1][z]+temprow
            temppattern.append(temprow)
