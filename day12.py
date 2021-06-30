# 직각 이등변 삼각형으로 출력하기.

def samGak(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*', end='')
        print()

samGak(2)

# 우측이 직각인 이등변 삼각형

def samGak2(n):
    for i in range(1,n+1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()
samGak2(5)