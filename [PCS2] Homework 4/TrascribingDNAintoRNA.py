def transform_rna(string):
    return string.replace("T", "U") 
    

string="TGTGGGCGAATCGTTAGAATTCATTTAGGCGAGCCTATTGTTCCTAACAGCATTGGAGGCTCTCCGGACAACCTGCATTCGAACTTCTTCTACCGCGCTATCCACCGACGGATTGCGAGCCGAGGTGCTTCGTATTGCCTATATTAGACACTTGTTGGCATCGGTTATATTGGACATTCCAAGCTTCATGGTATAACTGTGGATTATAACATAGGGCCGAGACTGACATACGGAGCCAAAGTGGACTAAATAACGTATCCGTATTGCTTTCCACAGGATATTCGCCCCGTCATGGCTGACGGACCCGGCAGGCACATTGCATTAGAGCCTAGACCCATTCCCTTCGAATCGTTCAATTCTCAAGACTCCAGAGAATAGGGAACTCGCGATCACAGCACCTGCAGTAACGGGATATGATTCGCTAACCCCTATCGTTAATTCAGTAGGATCCCCGGCGCTGGGTGGGTGTCCGTGTATCTGTAGAAGTCGTCGCGACTTGCGAGATCGTCCTCAGTCTTGTAGCAAACGGCCCGGGGGCATTTTGGGAAATTGGATTGTGAAGTTTCATATATAGCCCTCCCCGCGAGATTAGGTCCCCGCATCATGACTCGGGACATTTATCGTTAGCCCCACGCGTTATTCCGTCACGAATTCGGCGTCACGTCCTTATTTACGGACTGATAAGATTAAGCTACACGGCTGAGGTTTCGCATGCCCTATGTTAGGTTGATTGTTATTGCTACCCAAGCTCTTCTATGTCTAGACCTACTGCACGGGCTCGCTGTAAGGCCCAAAACCCGTTGATCAGCGGGTCATGATCTCAACAGCATAACATCGGCGAGGCGAACTGCTTCGCGTGTAGCAAACGGGGCAACTACAAAATGGCGGCTCTAGACCTCGTACTAG"

print(transform_rna(string))