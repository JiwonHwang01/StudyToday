import sys
read = sys.stdin.readline

N = int(read())
dancers = set()
dancers.add("ChongChong")  # 처음엔 총총이만 춤을 춤

for _ in range(N):
    p1, p2 = read().strip().split()
    # 둘 중 한 명이라도 춤을 추고 있다면 → 전염!
    if p1 in dancers or p2 in dancers:
        dancers.add(p1)
        dancers.add(p2)

print(len(dancers))
