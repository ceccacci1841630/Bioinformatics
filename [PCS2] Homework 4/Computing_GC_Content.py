from Filename import file_reader

def content_GC(string):
    c = string.count("C")
    g = string.count("G")
    tot = len(string)
    result = (c + g) * 100 / (tot)
    return (result)

fasta_dictionary = {}
string_name = ""
input_list = file_reader("rosalind_gc.txt")


for line in input_list:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        string_name = line[1:]
        if string_name not in fasta_dictionary:
            fasta_dictionary[string_name] = ""
        continue
    string = line
    fasta_dictionary[string_name] = fasta_dictionary[string_name] + string
dictionary = dict()
for string_name in fasta_dictionary:
    dictionary[string_name] = float(content_GC(fasta_dictionary[string_name]))

inverse = [(string, string_name) for string_name, string in dictionary.items()]


highest_GC = max(inverse)[1]


print ((highest_GC))
print(str(dictionary[highest_GC]))

