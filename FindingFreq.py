a = list(map(int,input().split(' ')))
a.sort()
freq = []
c=1
try:
    for i in range(len(a)):
        # if len(a)-1 == i:
        #     l.append
        if a[i]==a[i+1]:
            c+=1
        else:
            freq.append(a[i])
            freq.append(c)
            c=1
except:
    if(a[-2]==a[-1]):
        freq.append(a[i])
        freq.append(c)
    else:
        k=a[:len(a)-2]
        if a[-1] in k:
            pass
        else:
            c=1
            freq.append(a[i])
            freq.append(c)
            
j=0
for i in range(0,len(freq),2):
    print(freq[j],"is repeated",freq[j+1],"times")
    j+=2