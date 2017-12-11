import re


def greaterthan(x,y):
    if x > y:
        return True
    else:
        return False
def lessthan(x,y):
    if x < y:
        return True
    else:
        return False
def greaterthanequal(x,y):
    if x >= y:
        return True
    else:
        return False
def lessthanequal(x,y):
    if x <= y:
        return True
    else:
        return False
def equal(x,y):
    if x == y:
        return True
    else:
        return False
def notequal(x,y):
    if x != y:
        return True
    else:
        return False







thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)

thevalues={}
for x in range(0, len(thedata)):
    thedata[x]=thedata[x].split()
thedata = thedata[:-1]
for x in range(0, len(thedata)):
    thevalues[thedata[x][0]]=0
themax=0
for x in range(0, len(thedata)):
    if thedata[x][5] == ">":
        if(greaterthan(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    elif thedata[x][5] == "<":
        if(lessthan(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    elif thedata[x][5] == ">=":
        if(greaterthanequal(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    elif thedata[x][5] == "<=":
        if(lessthanequal(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    elif thedata[x][5] == "==":
        if(equal(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    elif thedata[x][5] == "!=":
        if(notequal(thevalues[thedata[x][4]],int(thedata[x][6]))):
            if(thedata[x][1])=="inc":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]+int(thedata[x][2])
            if(thedata[x][1])=="dec":
                thevalues[thedata[x][0]]=thevalues[thedata[x][0]]-int(thedata[x][2])
    maximum =max(thevalues, key=thevalues.get)
    if (int(thevalues[maximum]) > themax):
        themax = (thevalues[maximum])
maximum =max(thevalues, key=thevalues.get)
print(maximum, thevalues[maximum])
print(themax)
