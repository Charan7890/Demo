

string = input().split(' ')  # list

res = ""

for word in range(len(string)-1,-1,-1):
    
    res += string[word] +" "
    

print(res)
    

