import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    length = 0

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if length == 0:
            min_heap = []
            max_heap = []

        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            length += 1
        elif length > 0:
            if num == -1:
                heapq.heappop(min_heap)
            elif num == 1:
                heapq.heappop(max_heap)
            else:
                continue
            length -= 1

    if length <= 0:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))

from heapq import heapify, heappush, heappop

def solution(operations):
    answer = []
    hq = []
    
    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)

        if alphabet == 'I':
            heappush(hq, number)    
        else: # alphabet == 'D'
            if hq: # 빈 큐에서 데이터를 삭제하라는 연산이 주어졌을 시 무시
                if number == -1:
                    heappop(hq) # 최솟값을 삭제
                else:
                    hq.sort()
                    hq.pop() # 최댓값을 삭제
                    
    # 모든 연산을 처리한 후
    hq.sort()
    if hq: # 큐가 비어있지 않음
        answer = [hq[-1], hq[0]]
    else: # 큐가 비어있음
        answer = [0, 0]
        
    return answer


def solution(operations):
    answer = []
    hq = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)    

        if op == 'I':
            heappush(hq, num)
        else:
            if hq:
                if num == -1:
                    heappop(hq)
                else:
                    hq.sort()
                    hq.pop()
    
    hq.sort()
    if hq:
        answer = hq[-1], hq[0]
    else:
        answer = [0, 0]
    
    return answer

