# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
# print(chr(97)) = 'a'
import re

def cap_to_lower(str):
    res = ''
    for c in str:
        if 65<= ord(c) < 91:
            c = chr(ord(c)+32)
        
        res += c
    return  res

def rm_mark(str):
    res = ''
    for c in str:
        if (97<=ord(c)<97+26) or c=='-' or c=='_' or c=='.' or ord('0') <= ord(c) <= ord('9'):
            res += c
    return res

def rm_dot(s): 
    # 1. 연속된 점은 하나로
    s = re.sub(r'\.+', '.', s)
    # 2. 앞뒤 점 제거
    s = s.strip('.')
    return s

def length_short_2(str):
    if len(str) <= 2:
        str += str[-1]*(3-len(str))
    return str
        
def solution(new_id):
    answer = ''
    # print(ord('-')) 45
    # print(ord('_')) 95
    # print(ord('.')) 46
    new_id = rm_dot(rm_mark((cap_to_lower(new_id))))
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 15:
        new_id = new_id[:15]
    answer = length_short_2(rm_dot(new_id))
    
    #print(rm_dot('....ka.t..es.t'))
    return answer

