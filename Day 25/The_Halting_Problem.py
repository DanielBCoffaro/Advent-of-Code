
state="A"
tape=[0]
currentPos=0
current=tape[currentPos]
for x in range(0,12656374):
    current=tape[currentPos]
    if state=="A":
        if current==0:
            tape[currentPos]=1
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="B"
        else:
            tape[currentPos]=0
            if currentPos==0:
                tape.insert(0, 0)
            else:
                currentPos=currentPos-1
            state="C"
    elif state=="B":
            if current==0:
                tape[currentPos]=1
                if currentPos==0:
                    tape.insert(0, 0)
                else:
                    currentPos=currentPos-1
                state="A"
            else:
                tape[currentPos]=1
                if currentPos==0:
                    tape.insert(0, 0)
                else:
                    currentPos=currentPos-1
                state="D"
    elif state=="C":
        if current==0:
            tape[currentPos]=1
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="D"
        else:
            tape[currentPos]=0
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="C"
    elif state=="D":
        if current==0:
            tape[currentPos]=0
            if currentPos==0:
                tape.insert(0, 0)
            else:
                currentPos=currentPos-1
            state="B"
        else:
            tape[currentPos]=0
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="E"
    elif state=="E":
        if current==0:
            tape[currentPos]=1
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="C"
        else:
            tape[currentPos]=1
            if currentPos==0:
                tape.insert(0, 0)
            else:
                currentPos=currentPos-1
            state="F"
    elif state=="F":
        if current==0:
            tape[currentPos]=1
            if currentPos==0:
                tape.insert(0, 0)
            else:
                currentPos=currentPos-1
            state="E"
        else:
            tape[currentPos]=1
            if currentPos==len(tape)-1:
                tape.append(0)
            currentPos+=1
            state="A"
    # print("State: "+str(state))
    # print("Tape: "+str(tape))
    # print("Current Pos: "+str(currentPos))
    # print("--------------------")
print(tape.count(1))
