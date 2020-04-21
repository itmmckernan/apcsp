from matplotlib import cm
from matplotlib.colors import ListedColormap
from pyvox.parser import VoxParser
import matplotlib.pyplot as plt
import numpy as np
import math

map = VoxParser("C:/Users/itmm/Documents/Ap Principals Mpas/Stress Test.vox").parse()
array = map.to_dense()
print(array.shape)
voxelList = array.tolist()
newList = []
outputString = ""
for z in range(len(voxelList)):
    newZ = []
    for x in range(len(voxelList[z])):
        newX = voxelList[z][x]
        if sum(voxelList[z][x]) == 0:
            newX = []
            newZ.append(newX)
            continue
        indexItem = 0
        for item in voxelList[z][x]:
            newItem = item
            outputString = ""
            if item != 0:

                # 1.2
                if z != len(voxelList) - 1 and voxelList[z + 1][x][indexItem] != 0:
                    outputString = outputString + "0"
                else:
                    outputString = outputString + "1"

                #1.1
                if z != 0 and voxelList[z - 1][x][indexItem] != 0:
                    outputString = outputString+"0"
                else:
                    outputString = outputString+"1"

                    # 2.1
                if indexItem != 0 and voxelList[z][x][indexItem - 1] != 0:
                    outputString = outputString + "0"
                else:
                    outputString = outputString + "1"

                # 2.2
                if indexItem != len(voxelList[z][x]) - 1 and voxelList[z][x][indexItem + 1] != 0:
                  outputString = outputString + "0"
                else:
                   outputString = outputString + "1"

                    # 3.1


                if x != 0 and voxelList[z][x - 1][indexItem] != 0:
                    outputString = outputString + "0"
                else:
                    outputString = outputString + "1"

                    # 3.2
                if x != len(voxelList[z]) - 1 and voxelList[z][x + 1][indexItem] != 0:
                    outputString = outputString + "0"
                else:
                    outputString = outputString + "1"







                newItem = int(outputString, 2)
            newX[indexItem] = newItem
            indexItem += 1
        newZ.append(newX)
    newList.append(newZ)
print(newList, end="", sep="")
print(",")