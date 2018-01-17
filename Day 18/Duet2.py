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
def rcv(que,registers,x):
    registers[x]=que[len(que)-1]
    print("Before "+str(que))
    que = que[:-1]
    print("After "+str(que))
    print(que)
def jgz(currentpos,x,y):
    if x != 0:
        print(x)
        print("jump "+str(y))
        return  ((currentpos)+y)-1
    else:
        print("skip")
        return False

def actions(instructions,theprogram,theotherprogram):

    while theprogram.x < len(instructions):
        if instructions[theprogram.x][1] not in theprogram.registers:
            theprogram.registers[instructions[theprogram.x][1]]=0

        if instructions[theprogram.x][0]=='set' or  instructions[theprogram.x][0]=='add' or instructions[theprogram.x][0]=='mul' or instructions[theprogram.x][0]=='mod' or instructions[theprogram.x][0]=='jgz':
            if instructions[theprogram.x][2] in theprogram.registers:
                thenum=int(theprogram.registers[instructions[theprogram.x][2]])
            else:
                thenum=int(instructions[theprogram.x][2])

        if instructions[theprogram.x][0]=='snd':
            if instructions[theprogram.x][1] in theprogram.registers:
                theotherprogram.que.insert(0,theprogram.registers[instructions[theprogram.x][1]])
            else:
                theotherprogramque.insert(0,(int(instructions[theprogram.x][1])))

        elif instructions[theprogram.x][0]=='set':
            setit(theprogram.registers,instructions[theprogram.x][1],thenum)
        elif instructions[theprogram.x][0]=='add':
            addit(theprogram.registers,instructions[theprogram.x][1],thenum)
        elif instructions[theprogram.x][0]=='mul':
            mul(theprogram.registers,instructions[theprogram.x][1],thenum)
        elif instructions[theprogram.x][0]=='mod':
            modit(theprogram.registers,instructions[theprogram.x][1],thenum)
        elif instructions[theprogram.x][0]=='rcv':
            if theprogram.que:
                rcv(theprogram.que,theprogram.registers,instructions[theprogram.x][1])
                theprogram.waiting=False
            else:
                theprogram.waiting=True
                break
        elif instructions[theprogram.x][0]=='jgz':
            if (jgz(theprogram.x,int(theprogram.registers[instructions[theprogram.x][1]]),thenum)):
                theprogram.x=jgz(theprogram.x,int(theprogram.registers[instructions[theprogram.x][1]]),thenum)
        theprogram.x=theprogram.x+1




thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
instructions = thedata[:-1]
for x in range(0,len(instructions)):
    instructions[x]=instructions[x].split()

class Theprogram:
    def __init__(self):
        self.registers={}
        self.que=[]
        self.waiting=False
        self.x=0

program0=Theprogram()
program1=Theprogram()
program0.registers["p"]=0
program1.registers["p"]=1

while not program0.waiting and not program1.waiting:
    actions(instructions,program0,program1)
    print("stop the one")
    actions(instructions,program1,program0)
    print("stop the two")
    break

print(program0.registers)
print(program1.registers)
