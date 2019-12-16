#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:08:20 2019

@author: carlottaceccacci
"""


def ReadFASTA(data_location):
        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)
        

       
def ParseFASTA(f):
        fasta_list=[]
        for line in f:
                if line[0] == '>':
    
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']
                else:
                        current_dna[1] += line.rstrip('\n')
        
       
        fasta_list.append(current_dna)

        return fasta_list

dna, sub_seq = [fasta[1] for fasta in ReadFASTA('rosalind_sseq.txt')]

sseq_indicies, i = [], 0
for nucleotide in sub_seq:
	while dna[i] != nucleotide:
		i += 1

	sseq_indicies.append(str(i+1))
	i += 1

print (' '.join(sseq_indicies))
