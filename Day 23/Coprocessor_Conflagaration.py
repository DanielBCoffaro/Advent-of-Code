import re

def setit(registers,x,y):
    registers[x]=y
    return registers
def addit(registers,x,y):
    registers[x]=y+registers[x]
    return registers
def subit(registers,x,y):
    registers[x]=registers[x]-(y)
    return registers
def mul(registers,x,y):
    registers[x]=y*registers[x]
    return registers
def jgz(currentpos,x,y):
    print(x)
    if x != 0:
        print("jump "+str(y))
        return  ((currentpos)+y)-1
    else:
        print("skip")
        return False

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
instructions = thedata[:-1]
for x in range(0,len(instructions)):
    instructions[x]=instructions[x].split()
registers={}

thesound=0
x=0
howmanymul=0
while x < len(instructions):
    print(instructions[x])
    if instructions[x][1] not in registers and not instructions[x][1].isdigit():
        registers[instructions[x][1]]=0

    if instructions[x][0]=='set' or  instructions[x][0]=='add' or instructions[x][0]=='mul' or instructions[x][0]=='mod' or instructions[x][0]=='sub' or instructions[x][0]=='jnz':
        if instructions[x][2] in registers:
            thenum=int(registers[instructions[x][2]])
        else:
            thenum=int(instructions[x][2])

    if instructions[x][0]=='snd':
        if instructions[x][1] in registers:
            thesound=registers[instructions[x][1]]
        else:
            thesound=int(instructions[x][1])

    elif instructions[x][0]=='set':
        setit(registers,instructions[x][1],thenum)
    elif instructions[x][0]=='add':
        addit(registers,instructions[x][1],thenum)
    elif instructions[x][0]=='sub':
        subit(registers,instructions[x][1],thenum)
    elif instructions[x][0]=='mul':
        mul(registers,instructions[x][1],thenum)
        howmanymul+=1
    elif instructions[x][0]=='jnz':
        if instructions[x][1].isdigit():
            if jgz(x,instructions[x][1],thenum):
                x=jgz(x,instructions[x][1],thenum)
        else:
            if (jgz(x,int(registers[instructions[x][1]]),thenum)):
                x=jgz(x,int(registers[instructions[x][1]]),thenum)


    x=x+1
print()
print(registers)
