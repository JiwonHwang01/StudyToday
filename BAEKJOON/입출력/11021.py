count = int(input())

for i in range(1,count+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+": "+str(a+b))