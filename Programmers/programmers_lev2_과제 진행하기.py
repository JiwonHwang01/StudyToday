def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    stack = []    
    
    for i in range(len(plans)):
        name, start, playtime = plans[i][0], plans[i][1], int(plans[i][2])
        if i == len(plans)-1:
            answer.append(name)
            break

        
        nstart = plans[i+1][1]
        hour1, min1 = map(int,start.split(":"))
        hour2, min2 = map(int,nstart.split(":"))
        time = hour1*60 + min1
        ntime = hour2*60 + min2
        

        
        if time + playtime > ntime: # Not done
            playtime -= ntime-time
            plans[i][2] = playtime
            stack.append(plans[i])
        
        else:                       # Done
            answer.append(name)
            if time + playtime == ntime: # Time not left
                continue
            else:                          #Time left
                remain = ntime - time - playtime
                while True:
                    if len(stack)==0 or remain < 1:
                        break
                    todo = stack.pop()
                    if todo[2] > remain:
                        todo[2] -= remain
                        stack.append(todo)
                        break
                    else:
                        remain -= todo[2]
                        answer.append(todo[0])
    while stack:
        tmp = stack.pop()
        answer.append(tmp[0])
                    
    return answer