# 주사위 시뮬레이터

import random

coin = False

print('please insert coin.')
ic = input('coin 을 입력하시면 코인이 충전됩니다.')

if ic.lower() == 'coin':
    coin = True

if coin:
    result = random.randint(1,6)
    print(f'result = {result}')


