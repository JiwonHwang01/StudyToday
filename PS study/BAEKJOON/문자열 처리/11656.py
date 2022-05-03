import sys

word = sys.stdin.readline()

sub_str = [""] * (len(word)-1)

for i in range(len(word)-1):
    sub_str[i] = word[i:-1]

sub_str.sort()
print(*sub_str,sep='\n')
