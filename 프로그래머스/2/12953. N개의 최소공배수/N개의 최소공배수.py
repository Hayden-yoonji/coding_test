

def gcd(a,b) :
    while True :
        if (a%b == 0) :
            return b
        else :
            a,b=b,a%b

def lcm(a,b):
    return a*b // gcd(a,b)

    
def solution(arr):

    while len(arr) >=2:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a,b))
    
    return arr[0]
        