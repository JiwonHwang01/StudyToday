def func1():
    a = int(input())
    if a<1 or a>1000000:
        return
    count = 0

    while a != 1:
        if a % 3 ==0:
            a = a / 3
            count += 1
        elif a % 2 == 0:
            a = a / 2
            count += 1
        else :
            a = a - 1
            count - 1 

        
    print(count)
func1()