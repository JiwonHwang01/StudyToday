import sys

word = sys.stdin.readline().replace('\n','')
count = []

for i in range(ord("a"),ord("z")+1):
    count.append(-1)
for letter in word:
    count[ord(letter)-97] = word.index(letter)

print(*count,sep=" ")
    
