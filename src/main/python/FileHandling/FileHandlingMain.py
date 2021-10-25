"""
*****************************************
* Name: Rob Barlow
* Date: 10/21/2021
* Time: 2:26 PM
*
* Project: CSCI311_DNA_Sequencing
* Class: FileHandlingMain
*
* Description: Main file to handle files for the program
****************************************
"""

def ReadDNA_query():
    """
    Function to read DNA_query.txt.

    :return: String containing text from DNA_query.txt
    """
    DNA_queryRaw = open("DNA_query.txt", "r")

    DNA_queryStr = ""
    for line in DNA_queryRaw:
        DNA_queryStr += line

    DNA_queryRaw.close()
    return DNA_queryStr

ReadDNA_query()
