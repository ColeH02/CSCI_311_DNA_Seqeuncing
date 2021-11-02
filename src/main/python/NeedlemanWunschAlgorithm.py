"""
Needleman Wunsch Algorithm
Author: Cole Hausman
Project: CSCI 311 DNA Sequencing
- Algorithm for sequence allignment
- String inputs are case sensitive
- Gap is -1 by defualt, gap cooresponds a penalty for insertions and deletion.
  The gap is set to -1 by defualt so that the algorithm prioritizes larger gaps,
  ie. longer concurrent sections of the strings.
- match and mismatch are parameters which coorespond to filling in our matrix
- Input should be in the form nw(x, y), where x and y are strings, in order to
    leave all other parameters as defaults.
- Runtime: O(mn) where m is len(x), and n is len(y)
"""

import numpy as np

def nw(x, y, match = 1, mismatch = 1, gap = -1):
  nx = len(x)
  ny = len(y)
  #matrix of zeros with dimensions (nx+1) X (ny+1)
  F = np.zeros((nx+1, ny+1))
  #Fancy pythonic language to make the first column nx+1 values ranging from 0 to -nx (ie. 0, -1, -2,...,-nx)
  F[:,0] = np.linspace(0, -nx, nx+1)
  #Same thing as above except now for the first row in our matrix
  F[0,:] = np.linspace(0, -ny, ny+1)
  #Pointers to trace through optimal allignment
  P = np.zeros((nx+1, ny+1))
  #Make the first column 3's and the first row 4's
  P[:,0] = 3
  P[0,:] = 4
  #temp vars
  t = np.zeros(3)
  for i in range(nx):
    for j in range(ny):
      #If match, increment cell, if not subtract mismatch
      if x[i] == y[j]:
        t[0] = F[i,j] + match
      else:
        t[0] = F[i, j] - mismatch
      t[1] = F[i, j+1] - gap
      t[2] = F[i+1, j] - gap
      #grab the max value from t, we do this because in our case the cell F[i,j] has three neighbooring cells and we want to grab the one with the highest value.
      tmax = np.max(t)
      F[i+1, j+1] = tmax
      for k in range(3):
        if t[k] == tmax:
          P[i+1, j+1] += (2+k)
  #Trace through optimal alignment
  i = nx
  j = ny
  rx = []
  ry = []
  while i > 0 or j > 0:
    if P[i,j] in [2, 5, 6, 9]:
      rx.append(x[i-1])
      ry.append(y[j-1])
      i-=1
      j-=1
    elif P[i,j] in [3, 5, 7, 9]:
      rx.append(x[i-1])
      #this append looks like a face
      ry.append('-')
      i-=1
    elif P[i,j] in [4, 6, 7, 9]:
      #this append also looks like a face '-'
      rx.append('-')
      ry.append(y[j-1])
      j-=1
  #reverse strings
  rx = ''.join(rx)[::-1]
  ry = ''.join(ry)[::-1]
  return '\n'.join([rx, ry])
