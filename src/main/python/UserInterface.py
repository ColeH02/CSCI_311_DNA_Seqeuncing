""" 
USER INTERFACE 
Author: Cole Zehe 
Project: CSCI 311 DNA Sequencing 

- Allows the user to select which algorithm to use 
- Functions as main menu and runner of our code 
""" 
import lcSubstring


""" 
Prints out options of algorithms 
Allows user to input which to use and executes it
""" 
def chooseAlgorithm():
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
    lcSubstring()
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
# Begins main program loop for user
while(not exit):
  chooseAlgorithm()

print("\n --- Thank you, goodbye! --- ")

