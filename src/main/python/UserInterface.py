""" 
USER INTERFACE 
Author: Cole Zehe 
Project: CSCI 311 DNA Sequencing 

- Allows the user to select which algorithm to use 
- Functions as main menu and runner of our code 
""" 
import LCSubString
from src.main.python import FileHandlingMain

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
  print("4) Exit program")

  choice = input("\nType choice (1-4) here: ")

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
    pass
  # If the user wants to exit, change exit condition
  elif (choice == "4"):
    exit = True;


""" MAIN SECTION OF PROGRAM """

print("=====================") 
print("DNA SEQUENCE MATCHING") 
print("=====================")  

exit = False;

unknownDNA = FileHandlingMain.ReadFile("test3.txt")
DNASequenceDict = FileHandlingMain.HandleDNA_sequences(FileHandlingMain.ReadFile("DNA_sequences.txt"))
# Begins main program loop for user
while(not exit):
  chooseAlgorithm(unknownDNA, DNASequenceDict)

print("\n --- Thank you, goodbye! --- ")

