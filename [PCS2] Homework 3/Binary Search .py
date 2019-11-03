def binary_search(la, lb):
    start = 0 
    end = len(la) -1 
    while True:
        midpoint = (start + end)//2 
        if start > end: 
            return -1
        if lb > la[midpoint]:
            start= midpoint +1 
        elif lb < la[midpoint]:
            end = midpoint -1 
        else: 
            return midpoint +1 
            
              
with open("./rosalind_bins.txt", "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string= input_list[2], input_list[3]
la = list(map(int, string.split()))
lb= list(map(int, to_find_string.split()))
l = []
for item in lb:
    result = (binary_search(la,item))
    l.append(result)
print (str(l).replace(",", ""))

