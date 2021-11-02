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
* References: https://en.wikipedia.org/wiki/Edit_distance
*             https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
****************************************
"""

class Directions:
    """
    Class/Enum to store values to for table to recreate solution
    """
    DIAGONAL_NC = 1
    DIAGONAL_SUB = 2
    LEFT = 3
    UP = 4

class Colors:
    """
    Colors to be used when printing solution. The default color (white) means no changes were made to that
    character.
    """
    BLUE = "\033[94m"  # Substitute
    GREEN = "\033[92m" # Insert
    RED = "\033[91m"   # Delete
    END = "\033[0m"    # Stop color

def EditDistance(unknown, known, ):
    """
    Dynamic Programming algorithm to find the minimum number of edits to change unknown to known.

    :param unknown: String
    :param known:   String
    :return: int  - minimum number of edits
    :return: List - table to reconstruct solution
    """

    # Weight of each edit operation
    W_SUB = 1
    W_INS = 1
    W_DEL = 1

    # Lengths of the strings
    m = len(unknown)
    n = len(known)

    # Creating table c to store subproblem solutions
    # Creating table b to store edits to solution
    b, c = _CreateTables(m, n)

    # Finding the minimum number of edits
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Determining if next character if a_i = b_j
            if unknown[i - 1] == known[j - 1]:
                c[i][j] = c[i - 1][j - 1]
                b[i][j] = Directions.DIAGONAL_NC

            else:
                # Computing costs
                subCost = c[i - 1][j - 1] + W_SUB
                insCost = c[i][j - 1] + W_INS
                delCost = c[i - 1][j] + W_DEL

                # Finding the minimum cost
                if subCost <= insCost and subCost <= delCost:
                    c[i][j] = subCost
                    b[i][j] = Directions.DIAGONAL_SUB

                elif insCost <= delCost:
                    c[i][j] = insCost
                    b[i][j] = Directions.LEFT

                else:
                    c[i][j] = delCost
                    b[i][j] = Directions.UP

    return b, c


def _CreateTables(m, n):
    """
    Function to create and initialize tables.

    :param m: int
    :param n: int
    :return: List - table where subproblem solutions will be stored
    :return: List - table where direction to recreate solution will be stored
    """

    c = []
    b = []

    for i in range(m + 1):
        c.append([])
        b.append([])

        for j in range(n + 1):
            if i == 0:
                c[i].append(j)  # Base case

            elif j == 0:
                c[i].append(i)  # Base case

            else:
                c[i].append(0)
            b[i].append(0)

    return b, c

def _PrintSolution(b, unknown, known):
    """
    Prints the edits needed to transform unknown into known. The color of the letters correspond to the edits
    made:
        White: no change
        Blue:  substitution
        Green: Insert
        Red:   Delete

    :param b:       List - A table
    :param unknown: String
    :param known:   String
    """

    output = ""
    i = len(unknown)
    j = len(known)

    while b[i][j] != 0:
        if b[i][j] == Directions.DIAGONAL_SUB:
            output = Colors.BLUE + known[j - 1] + Colors.END + output
            i -= 1
            j -= 1

        elif b[i][j] == Directions.LEFT:
            output = Colors.GREEN + known[j - 1] + Colors.END + output
            j -= 1

        elif  b[i][j] == Directions.UP:
            output = Colors.RED + unknown[i - 1] + Colors.END + output
            i -= 1

        else:
            output = known[j - 1] + output
            i -= 1
            j -= 1


    print("\n" + output + "\n")

def printTable(table):
    for row in table:
        print(row)
    print("\n")


unknown = "GGGGACCCAGTAACCACCAGCCCTAAGTGATCCGCTACAATCAAAAACCATCAGCAAGCAGGAAGGTACTCTTCTCAGTGGGCCTGGCTCCCCAGCTAAGACCTCAGGGACTTGAGGTAGGATATAGCCTCCTCTCTTACGTGAAACTTTTGCTATCCTCAACCCAGCCTATCTTCCAGGTTATTGTTTCAACATGGCCCTGTGGATGCGCTTCCTGCCCCTGCTGGCCCTGCTCTTCCTCTGGGAGTCCCACCCCACCCAGGCTTTTGTCAAGCAGCACCTTTGTGGTTCCCACCTGGTGGAGGCTCTCTACCTGGTGTGTGGGGAGCGTGGCTTCTTCTACACACCCATGTCCCGCCGTGAAGTGGAGGACCCACAAGGTGAGTTCTGCCACTGAATTCTGTCCCCAGTGCTAACTACCCTGGTTTTCTTCACACTTGGGACATTGTAAATTGTGTCCTAGGTGTGGAGGGTCTCGGGATAACCAGGGAGTGGGGACACGTTTCTGGGGGAAGCTAGACATATGTAAACATGGCAGCTGCCAGGAATGAGTAAGAATCCTGCCTTAAGGGGTCCTTGGTGGTAGTAACTTGGGACATGTGACTAGATCCCAGGATAGGTACCTATTTAGGGCCCTCATAGAGCACTGCACTGACTGAAGATGAGTAGGCTTTAGAGGCCCATGTGTCCATCCATGACCAGTGACTTGTCCCACAGGCATGCAACCCCTGCCACCTGCAGGGGTTAAGGGGCGAGAAAACCTGGGGTAGTAGGAGGTTGCTCAGCTACTCCTGACTGGATTTTCCTATGTGTCTTTGCTTCTGTGCTGCTGATGCCCTGGCCTGCTCTGACACAACCTCCCTGGCAGTGGCACAACTGGAGCTGGGTGGAGGCCCGGGAGCAGGTGACCTTCAGACCTTGGCACTGGAGGTGGCCCAGCAGAAGCGTGGCATTGTAGATCAGTGCTGCACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACCCACCACTACCCAGCCTACCCCTCTGCAATGAATAAAACCTTTGAATGAGCACAA"
known   = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"
b, c = EditDistance(unknown, known)
printTable(c)
printTable(b)
_PrintSolution(b, unknown, known)