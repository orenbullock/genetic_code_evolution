from Bio.Data import CodonTable
import random
import json 

def gce(file_name_modifier):

    codon_to_aa_dict = CodonTable.unambiguous_dna_by_id[11].forward_table

    aa_to_codon_dict = {}
    for codon,aminoacid in codon_to_aa_dict.items():
        if aminoacid not in aa_to_codon_dict.keys():
            aa_to_codon_dict[aminoacid] = []
        aa_to_codon_dict[aminoacid].append(codon)

    aa_list = list(aa_to_codon_dict.keys())
    codon_list = list(aa_to_codon_dict.values())

    random.shuffle(aa_list)

    shuffled_aa_to_codon_dict = dict(zip(aa_list,codon_list))          

    shuffled_codon_to_aa_dict = {}

    for aminoacid,codons in shuffled_aa_to_codon_dict.items():
        for codon in codons:
            shuffled_codon_to_aa_dict[codon] = aminoacid

    with open("../data/shuffled_aa_to_codon_dict_{}.json".format(file_name_modifier), "w") as outfile:
        json.dump(shuffled_aa_to_codon_dict, outfile)

    with open("../data/shuffled_codon_to_aa_dict_{}.json".format(file_name_modifier), "w") as outfile:
        json.dump(shuffled_codon_to_aa_dict, outfile)
        
    return

for i in range(20):
    gce(i)
    