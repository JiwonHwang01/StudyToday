import heapq

def solution(book_time):
    answer = 0
    times = []
    heap = []
    for time in book_time:
        tmp = []
        tmp.append(list(map(int,time[0].split(":"))))
        tmp.append(list(map(int,time[1].split(":"))))
        times.append([int(tmp[0][0])*60+int(tmp[0][1]),int(tmp[1][0])*60+int(tmp[1][1])])
    
    times.sort(key = lambda x:(x[0],x[1]))

    heapq.heappush(heap,-11)
    for time in times:
        if heap[0]+10 <= time[0]:
            heapq.heappop(heap)
        
        heapq.heappush(heap,time[1])
        

    return len(heap)