from collections import deque
import re

registers_0={"p":0,"counter":0}
registers_1={"p":1,"counter":0}
queue_for_0=deque()
queue_for_1=deque()

# runs until termination or wait state. Returns False on termination
def run_program(registers,queue_in,queue_out):

    def value(r):
        if r.isalpha():
            return registers.get(r,0)
        else:
            return int(r)

    #first_rcv_done=False
    while (registers["counter"]>=0) and (registers["counter"]<len(instructions)):
        theinstruction=instructions[registers["counter"]]

        if theinstruction[0]=="rcv":
            if len(queue_in)==0:
                return True
            registers[theinstruction[1]]=queue_in.popleft()
        if theinstruction[0]=="jgz":
            if value(theinstruction[1])>0:
                registers["counter"]+=value(theinstruction[2])
                continue
        if theinstruction[0]=="snd":
            queue_out.append(value(theinstruction[1]))
            registers["sent"]=value("sent")+1
        if theinstruction[0]=="set":
            registers[theinstruction[1]]=value(theinstruction[2])
        if theinstruction[0]=="add":
            registers[theinstruction[1]]=value(theinstruction[1])+value(theinstruction[2])
        if theinstruction[0]=="mul":
            registers[theinstruction[1]]=value(theinstruction[1])*value(theinstruction[2])
        if theinstruction[0]=="mod":
            registers[theinstruction[1]]=value(theinstruction[1])%value(theinstruction[2])
        registers["counter"]+=1
    return False

thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
instructions = thedata[:-1]
for x in range(0,len(instructions)):
    instructions[x]=instructions[x].split()

while True:
    if not run_program(registers_0,queue_for_0,queue_for_1):
        break
    if not run_program(registers_1,queue_for_1,queue_for_0):
        break
    if len(queue_for_0)==0 and len(queue_for_1)==0:
        break

print(registers_1["sent"])
