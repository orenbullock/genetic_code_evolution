from Bio.Data import CodonTable
import random
import json
import argparse

def get_dicts(trans_table):
    # Forms codon (key, str) to amino acid (value, str) dictionary using prexisting Bio.Data dictionary
    codon_to_aa_dict = dict(CodonTable.unambiguous_dna_by_id[trans_table].forward_table)
    
    # Creates an amino acid (key, str) to codon (value, lst) dictionary using initial codon to amino acid dictionary 
    aa_to_codon_dict = {}
    for codon,aminoacid in codon_to_aa_dict.items():
        if aminoacid not in aa_to_codon_dict.keys():
            aa_to_codon_dict[aminoacid] = []
        aa_to_codon_dict[aminoacid].append(codon)
    return codon_to_aa_dict, aa_to_codon_dict

def shuffle_aminoacid_dicts(ns_to_shuffle, shuffle = True, trans_table = 11):
    
    '''
    Inputs:
    ns_to_shuffle (list) refers to the number of codons for a given amino acid (e.g. ser has 6 codons)
    - Amino acids with these n's will be left in the dictionary to be shuffled
    - Any amino acids with n's not included will be excluded from the dictionary and hence, not shuffled
    - Must be a list of ints
    - Function work well for ints 1-6, excluding 5
    
    shuffle = True, returns shuffled dictionaries
    shuffle = False, returns original unshuffled amino acid/codon dictionaries
    
    Only works for trans_table = 11 right now.
    https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
    
    Outputs:
    Either,
    1. All amino acids and corresponding codons shuffled together; returns two dictionaries
    2. Individual amino acid with codon groups of size n will be shuffled together; returns two dictionaries
    '''
    codon_to_aa_dict, aa_to_codon_dict = get_dicts(trans_table)

    # Removes any unwanted amino acids (with n codons, where n is not in our ns_to_shuffle) 
    # from the dictionaries before shuffling
    for aminoacid,codons in list(aa_to_codon_dict.items()):
        if len(codons) not in ns_to_shuffle:
            del aa_to_codon_dict[aminoacid] 
            for codon in codons:            
                del codon_to_aa_dict[codon]
    
    if not shuffle:
        return aa_to_codon_dict, codon_to_aa_dict
    
    aa_list = list(aa_to_codon_dict.keys())
    codon_list = list(aa_to_codon_dict.values())
    
    # Shuffles amino acids/codons, zips into new shuffled amino acid (key,str) to codon (value,lst) dictionary
    random.shuffle(aa_list)
    shuffled_aa_to_codon_dict = dict(zip(aa_list,codon_list))          

    # Forms shuffled codon (key, str) to amino acid (value, str) dictionary based on 
    # previous shuffled amino acid to codon dictionary
    shuffled_codon_to_aa_dict = {}
    for aminoacid,codons in shuffled_aa_to_codon_dict.items():
        for codon in codons:
            shuffled_codon_to_aa_dict[codon] = aminoacid
            
            
    return shuffled_aa_to_codon_dict, shuffled_codon_to_aa_dict


# Write to files. Insert number of desired shuffled dictionaries into range function.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices = ["mode1","mode2"], 
                        help = "Select mode. PUT MORE HERE", 
                        type = str)
    parser.add_argument("shuffling", 
                        help = "Number of shuffles to perform PUT MORE HERE", 
                        type = int)
    
    args = parser.parse_args()     
    
    for i in range(args.shuffling):
        if args.mode == "mode1":
            
            ## 1. Run this line if you want all amino acids shuffled with each other ##

            aa_to_codon,codon_to_aa = shuffle_aminoacid_dicts([1,2,3,4,6])
            
        elif args.mode == "mode2":
            
            ## 2. Run these lines if you only want individual codon groups (of size n) shuffled together ##

            a1,b1 = shuffle_aminoacid_dicts([1])
            a2,b2 = shuffle_aminoacid_dicts([2])
            a3,b3 = shuffle_aminoacid_dicts([3])
            a4,b4 = shuffle_aminoacid_dicts([4])
            a6,b6 = shuffle_aminoacid_dicts([6])
            aa_to_codon = {**a1,**a2,**a3,**a4,**a6}
            codon_to_aa = {**b1,**b2,**b3,**b4,**b6}

        with open("../data/shuffled_aa_to_codon_dict_{}_{}.json".format(args.mode,i), "w") as outfile:
            json.dump(aa_to_codon, outfile)

        with open("../data/shuffled_codon_to_aa_dict_{}_{}.json".format(args.mode,i), "w") as outfile:
            json.dump(codon_to_aa, outfile)
            
            
            