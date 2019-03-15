from Bio.Data import CodonTable
import random
import json 

def shuffle_and_return_aa_and_codon_dicts(trans_table = 11):
    '''
    blahblah
    
        hyy bgb
    '''
    codon_to_aa_dict = CodonTable.unambiguous_dna_by_id[trans_table].forward_table

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
            
    return shuffled_aa_to_codon_dict, shuffled_codon_to_aa_dict

    
        
    
if __name__ == "__main__":
#     for i in range(20):
#         aa_to_codon, codon_to_aa = gce(i)
#         with open("../data/shuffled_aa_to_codon_dict_{}.json".format(i), "w") as outfile:
#             json.dump(aa_to_codon, outfile)

#         with open("../data/shuffled_codon_to_aa_dict_{}.json".format(i), "w") as outfile:
#             json.dump(codon_to_aa, outfile)
    
    
    



    ########Run this line if you want everyone shuffled
    atotal = functiony([1,2,3,5,6])
    
    
#     ########Run this set to shuffle individual sets and put back together
#     a1 = 
#     a2 = 
#     atotal = 

# a1 =
# #     a2=
#     a3=
    ....
        atotal = {**a1, **a2, **a3, **a4, **a6}
          with oh;pen...
        
            json.dump(atotal)
# put comments in code
# clean up code
# rename function and outfiles
# write docstring
