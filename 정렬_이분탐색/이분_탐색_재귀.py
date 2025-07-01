def binary_search_sub(a, x, start, end) :
    mid = int((start+end)/2)
    if start > end :
        return -1
    if a[mid] == x :
        return mid
    if a[mid] < x :
        return binary_search_sub(a, x, mid+1, end)
    else :
        return binary_search_sub(a, x, start, mid-1)

# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))