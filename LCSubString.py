def lcs(s1 , s2):
  m = len(s1) + 1
  n = len(s2) + 1
  retval = ""
  longesti = longestj = 0
  #initialize empty table
  lookup = [[0 for x in range(n)] for y in range(m)]
  #fill table, we only care about diagonals
  for i in range(1, m):
    for j in range(1, n):
      if s1[i-1] == s2[j-1]:
        lookup[i][j] = lookup[i-1][j-1]+1
        if lookup[i][j] > lookup[longesti][longestj]:
          longesti = i
          longestj = j
  #iterate through longest diagonal
  while lookup[longesti][longestj] != 0:
    retval += s1[longesti-1]
    longesti = longesti - 1
    longestj = longestj - 1

  return retval[::-1]
