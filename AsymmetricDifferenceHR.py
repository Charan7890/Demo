# Enter your code here. Read input from STDIN. Print output to STDOUT

x = [0]*1001

a = int(input())

l1 = list(map(int,input().split(' ')))

for item in l1:
    x[item]+=1

b = int(input())

l2 = list(map(int,input().split(' ')))

for item in l2:
    x[item]+=1
    
count=0

for i in x:
    if i==1:
        count+=1
    else:
        pass

print(count)
