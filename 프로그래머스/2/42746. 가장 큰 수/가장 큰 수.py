def solution(numbers):
    answer = ''
    lst = list(map(str,numbers))
    lst.sort(key=lambda x:x*4, reverse=True)
    #print(lst)
    answer = ''.join(lst)
    
    return '0' if answer[0]=='0' else answer