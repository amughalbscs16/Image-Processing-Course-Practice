from operator import xor

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
nObj = 2;
finallist = {}
for y in range(len(array1[0])):
	for x in range(len(array1)):
		if array1[x][y] == 0:
			continue;
		elif (x-1 >= 0 and y-1 >= 0 and array1[x-1][y-1] >= 2):
				array1[x][y] = array1[x-1][y-1];
		elif (x-1 >= 0 and array1[x-1][y] == 1 and y-1 >= 0 and array1[x][y-1] == 1):
			nObj+=1;
			array1[x][y] = nObj
		elif (x-1 >=0 and y-1 >= 0 and array1[x-1][y] > 1 and array1[x][y-1] > 1):
			array1[x][y] = array1[x-1][y];
		elif (x-1 >= 0 and array1[x-1][y] > 1):
			array1[x][y] = array1[x-1][y];
		elif (y-1 >= 0 and array1[x][y-1]):
			array1[x][y] = array1[x][y-1];
		if (x-1 >= 0 and y-1 >= 0):
			if not array1[x-1][y] == array1[x][y-1]:
				finallist[array1[x-1][y]] = array1[x][y-1]
for i in range(1,len(array1)-1):
	for j in range(1,len(array1[0])-1):
		print(i-1,j-1,j+1,i+1)
		array1[x][y] = max(array1[x-1][y], array1[x][y], array1[x+1][y], array1[x-1][y+1], array1[x-1][y-1], array1[x][y-1]) 

for i in range(len(array1)):
	print(array1[i])

print(finallist)

import matplotlib.pyplot as plt
plt.imshow(array1,"nipy_spectral")
plt.show()

