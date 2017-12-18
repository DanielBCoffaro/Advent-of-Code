# Gen_A_Val=65
# Gen_B_Val=8921
Gen_A_Val=634
Gen_B_Val=301

matching=0
index=0
# while index<5:
while index<= 40000000:
    Gen_A_Val=Gen_A_Val*16807
    Gen_B_Val=Gen_B_Val*48271





    Gen_A_Val=Gen_A_Val % 2147483647
    Gen_B_Val=Gen_B_Val % 2147483647
    Gen_A_Val=Gen_A_Val % 2147483647
    Gen_B_Val=Gen_B_Val % 2147483647
    # print(str(Gen_A_Val)+" "+str(Gen_B_Val))

    index+=1
    # print('{0:16b}'.format(Gen_A_Val)[-16:])
    # print('{0:16b}'.format(Gen_B_Val)[-16:])


    if('{0:16b}'.format(Gen_A_Val)[-16:]=='{0:16b}'.format(Gen_B_Val)[-16:]):
        matching+=1
    # print("")

print(matching)
