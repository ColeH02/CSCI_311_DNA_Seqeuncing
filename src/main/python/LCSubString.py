"""
LONGEST COMMON SUBSTRING
Author: Cole Hausman
Project: CSCI 311 DNA Sequencing
- Algorithm which computes the longest common substring of two strings
- String inputs are case sensitive 
"""

def lcSubstring(s1 , s2):
  m = len(s1) + 1
  n = len(s2) + 1
  largest = index = 0
  #initialize empty table
  lookup = [[0 for x in range(n)] for y in range(m)]
  #fill table, we only care about diagonals
  for i in range(1, m):
    for j in range(1, n):
      if s1[i-1] == s2[j-1]:
        lookup[i][j] = lookup[i-1][j-1]+1
        if lookup[i][j] > largest:
          largest = lookup[i][j]
          index +=1
  #slice the string from the length of the lcs to the index
  return s2[index-largest:index]
