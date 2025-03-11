import sys

read = sys.stdin.readline



# 시작이 소문자가 아니다


def capital(words):
    for i in range(1,len(words)):
        words[i] = words[i][0].capitalize()+words[i][1:]
    return words

def isCapital(ch):
    if 65 <= ord(ch) < 91:
        return True
    else: return False

def small(word):
    res = ""
    for ch in word:
        if isCapital(ch):
            res = res + '_' + ch.lower()
            
        else: res += ch
    return res


if __name__ == '__main__':
    input = read().rstrip()
    words = []

    if not input:
        print("Error!")
        exit()

    if not 97 <= ord(input[0]) < 123:
        print("Error!")
        exit()
    
    if input[-1] == '_':
        print("Error!")
        exit()

    if '_' in input:
        words = input.split('_')
        if '' in words:
            print("Error!")
            exit()
        for word in words:
            for ch in word:
                if isCapital(ch):
                    print("Error!")
                    exit()

        
        words = capital(words)
        print(*words, sep='')

    else:
        print(small(input))
