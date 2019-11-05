def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def merge_sort(a):
    if len(a) ==1:
        return a

    middle = len(a)//2

    left = a[:middle]
    right = a[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left,right))
    
with open("./rosalind_ms.txt", "r") as file:
    input_list = file.read().split("\n")
    string = input_list[1]
l = list(map(int, string.split())) 

result = merge_sort(l)
print (str(result).replace(",", ""))
    