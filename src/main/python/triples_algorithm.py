"""
Triple's Algorithm
By Nick Satriano

input: query sequence to match, dictionary of sequences

output: sequence that matches query, most common gene triplet

"""

def triples_algorithm(query, seqs):
  triples_dict = {}

  for i in range(len(query) - 3):
    if query[i].upper() in "ATGC":
      triple = query[i:i+2]
      triple = triple.upper()
      if triple in triples_dict:
        triples_dict[triple] += 1
      else:
        triples_dict[triple] = 1


  max_triple = max(triples_dict, key = triples_dict.get)
  max_triple = max_triple.upper()
  
  seq_dict = {}

  for key in seqs:
    for letter in seqs[key]:
      letter = letter.upper()
      if (letter in "ATGC") & (letter in max_triple):
        if key in seq_dict:
          seq_dict[key] += 1
        else:
          seq_dict[key] = 1

  match_key = max(seq_dict, key = seq_dict.get)


  return match_key, max_triple
