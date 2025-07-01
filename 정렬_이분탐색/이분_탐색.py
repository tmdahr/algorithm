def binary_search(a, x) :
    start = 0
    end = len(a)-1
    while start <= end :
        mid = int((start+end)/2)
        if a[mid] == x :
            return mid
        if a[mid] < x :
            start = mid+1
        else :
            end = mid-1
    return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))