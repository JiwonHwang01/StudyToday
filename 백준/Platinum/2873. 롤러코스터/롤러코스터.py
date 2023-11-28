import sys
read = sys.stdin.readline

def func():
    r, c= map(int,read().split())
    happiness = [list(map(int,read().split())) for _ in range(r)]
    s= ""
    
    if r % 2 == 1 :
        s += ("R"*(c-1) + "D" + "L"*(c-1) + "D") * (r//2) + "R"*(c-1)
        print(s)
        return

    if c % 2 == 1:
        s += ("D"*(r-1) + "R" + "U"*(r-1) + "R") * (c//2) + "D"*(r-1)
        print(s)
        return
    

    min_val = 1000
    for i in range(r):
        for j in range(c):
            if (i+j) % 2 == 1:
                if happiness[i][j] < min_val:
                    min_val = happiness[i][j]
                    min_pos = [j, i]

    s += ("R"*(c-1) + "D" + "L"*(c-1) + "D") * (min_pos[1]//2)
    s += ("DRUR") * (min_pos[0]//2)
    
    if min_pos[0] % 2 == 0:
        s += "RD"
    else:
        s += "DR"
    
    s += ("RURD") * ((c-1-min_pos[0])//2)
    s += ("D" + "L"*(c-1) + "D" + "R"*(c-1)) * ((r-1-min_pos[1])//2)
    
    print(s)

func()