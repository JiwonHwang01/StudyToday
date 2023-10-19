# 수학적 판단 # 완전 탐색
def solution(m, n, startX, startY, balls):
    answer = []
    for pos in balls:
        endX, endY = pos
        res = 1e7
        case = 0
        # 1.Y=0 / 2.Y=m / 3.X=0 / 4.X=n
        if startY == endY:
            if startX > endX:
                case = 1
            elif startX < endX:
                case = 2
        elif startX == endX:
            if startY > endY:
                case = 3
            elif startY < endY:
                case = 4

        dx = [-2*startX,2*(m-startX),0,0]
        dy = [0,0,-2*startY,2*(n-startY)]
        for i in range(4):
            if case > 0 and i == case-1:
                continue
                
            nx = startX + dx[i]
            ny = startY + dy[i]
            distance = (endX - nx)**2 + (endY - ny)**2
            
            res = min(distance, res)
        answer.append(res)
    return answer