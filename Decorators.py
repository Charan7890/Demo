from math import factorial as f


def outer(fun):
    def inner():
        x = fun()
        result = f(x)
        return result 
    return inner
    
@outer
def fun():
    n = int(input('enter:'))
    return n
    

    
answer = fun()
print(answer)
