import sys

integer = int(sys.stdin.readline())
m_bin = ""
remain = 0

if integer == 0:
        m_bin = "0"

while integer:
    if integer == 2:
        m_bin = "110"+m_bin
        break
    remain = integer % -2 * -1
    if remain == 0 :
        integer = integer // -2
    else :    
        integer = integer // -2 + 1
    m_bin = str(remain) + m_bin

print(m_bin)
