import re

thefile  = open("checksum_data.txt", "r")
spreadsheet= thefile.read()
spreadsheet=re.split(r'\n+', spreadsheet)

for x in range(0, len(spreadsheet)):
    spreadsheet[x]=re.split(r'\t+', spreadsheet[x])

thesum=0

for x in range(0, len(spreadsheet)):
    if spreadsheet[x]==['']:
        break
    biggest=int(spreadsheet[x][0])
    smallest=int(spreadsheet[x][0])
    for y in range(0, len(spreadsheet[x])):
            if int(spreadsheet[x][y])>biggest:
                biggest=int(spreadsheet[x][y])
            if int(spreadsheet[x][y])<smallest:
                smallest=int(spreadsheet[x][y])
    thesum=thesum+(biggest-smallest)

print("The Sum is: "+str(thesum))
