import sys
import numpy as np
##def makingTriangleStars():
    
print ('What is your prefered number?')
number = sys.stdin.readline()

print 'number:', number
m = int(number)
a = m+ (m-1)
n=float (a)
Matrix = [[' ' for x in range(a)] for y in range(m)]
Matrix [0][(a/2)]= '*'
for i in range (1, m):
    
    for j in range ((a/2)-i, (a/2)+i+1,2):
        #if (k%2==0):
        Matrix[i][j]='*'
        #k = k +1
for i in range (0, m):
    print Matrix [i]

# From this line below is Babak's code
import sys

print "Enter the number of rows: "
n = raw_input()
r = int(n)

c = (2*r-1)

matrix = [[' ' for j in range(0, c)] for i in range(0, r)]

# if(r%2 == 0):
l = c/2
m = c/2
matrix[0][(c/2)] = '*'
i = 1
p = c/2 - 1
while(i < r):
	l = l - 1
	m = m + 1

	for s in range(l, c):
		if(p <= m and p >= l):
			matrix[i][p] = '*'
		p = p + 2

	if(p%2 == 0):
		p = 1
	else:
		p = 0
	i += 1
		
			
# for x in range(r):
# 	print x, matrix[x]

for x in range(0, r):
	line = ""
	for y in range(0, c):
		line = line + matrix[x][y]
	print line