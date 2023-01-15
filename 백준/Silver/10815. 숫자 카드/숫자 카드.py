n = int(input())
n_num = list(map(int, input().split()))
n_num.sort()
m = int(input())
m_num = list(map(int, input().split()))

def binary_search(target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if n_num[mid] == target:
        return 1
    elif n_num[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)
        
for i in m_num:
    print(binary_search(i, 0, n - 1), end = ' ')