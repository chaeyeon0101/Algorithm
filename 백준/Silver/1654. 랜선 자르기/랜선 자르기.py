k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
data.sort()

def isPossible(max_len):
    cnt = 0
    for i in data:
        cnt += i // max_len
    if cnt >= n:
        return True
    else:
        return False

start = 1
end = data[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    
    if isPossible(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)