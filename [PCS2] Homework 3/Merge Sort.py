
def merge_sorted(listc):
    return sorted(listc)


with open("./rosalind_ms.txt", "r") as file:
    input_list = file.read().split("\n")
    string = input_list[1]
listc = list(map(int, string.split())) 

result = merge_sorted(listc)
print (str(result).replace(",", ""))