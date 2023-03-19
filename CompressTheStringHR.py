# Enter your code here. Read input from STDIN. Print output to STDOUT

String = list(input())
String.append("*")
ans = []
count=1
for i in range(len(String)):
    if String[i]!='*' and String[i]==String[i+1]:
        count+=1
    elif String[i]=='*':
        break
    else:
        x = (count,int(String[i]))
        ans.append(x)
        count=1
for item in ans:
    print(str(item),end=" ")
