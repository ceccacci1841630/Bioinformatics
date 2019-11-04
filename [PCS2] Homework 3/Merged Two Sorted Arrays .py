def merge_sorted(listc):
    return(sorted(listc))

with open("./rosalind_mer.txt", "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string= input_list[1], input_list[3]
arraya = list(map(int, string.split()))
arrayb= list(map(int, to_find_string.split()))
listc = list(arraya+arrayb)
result = merge_sorted(listc)
print (str(result).replace(",", ""))