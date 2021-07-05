# 배열 원소를 역순으로 정렬하기

from typing import MutableSequence


def reverseArray(a = MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 개수를 입력. :'))
    lst = [None] * nx # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        lst[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverseArray(lst)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'lst[{i}] = {lst[i]}')