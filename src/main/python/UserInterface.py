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
  print("5) Exit program")

  choice = input("\nType choice (1-5) here: ")

  # If the user wants to use L-C-Subsequence
  if (choice == "1"):
    pass
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

    EditDistanceMain(unknownDNA, DNASequenceDict, userInput)

  # If user wants to use Zehe's algorithm
  elif (choice == "4"):
    Key, ratioVar = ZeheAlgorithm(unknownDNA, DNASequenceDict)
    print("Sequence name and function: " + Key)
    print("Variation in letter count / total percentages: " + str(ratioVar))

  # If the user wants to exit, change exit condition
  else:
    exit = True


""" MAIN SECTION OF PROGRAM """

print("=====================") 
print("DNA SEQUENCE MATCHING") 
print("=====================")  

exit = False

unknownDNA = FileHandlingMain.ReadFile("src\main\python\\test3.txt")
DNASequenceDict = FileHandlingMain.HandleDNA_sequences(FileHandlingMain.ReadFile("src\main\python\DNA_sequences.txt"))
# Begins main program loop for user
while(not exit):
  chooseAlgorithm(unknownDNA, DNASequenceDict)

print("\n --- Thank you, goodbye! --- ")

