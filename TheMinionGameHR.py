def minion_game(string):
    # your code goes here
    String = list(string.lower())
    isVowel = list('aeiou')
    
    p1,p2 = 0,0
    
    for i in range(len(String)):
        
        if String[i] in isVowel:
            p1+=(len(String)-i)
        else:
            p2+=(len(String)-i)
    
    # print(p1,p2)
    if p1>p2:
        print(f'Kevin {p1}')
    elif p1<p2:
        print(f'Stuart {p2}')
    else:
        print('Draw')
        
    
    

if __name__ == '__main__':
    String = input()
    minion_game(String)
