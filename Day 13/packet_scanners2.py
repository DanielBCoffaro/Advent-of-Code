firewall=[[0,4],[1,2],[2,3],[4,4],[6,8],[8,5],[10,6],[12,6],[14,10],[16,8],[18,6],[20,9],[22,8],[24,6],[26,8],[28,8],[30,12],[32,12],[34,12],[36,12],[38,10],[40,12],[42,12],[44,14],[46,8],[48,14],[50,12],[52,14],[54,14],[58,14],[60,12],[62,14],[64,14],[66,12],[68,12],[72,14],[74,18],[76,17],[86,14],[88,20],[92,14],[94,14],[96,18],[98,18]]
# firewall=[[0,3],[1,2],[4,4],[6,4]]

caught=True
offset=0
while caught:
# while offset < 11:
    caught=False
    for x in range (0,len(firewall)):

        # print("firewall mod: "+str((firewall[x][0]+offset)%(((firewall[x][1]-1)*2))))
        if (firewall[x][0]+offset)%(((firewall[x][1]-1)*2))==0:
            # print("sum = "+str(firewall[x][1])+"*"+str(firewall[x][0]))
            caught=True
    offset+=1
print(offset-1)
