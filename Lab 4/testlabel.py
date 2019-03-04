
array1 = [[1,1,0,1,1,1,0,1],
		  [1,1,0,1,0,1,0,1],
		  [1,1,1,1,0,0,0,1],
		  [0,0,0,0,0,0,0,1],
		  [1,1,1,1,0,1,0,1],
		  [0,0,0,1,0,1,0,1],
		  [1,1,1,1,0,0,0,1],
		  [1,1,1,1,0,1,1,1]];
V = 1
noV = 0
nObj = 0;
finallist = {2:3}
#First Pass
for y in range(len(array1[0])):
	for x in range(len(array1)):
		if (array1[x][y] == V):
			if x - 1 < 0 and y - 1 < 0:
				nObj+=1;
				array1[x][y] = nObj; 
			
			#If both are available
			if x - 1 >= 0 and y - 1 >= 0:
				if (array1[x-1][y] == noV and array1[x][y-1] == noV):
					nObj+=1;
					array1[x][y] = nObj;
				else:
					array1[x][y] = max(array1[x-1][y],array1[x][y-1]);
					
					
			#If only left is available
			elif x-1 >= 0:
				if (array1[x-1][y] == noV):
					nObj+=1;
					array1[x][y] = nObj;
					print(nObj)
				else:
					array1[x][y] = array1[x-1][y]
					finallist[array1[x][y]] = array1[x-1][y]

			elif y-1 >= 0:
				if array1[x][y-1] == noV:
					nObj+=1;
					array1[x][y] = nObj;
				else:
					array1[x][y] = array1[x][y-1]

			if (array1[x-1][y] > 0 and array1[x][y-1] > 0):
						finallist[array1[x][y]] = min(array1[x-1][y],array1[x][y-1])


#Second Pass
for x in range(len(array1)):
	for y in range(len(array1[0])):
		if array1[x][y] in finallist:
			array1[x][y] = finallist[array1[x][y]] 

import matplotlib.pyplot as plt
plt.imshow(array1,"nipy_spectral")
plt.show()