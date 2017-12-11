import re

thefile  = open("instructions.txt", "r")
spreadsheet= thefile.read()
spreadsheet=re.split(r'\n+', spreadsheet)
# print(spreadsheet)
cur=0
oldcur=0
steps=1
while True:
    # print("before:"+str(spreadsheet[cur]))
    # print("cur:"+str(cur))
    # print("oldcur:"+str(oldcur))
    cur=cur+int(spreadsheet[cur])
    # print ("after"+str(spreadsheet[cur]))
    spreadsheet[oldcur]=int(spreadsheet[oldcur])+1
    oldcur=cur
    if cur>(len(spreadsheet)-2) or cur<0:
        # print('here')
        break
    # print("steps"+str(steps))
    steps=steps+1
    # print(spreadsheet)
    # print("")

print("The steps are: "+str(steps))
