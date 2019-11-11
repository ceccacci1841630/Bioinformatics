from Filename import file_reader
def sum_3(a):
    dict_negatives = {}
    dict_positives = {}
    dict_zeros = {}
    length = len(a)
    for i in range(length):
        for j in range(i+1,len(a)):
            sum_ = a[i] + a[j]
            if sum_ < 0:
                dict_negatives[sum_] = (i, j)
            elif sum_ > 0:
                dict_positives[sum_] = (i, j)
            else:
                dict_zeros[sum_] = (i, j)
    for i in range(length):
        value = a[i]
        if value < 0:
            for j in dict_positives.keys():
                if j == -value and i not in dict_positives[j]:
                    index1, index2 = dict_positives[j]
                    return index1+1, index2+1, i+1
        elif value > 0:
            for j in dict_negatives.keys():
                if j == -value and i not in dict_negatives[j]:
                    index1, index2 = dict_negatives[j]
                    return index1+1, index2+1, i+1
        else:
            for j in dict_zeros.keys():
                if i not in dict_zeros[j]:
                    index1, index2 = dict_zeros[j]
                    return index1+1, index2+1, i+1
    else:
        return [-1]
        
l = file_reader("rosalind_3sum.txt")
k = l[0].split()[0]
results = []

for ind in range(1, int(k)+1):
    result = sum_3(list(map(int, l[ind].split())))
    print(" ".join(list(map(str, sorted(result)))))