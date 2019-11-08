def med(arr, n, k):
    arr.sort()
    return arr[int(k[0])-1]
f = open('rosalind_med.txt', 'r') 
n = f.readline().strip().split()
arr = list(map(int,f.readline().split()))
k = f.readline().strip().split()

print(med(arr, n, k))