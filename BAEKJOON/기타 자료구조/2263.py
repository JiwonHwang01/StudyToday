#Recursion Error #Tree
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

def traverse(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root, end=' ')
    
    root_index = in_order.index(root)
    l_count = root_index - in_start
    r_count = in_end - root_index

    traverse(in_start, root_index - 1, post_start, post_start + l_count - 1)
    traverse(root_index + 1, in_end, post_end - r_count, post_end - 1)
    
traverse(0, n-1, 0, n-1)