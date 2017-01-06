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