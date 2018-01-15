import re

def setit(registers,x,y):
    registers[x]=y
    return registers
def addit(registers,x,y):
    registers[x]=y+registers[x]
    return registers
def mul(registers,x,y):
    registers[x]=y*registers[x]
    return registers
def modit(registers,x,y):
    registers[x]=registers[x]%y
    return registers
def rcv(sound,x):
    if x != 0:
        return sound
    else:
        print("skip")
        return False
def jgz(currentpos,x,y):
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
while x < len(instructions):
    print(instructions[x])
    if instructions[x][1] not in registers:
        registers[instructions[x][1]]=0

    if instructions[x][0]=='set' or  instructions[x][0]=='add' or instructions[x][0]=='mul' or instructions[x][0]=='mod' or instructions[x][0]=='jgz':
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
    elif instructions[x][0]=='mul':
        mul(registers,instructions[x][1],thenum)
    elif instructions[x][0]=='mod':
        modit(registers,instructions[x][1],thenum)
    elif instructions[x][0]=='rcv':
        if (rcv(thesound,int(registers[instructions[x][1]]))):
            print (thesound)
            break
    elif instructions[x][0]=='jgz':
        if (jgz(x,int(registers[instructions[x][1]]),thenum)):
            x=jgz(x,int(registers[instructions[x][1]]),thenum)

    x=x+1x)
