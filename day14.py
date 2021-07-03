from max_of import *
import random

num = int(input('난수의 개수를 입력.: '))
lo = int(input('난수의 최소값을 입력.: '))
hi = int(input('난수의 최대값를 입력.: '))

x = [None] * num
for i in range(num):
    x[i] = random.randint(lo,hi)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {maximum(x)}입니다.')