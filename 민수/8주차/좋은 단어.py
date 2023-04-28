import sys

n = int(sys.stdin.readline())

count = 0

for i in range(n):
    word = sys.stdin.readline().rstrip()
    stack = []
    
    for i in range(len(word)) :
        if stack :
            if word[i] == stack[-1] :
                stack.pop()
                            
            else :
                stack.append(word[i])
        else :
            stack.append(word[i])
 
    if not stack :
        count += 1
        
print(count)