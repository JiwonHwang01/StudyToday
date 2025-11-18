import re
def solution(dartResult):
    answer = [0]*(4)
    pattern = r'(10|[0-9])([SDT])([*#]?)'
    matches = re.findall(pattern, dartResult)
    tmp = 0
    for i in range(len(matches)):
        if matches[i][1] == 'S':
            tmp = int(matches[i][0])**1
        elif matches[i][1] == 'D':
            tmp = int(matches[i][0])**2
        else:
            tmp = int(matches[i][0])**3
        
        if matches[i][2] == '#':
            tmp *= -1
        elif matches[i][2] == '*':
            tmp *= 2
            answer[i] *= 2
            
        answer[i+1] = tmp
        
    return sum(answer)