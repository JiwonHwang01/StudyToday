import math
import sys
import time


read = sys.stdin.readline

num1, num2 = map(int,read().split())
start_time = time.time()

def counting_num(num, N):
    count = 0
    while num > 0:
        num = num // N
        count += num

    return count

print(min(counting_num(num1,5)-counting_num(num2,5)-counting_num(num1-num2,5), counting_num(num1,2)-counting_num(num2,2)-counting_num(num1-num2,2)))
