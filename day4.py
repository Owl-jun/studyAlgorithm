# a ~ b 사이의 연속하는 정수의 합 구하기.

def sumTwoNums(a,b):
    result = 0
    if a > b:
        a, b = b, a  # 두 값의 교환

    for i in range(a,b+1):
        if i < b:
            print(f'{i} + ', end='')
        result += i
        
    print(f'{b} = ', end='')
    print(result)    
    return result

print(sumTwoNums(8,3))