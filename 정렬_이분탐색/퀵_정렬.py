def quick_sort_sub(a, start, end):
    if start >= end:
        return
    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i+=1
    
    a[i], a[end] = a[end], a[i]
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)

# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)