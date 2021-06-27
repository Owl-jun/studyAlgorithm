# 세 정수의 대소 관계와 중앙값 구하기

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print(med3(71,71,90))

# 두번째 방법
def med3two(a,b,c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c <= b) or (a < b and c > b):
        return b
    return c

# 세 정수의 중앙값 구하기.

def midNum(a,b,c):
    lst = [a,b,c]
    lst.sort()
    return lst[1]

print(midNum(3,6,1))


# 입력 받은 정수의 부호 양수만 출력하기.

while True:
    n = int(input("정수를 입력하세요. : "))
    if n < 0:
        print(f"현재 입력하신 값은 음수입니다. {n}")
    elif n == 0 :
        print(f"오류발생. 입력하신 값을 확인하세요. (0입력시 오류발생){n}")
    else : 
        print(f"현재 입력하신 수는 양수입니다. 입력한값 : {n}")
        break


# 입력 받은 정수의 부호 (양수, 음수, 0) 출력하기

n = int(input("정수를 입력하세요. : "))
if n > 0:   # 입력받은 n이 0보다 큰 숫자일때 실행.
    print('이 수는 양수입니다.')
elif n < 0: # 입력받은 n이 0보다 작은 숫자일때 실행.
    print("이 수는 음수입니다.")
else: # 위의 두가지 어느것에도 포함되지 않을때 실행.
    print("이 수는 0입니다.")
