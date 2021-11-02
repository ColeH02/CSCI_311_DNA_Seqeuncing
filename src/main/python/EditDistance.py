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
import sys


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

def EditDistanceMain(unknown, DNASequenceDict, displayEdits):
    """
    Function that runs the Edit Distance method and prints the minimum number of edits and name of the
    corresponding sequence. User has the option to print out the edits required to get from the unknown
    sequence to the closest match sequence.

    :param unknown:         String     - Unknown DNA sequence
    :param DNASequenceDict: Dictionary - Known DNA sequences
    :param displayEdits:    Boolean    - True if the user wants the edits displayed
    """

    # Initializing variables
    minEdits        = sys.maxsize
    minSequenceName = ""
    minSequence     = ""
    b               = None

    for key in DNASequenceDict:
        temp_b, tempEdits = _EditDistance(unknown, DNASequenceDict[key])

        if tempEdits < minEdits:
            minEdits        = tempEdits
            minSequenceName = key
            minSequence     = DNASequenceDict[key]
            b               = temp_b

    if minEdits == sys.maxsize or minSequenceName == "" or minSequence == "" or b == None:
        print("\nAn invalid sequence was entered!\n")

    else:
        if displayEdits:
            _PrintSolution(b, unknown, minSequence)

        print("\nMinimum Edit Distance:      ", minEdits)
        print("Sequence Name and Function: ", minSequenceName)


def _EditDistance(unknown, known):
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
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    b = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Initializing base cases
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                c[i][j] = j # Base case
            elif j == 0:
                c[i][j] = i # Base case

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

    return b, c[m][n]

def _PrintSolution(b, unknown, known):
    """
    Prints the edits needed to transform unknown into known. The color of the letters correspond to the edits
    made:
        White: No Change
        Blue:  Substitution
        Green: Insert
        Red:   Delete

    :param b:       List - A table
    :param unknown: String
    :param known:   String
    """

    outputEdits = ""
    i = len(unknown)
    j = len(known)

    while b[i][j] != 0:
        if b[i][j] == Directions.DIAGONAL_SUB:
            outputEdits = Colors.BLUE + known[j - 1] + Colors.END + outputEdits
            i -= 1
            j -= 1

        elif b[i][j] == Directions.LEFT:
            outputEdits = Colors.GREEN + known[j - 1] + Colors.END + outputEdits
            j -= 1

        elif  b[i][j] == Directions.UP:
            outputEdits = Colors.RED + unknown[i - 1] + Colors.END + outputEdits
            i -= 1

        else:
            outputEdits = known[j - 1] + outputEdits
            i -= 1
            j -= 1

    print("\nLegend:\nWhite: No Change\nBlue:  Substitution\nGreen: Insert\nRed:   Delete\n")
    print("Unknown Sequence:\n" + unknown)
    print("Edits Made:\n" + outputEdits)
    print("Known Sequence:\n" + known)