# 1부터 n까지 정수의 합 구하기

def addAll(n) :
    result = 0
    for i in range(1,n+1):
        result += i
    
    return result

print(addAll(3))