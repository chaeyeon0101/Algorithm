import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            if heap[0][1] == 1:
                print(heapq.heappop(heap)[0])
            elif heap[0][1] == 0:
                print(-heapq.heappop(heap)[0])
    else:
        if x > 0:
            heapq.heappush(heap, [x, 1])
        else:
            heapq.heappush(heap, [-x, 0])