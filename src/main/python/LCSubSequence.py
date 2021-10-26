"""
LONGEST COMMON SUBSEQUENCE
Author: Cole Hausman
Project: CSCI 311 DNA Sequencing
- Algorithm which computes the longest common subsequence of two strings
- String inputs are case sensitive
"""

def lcSubstring(s1 , s2):
  m = len(s1) + 1
  n = len(s2) + 1
  retval = ""
  largesti = largestj = 0
  #initialize empty table
  lookup = [[0 for x in range(n)] for y in range(m)]
  #fill in lookup table
  for i in range(1, m):
    for j in range(1, n):
      if s1[i-1] == s2[j-1]:
        lookup[i][j] = lookup[i-1][j-1]+1
      #check up
      elif lookup[i-1][j] >= lookup[i][j-1]:
        lookup[i][j] = lookup[i-1][j]
      #check left
      else:
        lookup[i][j] = lookup[i][j-1]
      #update largest indicies(used to find where to start traversal)
      if lookup[i][j] >= lookup[largesti][largestj]:
          largesti = i
          largestj = j

  #traverse table
  while lookup[largesti][largestj] != 0:
    #check left
    if lookup[largesti][largestj] == lookup[largesti][largestj-1]:
      largestj = largestj - 1
    #check up
    elif lookup[largesti][largestj] == lookup[largesti-1][largestj]:
      largesti = largesti -1
    #chars are equal so update retval and modify indicies
    else:
      retval += s1[largesti-1]
      largesti = largesti - 1
      largestj = largestj - 1
  #traversed in reverse so reverse output string
  return retval[::-1]
