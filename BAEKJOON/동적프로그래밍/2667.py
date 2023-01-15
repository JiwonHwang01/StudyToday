# 2096 내려가기 (슬라이딩 윈도우, DP)
import sys
input = sys.stdin.readline

n = int(input())
maxArr = [0]*3
minArr = [0]*3


for i in range(n):
    board = list(map(int,input().split()))

    tmpArr = [0]*3

    tmpArr[0] , tmpArr[1], tmpArr[2] = maxArr[0], maxArr[1], maxArr[2]
    maxArr[0] = max(tmpArr[0] + board[0], tmpArr[1] + board[0])
    maxArr[1] = max(tmpArr[0] , tmpArr[1], tmpArr[2]) + board[1]
    maxArr[2] = max(tmpArr[1] + board[2], tmpArr[2] + board[2])

    tmpArr[0] , tmpArr[1], tmpArr[2] = minArr[0], minArr[1], minArr[2]
    minArr[0] = min(tmpArr[0] + board[0], tmpArr[1] + board[0])
    minArr[1] = min(tmpArr[0] , tmpArr[1], tmpArr[2]) + board[1]
    minArr[2] = min(tmpArr[1] + board[2], tmpArr[2] + board[2])

#print(maxArr, minArr)
print(max(maxArr), min(minArr))