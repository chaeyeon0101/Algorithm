n = int(input())
data = list(map(int, input().split()))
data.sort()
total = int(input())
total_data = sum(data)

if total_data <= total:
    print(data[-1])
    exit()
    
def isPossible(ceiling):
    total_data = 0
    for i in data:
        if i > ceiling:
            total_data += ceiling
        else:
            total_data += i
    
    if total_data <= total:
        return True
    else:
        return False
    
start = 1
end = data[-1]
result = -1
while start <= end:
    mid = (start + end) // 2
    
    if isPossible(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)