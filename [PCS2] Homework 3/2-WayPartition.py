from Filename import file_reader


def par(arrays):
    i = len(arrays)-1
    pivot = arrays[0]
    for j in range(len(arrays) -1,0,-1):
        if arrays[j] > pivot:
            arrays[j], arrays[i] = arrays[i], arrays[j]
            i -= 1 
    arrays[i], arrays[0] = arrays[0], arrays[i]
    return arrays 

input_list = file_reader("rosalind_par.txt")
arrays = list(map(int, input_list[1].split()))
result = par(arrays)
result = " ".join(list(map(str, result)))
with open("./answer.txt", "w") as file:
    file.write(result)

    
    