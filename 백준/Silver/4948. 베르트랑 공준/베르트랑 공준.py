import sys
import math
input = sys.stdin.readline

arr = [True] * (123456 * 2 + 1)
arr[0], arr[1] = 0, 0

for i in range(2, int(math.sqrt(123456 * 2 + 1))):
    if arr[i]:
        for j in range(i + i, 123456 * 2 + 1, i):
            arr[j] = False

while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        print(arr[n + 1 : (2 * n) + 1].count(True))