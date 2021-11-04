# CSCI311_DNA_Sequencing
DNA Sequencing programs for CSCI 311 Design and Analysis of Algorithms

Authors: Cole Zehe, Cole Hausman, Rob Barlow, Nick Satriano

### Github Repository for Our Code:
https://github.com/colezehe/CSCI311_DNA_Sequencing/

### How to Run and Interact with Our Code:
1) Open your favorite IDE for running Python code
2) _CSCI311_DNA_Sequencing/src/main/python_ contains all the code for this project
3) _/src/main/python/UserInterface.py_ contains the main code for interacting with our programs. This is the code you want to run in order to interact with our interface and choose different algorithms.

### How to Understand Our Programs

_/src/main/python/UserInterface.py_
  - Contains the main loop for the user to interact with our algorithms
  - Is what should be run by the user

_/src/main/python/FileHandling/FileHandlingMain.py_
  - Contains functions for reading in DNA sequences
  - Follows the FASTA format required

_/src/main/python/LCSubString.py_
  - Contains code for finding the longest common substring
  - Inputs are two strings s1 and s2

_/src/main/python/LCSubSequence.py_
  - Contains code for finding the longest common subsequence
  - Inputs are two strings s1 and s2

_/src/main/python/EditDistance.py_
  - Contains functions for finding the minimum edit distance
  - Requires three inputs: unknown DNA sequence, dictionary of known sequences, and boolean indicating if the user wants to see the edits

_/src/main/python/NeedlemanWunschAlgorithm.py_
  - Uses the Needleman Wunsch Algorithm
  - Input should be in the form nw(x, y), where x and y are strings, in order to leave all other parameters as defaults.

_/src/main/python/ZeheAlgorithm.py_
  - Uses unique algorithm designed by famed computer engineer Cole Zehe
  - Inputs: t = target sequence, sequences = dictionary where keys are function of seq., values are sequence of chars

_/src/main/python/triples_algorithm.py_
  - Looks at triples of letters in the sequences
  - Inputs: query = query sequence to match, seqs = dictionary of sequences
