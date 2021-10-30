"""
ZEHE'S ALGORITHM
Author: Cole Zehe
Project: CSCI 311 DNA Sequencing
- Counts up each type of letter relative to total for each sequence
- Compares ratios of letter count to total
- Sequence with least variation from from ratios on target sequence is closest

INPUTS:
t = target sequence string
sequences  = dictionary of sequences

OUTPUT:
2 items: Name / Function of winning sequence, dict of percent differences in ratios
"""

def ZeheAlgorithm(t, sequences):
    
    # FIRST FIND LETTER RATIOS FOR TARGET SEQUENCE
    tRatios = {"a":0, "t":0, "c":0, "g":0}

    for letter in t:
        lett = letter.lower()
        # Ignore non DNA-related characters
        if lett in "atcg":
            # Add to count
            tRatios[lett] += 1

    # Now divide by total to get ratios
    for letter in tRatios:
        tRatios[letter] = tRatios[letter] / len(t)



    # NOW FOR THE OTHER SEQUENCES
    bestSeqName = ""
    leastVariation = 999999
    bestRatioVariations = {}
    # Compare ratios for each letter type ratio in each sequence
    for key in sequences:
        ratios = {"a":0, "t":0, "c":0, "g":0}
        # Look at each character in the sequence
        for letter in sequences[key]:
            l = letter.lower()
            # Ignore non DNA-related characters
            if l in "atcg":
                # Add to count
                ratios[l] += 1

        variation = 0
        # Now divide by total to get ratios
        for letter in ratios:
            ratios[letter] = (ratios[letter] / len(sequences[key]))
            # Keep track of how much the ratios vary to target ratios
            variation += abs(ratios[letter] - tRatios[letter])

        if variation < leastVariation:
            leastVariation = variation
            bestSeqName = key
            bestRatioVariations = ratios


    # Return the best sequence with the least variation from the target
    return bestSeqName, bestRatioVariations