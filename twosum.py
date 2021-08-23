# twosum using two pointer approach
def twosum(arr,k):
    n = len(arr)
    arr.sort()
    i = 0
    j = n-1
    while i< n and j >= 0:
        if arr[i]+ arr[j] == k:
            return 1
        if arr[i] + arr[j] < k :
            i += 1
            continue
        if arr[i]+ arr[j]>k:
            j -= 1
            continue
    return 0
    
print(twosum([2,3,9,5,1],12))
