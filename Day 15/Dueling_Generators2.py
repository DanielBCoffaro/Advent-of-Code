# Gen_A_Val=65
# Gen_B_Val=8921
Gen_A_Val=634
Gen_B_Val=301
Gen_A_judge=[]
Gen_B_judge=[]
matching=0

# while len(Gen_A_judge)<= 1057 or len(Gen_B_judge)<= 1057:
while len(Gen_A_judge)<= 5000000 or len(Gen_B_judge)<= 5000000:
    Gen_A_Val=Gen_A_Val*16807
    Gen_B_Val=Gen_B_Val*48271

    Gen_A_Val=Gen_A_Val % 2147483647
    Gen_B_Val=Gen_B_Val % 2147483647
    Gen_A_Val=Gen_A_Val % 2147483647
    Gen_B_Val=Gen_B_Val % 2147483647

    if Gen_A_Val%4==0:
        Gen_A_judge.append(Gen_A_Val)
    if Gen_B_Val%8==0:
        Gen_B_judge.append(Gen_B_Val)

print(len(Gen_A_judge))
print(len(Gen_B_judge))
if len(Gen_A_judge)>len(Gen_B_judge):
    for m in range (0, len(Gen_B_judge)):
        # print(str(Gen_A_judge[m])+" "+str(Gen_B_judge[m]))
        if('{0:16b}'.format(Gen_A_judge[m])[-16:]=='{0:16b}'.format(Gen_B_judge[m])[-16:]):
            matching+=1
else:
    for m in range (0, len(Gen_A_judge)):
        # print(str(Gen_A_judge[m])+" "+str(Gen_B_judge[m]))
        if('{0:16b}'.format(Gen_A_judge[m])[-16:]=='{0:16b}'.format(Gen_B_judge[m])[-16:]):
            matching+=1

print(matching)
