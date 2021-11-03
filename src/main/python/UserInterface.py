""" 
USER INTERFACE 
Author: Cole Zehe 
Project: CSCI 311 DNA Sequencing 

- Allows the user to select which algorithm to use 
- Functions as main menu and runner of our code 
""" 
import LCSubString
from ZeheAlgorithm import *
import FileHandlingMain
from src.main.python.EditDistance import EditDistanceMain
from src.main.python.LCSubSequence import lcSubsequence
from src.main.python.NeedlemanWunschAlgorithm import nw

""" 
Prints out options of algorithms 
Allows user to input which to use and executes it
""" 
def chooseAlgorithm(unknownDNA, DNASequenceDict):
  global exit
  # List out choices for user
  print("\nWelcome to our DNA Sequence Matching program") 
  print("Select one of the following algorithms to use:")
  print("1) Longest Common Sequence") 
  print("2) Longest Common Substring") 
  print("3) Edit Distance")
  print("4) Zehe's Algorithm")
  print("5) Needleman Wunsch Algorithm")
  print("6) Exit program")

  choice = input("\nType choice (1-6) here: ")

  # If the user wants to use L-C-Subsequence
  if (choice == "1"):
    # LCSubString()
    maxLen = 0
    maxKey = ""
    maxSubSequence = ""
    for key in DNASequenceDict:
      subString = lcSubsequence(unknownDNA, DNASequenceDict[key])
      # print(subString)
      if (len(subString) > maxLen):
        maxLen = len(subString)
        maxKey = key
        maxSubSequence = subString
    print("Longest Subsequence: " + maxSubSequence)
    print("Sequence name and function: " + maxKey)

  # If the user wants to use L-C-Substring
  elif (choice == "2"):
    # LCSubString()
    maxLen = 0
    maxKey = ""
    maxSubString = ""
    for key in DNASequenceDict:
      subString = LCSubString.lcSubstring(unknownDNA, DNASequenceDict[key])
      # print(subString)
      if (len(subString) > maxLen):
        maxLen = len(subString)
        maxKey = key
        maxSubString = subString
    print("Longest Substring: " + maxSubString)
    print("Sequence name and function: " + maxKey)

  # If the user wants to use Edit distance
  elif (choice == "3"):

    # Getting input from user
    userInputSTR = input("\nDisplay Edits? (yes/no): ").strip().lower()
    userInput = False

    # Interpreting input
    if userInputSTR == "y" or userInputSTR == "yes" or userInputSTR == "t" or userInputSTR == "true":
      userInput = True

    # Checking that non-empty sequences are used
    if len(unknownDNA) >= 1:
      EditDistanceMain(unknownDNA, DNASequenceDict, userInput)
    else:
      print("\nSequence of length 0 entered")

  # If user wants to use Zehe's algorithm
  elif (choice == "4"):
    Key, ratioVar = ZeheAlgorithm(unknownDNA, DNASequenceDict)
    print("Sequence name and function: " + Key)
    print("Variation in letter count / total percentages: " + str(ratioVar))

  # If user wants to use Needleman Wunsch algorithm
  elif (choice == "5"):
    maxLen = 0
    maxKey = ""
    bestMatch = ""
    for key in DNASequenceDict:
      output = nw(unknownDNA, DNASequenceDict[key])
      # print(subString)
      if (len(output) > maxLen):
        maxLen = len(output)
        maxKey = key
        bestMatch = output
    print("Closest Match: " + bestMatch)
    print("Sequence name and function: " + maxKey)
  # If the user wants to exit, change exit condition
  else:
    exit = True


""" MAIN SECTION OF PROGRAM """

print("=====================") 
print("DNA SEQUENCE MATCHING") 
print("=====================")  

exit = False

# Loading in files
unknownDNA = FileHandlingMain.ReadFile("src\main\python\\test1.txt")
DNASequenceDict = FileHandlingMain.HandleDNA_sequences(FileHandlingMain.ReadFile("src\main\python\DNA_sequences.txt"))

# Begins main program loop for user
while(not exit):
  chooseAlgorithm(unknownDNA, DNASequenceDict)

print("\n --- Thank you, goodbye! --- ")

