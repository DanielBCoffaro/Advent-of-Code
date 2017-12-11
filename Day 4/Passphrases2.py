import re

thefile  = open("Passphrase1.txt", "r")
spreadsheet= thefile.read()
spreadsheet=re.split(r'\n+', spreadsheet)

for x in range(0, len(spreadsheet)):
    spreadsheet[x]=spreadsheet[x].split()

thesum=0

for x in range(0, len(spreadsheet)):
    good=True
    if spreadsheet[x]==['']:
        break
    for y in range(0, len(spreadsheet[x])):
        for z in range(0, len(spreadsheet[x])):
            if(y!=z):
                if (spreadsheet[x][y] ==spreadsheet[x][z]):
                    good=False
                if (sorted(spreadsheet[x][y]) == sorted(spreadsheet[x][z])):
                    good=False

    if good:
        thesum=thesum+1
print("The Sum is: "+str(thesum))
