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

def ReadFile(file):
    """
    Function to read DNA_query.txt.

    :param file: name of the file to read in
    :return: String containing text from file
    """
    rawFile = open(file, "r") #Opening the file

    #Reading in each line in the file
    fileSTR = ""
    for line in rawFile:
        fileSTR += line

    rawFile.close()
    return fileSTR.upper().strip().strip("\n")

def HandleDNA_sequences(DNA_sequencesStr):
    """
    Function that takes a string of known DNA sequences and puts then into a dictionary where key
    is the sequence description and value is the DNA sequence.

    :param DNA_sequencesStr: String
    :return: Dictionary
    """
    DNA_sequencesList = DNA_sequencesStr.split("\n")

    #Removing any empty elements
    DNA_sequencesListMod = [line for line in DNA_sequencesList if len(line.strip()) >0]
    DNA_sequencesDict = {}

    #Iterating over each element and storing the sequences in a dictionary
    for line in DNA_sequencesListMod:
        line.strip() #Removing any spaces at the beginning or end
        if line[0] == ">":
            key = line
            DNA_sequencesDict[key] = ""
        else:
            DNA_sequencesDict[key] += line.upper()

    return DNA_sequencesDict
