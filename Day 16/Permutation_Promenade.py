
programs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
# programs=['a','b','c','d','e']
print(programs)

thefile  = open("input.txt", "r")
thedata= thefile.read()
commands = thedata.strip().split(',')

def spin(programs,k):
    programs=programs[-k:]+programs[:-k]
    return programs

def exchange(programs,a,b):
    swapA=programs[a]
    swapB=programs[b]
    programs[a]=swapB
    programs[b]=swapA
    return programs

def partner(programs,a,b):
    swapA=programs.index(a)
    swapB=programs.index(b)
    programs[swapA]=b
    programs[swapB]=a
    return programs


for command in commands:
    if command[0] == "s":
        # print(command)
        programs=spin(programs,int(command[1:]))
    if command[0] == "x":
        command=command[1:].split('/')
        programs=exchange(programs,int(command[0]),int(command[1]))
    if command[0] == "p":
        command=command[1:].split('/')
        programs=partner(programs,command[0],command[1])
print(''.join(programs))
