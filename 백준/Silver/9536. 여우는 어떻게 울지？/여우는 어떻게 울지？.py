import sys

read = sys.stdin.readline

T = int(read())
for i in range(T):
    total_sound = read().split()
    tmp = []
    while True:
        line = read().split()
        if line[-1] == 'say?':
            print(*total_sound, sep=' ')
            break
        if line[-1] in tmp:
            continue

        if line[-1] in total_sound:
            total_sound = [i for i in total_sound if i != line[-1]]
            tmp.append(line[-1])
        else:
            pass