def merge_arrays2(a, b):
    i = j = 0
    sorted = []
    while len(a) > 0 and len(b) > 0:
        if a[i] < b[j]:
            sorted.append(a.pop(i))
        else:
            sorted.append(b.pop(i))
    if len(a) > 0:
        list_with_remaining = a
    else:
        list_with_remaining = b
    for el in list_with_remaining:
        sorted.append(el)
    return sorted
    
with open("./rosalind_mer.txt", "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string= input_list[1], input_list[3]
a = list(map(int, string.split()))
b= list(map(int, to_find_string.split()))
result = merge_arrays2(a,b)
print (str(result).replace(",", ""))