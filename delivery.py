# Algorithm for delivery!
# Author: Berin Berchmans
import matplotlib.pyplot as plt
import mdptoolbox
import numpy as np
import random 
from random import randrange


def returnTheNeighbors(ox,oy):
    gg = []
    #UP
    if(ox >= 0 and ox < worldLength):
            if(oy+1 >= 0 and oy+1 < worldBreadth):
                gg.append(finaldd2[oy+1][ox])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    # DOWN
    if(ox >= 0 and ox < worldLength):
            if(oy-1 >= 0 and oy-1 < worldBreadth):
                gg.append(finaldd2[oy-1][ox])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    # RIGHT
    if(ox+1 >= 0 and ox+1 < worldLength):
            if(oy >= 0 and oy < worldBreadth):
                gg.append(finaldd2[oy][ox+1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    # LEFT
    if(ox-1 >= 0 and ox-1 < worldLength):
            if(oy >= 0 and oy < worldBreadth):
                gg.append(finaldd2[oy][ox-1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    #Topleft
    if(ox-1 >= 0 and ox-1 < worldLength):
            if(oy-1 >= 0 and oy-1 < worldBreadth):
                gg.append(finaldd2[oy-1][ox-1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    #topright
    if(ox+1 >= 0 and ox+1 < worldLength):
            if(oy-1 >= 0 and oy-1 < worldBreadth):
                gg.append(finaldd2[oy-1][ox+1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    #bottomleft
    if(ox-1 >= 0 and ox-1 < worldLength):
            if(oy+1 >= 0 and oy+1 < worldBreadth):
                gg.append(finaldd2[oy+1][ox-1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    #bottomright
    if(ox+1 >= 0 and ox+1 < worldLength):
            if(oy+1 >= 0 and oy+1 < worldBreadth):
                gg.append(finaldd2[oy+1][ox+1])
            else:
                gg.append(-100)
    else:
            gg.append(-100)
    return gg


a = []
cc = [[9,9]]
tt = [[9,7],[8,7],[6,7],[6,8]]

ox = 0
oy = 0
oo = [[ox,oy]]

phase2 = True
if(phase2 == True):
    newobs =0
    while(newobs < 40):
        ax =randrange(10)
        ay = randrange(10)
        if(not [ax, ay] in tt and not [ax, ay] in cc and not [ax, ay] in oo ):
            tt.append([ax,ay])
            newobs = newobs + 1

         
worldBreadth = 10
worldLength = 10
 
cost = -0.04
for k in range(worldBreadth):
        for j in range(worldLength):
            if([j, k] in tt):
                a.append([-3, -3, -3, -3, -3, -3,-3,-3])
            elif([j, k] in cc):
                a.append([5, 5, 5, 5, 5, 5,5,5])
            else:
                a.append([cost, cost, cost, cost, cost, cost,cost,cost])

R3 = np.array(a)

goodaction = 1
badaction = 0
fullAction = []
rmatTotal = []
rmat = []

# calculating the transition model for actions -> right ,left, up , down, and 4 diagonal directions
for inx in range(8):
        rmatTotal = []
        rmat = []
        for actCounty in range(worldBreadth):
            for actCountx in range(worldLength):
                if([actCountx, actCounty] in tt):
                    for n in range(worldBreadth):
                        for m in range(worldLength):
                            if(actCountx == m and actCounty == n and [m, n] in tt):
                                rmat.append(1)
                            else:
                                rmat.append(0)
                elif([actCountx, actCounty] in cc):
                    for n in range(worldBreadth):
                        for m in range(worldLength):
                            if(actCountx == m and actCounty == n and [m, n] in cc):
                                rmat.append(1)
                            else:
                                rmat.append(0)
                else:
                    if(inx == 0):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(goodaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    elif(inx == 1):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty == n):
                                    rmat.append(goodaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    elif(inx == 2):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(goodaction)
                                elif(actCountx-1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    if(inx == 3):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(goodaction)
                                elif(actCountx-1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    if(inx == 4):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(goodaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    if(inx == 5):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(goodaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    if(inx == 6):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(goodaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(goodaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                else:
                                    rmat.append(0)
                    if(inx == 7):
                        for n in range(worldBreadth):
                            for m in range(worldLength):
                                if(actCountx == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty-1 == n):
                                    rmat.append(badaction)
                                elif(actCountx-1 == m and actCounty+1 == n):
                                    rmat.append(badaction)
                                elif(actCountx+1 == m and actCounty-1 == n):
                                    rmat.append(goodaction)
                                else:
                                    rmat.append(0)

                rowsum = sum(rmat)
                if(rowsum < 1):
                    done = 0
                    for jj in rmat:
                        rmat[0] = 1
                        done = 1
                if(rowsum > 1):
                    done = 0
                    for jj in rmat:

                        if(jj > 0 and done == 0):
                            rmat[rmat.index(jj)] = 0
                            done = 1
                rowsum = sum(rmat)
                rmatTotal.append(rmat)
                rmat = []
        rmatTotal2 = np.array(rmatTotal)
        fullAction.append(rmatTotal2)
        rmatTotal = []
        rmat = []

# generating utility values using value iteration - (using mdptoolbox)
mdptoolbox.util.check(fullAction, R3)
vi2 = []
vi2 = mdptoolbox.mdp.ValueIteration(fullAction, R3, 0.9)
vi2.run()

dd = []
vv = []
finaldd = []
finaldd2 = []
countd = 0
countd2 = 0


for ee in range(worldBreadth):
        for ff in range(worldLength):
            vv.append(vi2.V[countd2])
            countd2 = countd2 + 1
        finaldd2.append(vv)
        vv = []


finaldd2 = np.array(finaldd2)
# finaldd2 = np.flipud(finaldd2)


# Greedy checking the utility values of next states to find optimal action

delivered = False
cudnotdeliver  = False
thepath =[]
while(delivered == False):

    gg2 = returnTheNeighbors(ox,oy)
    max_value = max(gg2)
    max_index = gg2.index(max_value)

        # Applying the optimal action
    if(not [ox,oy] in thepath):
        thepath.append([ox,oy])        
    else:
        delivered = True
        cudnotdeliver = True
        print("Could not deliver")
    if(max_index == 0):
            # print("SOUTH")
            
            oy=oy+1
    elif(max_index == 1):
            # print("NORTH")
           
            oy=oy-1
    elif(max_index == 2):
            # print("EAST")
           
            ox=ox+1
    elif(max_index == 3):
            # print("WEST")
            
            ox=ox-1
    elif(max_index == 4):
            # print("topleft")
            
            ox=ox-1
            oy=oy-1
    elif(max_index == 5):
            # print("topright")
            
            ox=ox+1
            oy=oy-1
    elif(max_index == 6):
            # print("bottomleft")
            
            ox=ox-1
            oy=oy+1
    elif(max_index == 7):
            # print("bottomright")
            
            ox=ox+1
            oy=oy+1
    
    # if(len(thepath)>2):
    #     print(ox,oy,thepath[len(thepath)-2])
    #     if(thepath[len(thepath)-2] == [ox,oy]):
    #         delivered = True
    #         cudnotdeliver = True
    #         print("Could not deliver",ox,oy)
        
    if([ox,oy] in cc):
        delivered = True
if(cudnotdeliver == True):
    finalnode = thepath[len(thepath)-1]
    # print("final node", finalnode)
    gg3 = returnTheNeighbors(finalnode[0],finalnode[1])
    print(gg3)

k0 = (10,10)
theboard = np.zeros(k0)
for i in range(worldBreadth):
    for j in range(worldLength):
            
            if([i, j] in tt):
                
                theboard[j][i] =5
            elif([i, j] in cc):
             
                theboard[j][i] =10
            elif([i, j] in thepath):
               
                theboard[j][i] =20
            else:
                theboard[j][i]=0


print(thepath)
print("No of Steps : ",len(thepath))
row_labels = range(10)
col_labels =range(10)
plt.matshow(theboard)
plt.xticks(range(10), col_labels)
plt.yticks(range(10), row_labels)
plt.show()

