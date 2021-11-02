"""
*****************************************
* Name: Rob Barlow
* Date: 11/1/2021
* Time: 10:17 PM
*
* Project: CSCI311_DNA_Sequencing
* Class: EditDistance
*
* Description: File that contains code for the edit distance method to find closest matching DNA sequence.
* Reference: https://en.wikipedia.org/wiki/Edit_distance
****************************************
"""

def EditDistance(unknown, known):
    """
    Dynamic Programming algorithm to find the minimum number of edits to change unknown to known.

    :param unknown: String
    :param known:   String
    :return: int - minimum number of edits
    """

    # Weight of each edit operation
    W_SUB = 1
    W_INS = 1
    W_DEL = 1

    # Directions to form solution
    DIAGONAL_NC  = 1
    DIAGONAL_SUB = 2
    LEFT         = 3
    UP           = 4

    # Lengths of the strings
    m = len(unknown)
    n = len(known)

    # Creating table c to store subproblem solutions
    # Creating table b to store edits to solution
    c = []
    b = []
    for i in range(m + 1):
        c.append([])
        b.append([])
        for j in range(n + 1):
            if i == 0:
                c[i].append(j) # Base case
            elif j == 0:
                c[i].append(i) # Base case
            else:
                c[i].append(0)
            b[i].append(0)

    # Finding the minimum number of edits
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if unknown[i - 1] == known[j - 1]:
                c[i][j] = c[i - 1][j - 1]
                b[i][j] = DIAGONAL_NC
            else:
                subCost = c[i - 1][j - 1] + W_SUB
                insCost = c[i][j - 1] + W_INS
                delCost = c[i - 1][j] + W_DEL

                if subCost <= insCost and subCost <= delCost:
                    c[i][j] = subCost
                    b[i][j] = DIAGONAL_SUB
                elif insCost <= delCost:
                    c[i][j] = insCost
                    b[i][j] = LEFT
                else:
                    c[i][j] = delCost
                    b[i][j] = UP

    return c, b

def printTable(table):
    for row in table:
        print(row)
    print("\n")

c, b = EditDistance("Test", "Resting")
printTable(c)
printTable(b)

