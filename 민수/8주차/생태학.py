import sys
from collections import defaultdict

count = 0

hashmap = defaultdict(int)

while True :
    word = sys.stdin.readline().rstrip()
    
    if not word :
        break
        
    hashmap[word] += 1
    count += 1
    
key = list(hashmap.keys())
key.sort()

for i in key :
    print("%s %.4f" %(i, hashmap[i] / count * 100))