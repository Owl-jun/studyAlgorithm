# 10~99사이의 난수 n개 생성하기 (13이나오면 중단)

import random

def gotcha(n):
    for _ in range(n):
        r = random.randint(10,99)
        print(r, end=' ')
        if r == 13: 
            print('\n프로그램을 중단합니다.')
            break
    else: print('\n난수 생성을 종료합니다.')

gotcha(5)