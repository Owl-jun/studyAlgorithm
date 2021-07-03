# 배열의 최대값, 최소값 구하는 함수생성.

def maximum(array):
    maximum = array[0]
    for i in array:
        if maximum < i :
            maximum = i
    return maximum

def minimum(array):
    minimum = array[0]
    for i in array:
        if minimum > i :
            minimum = i
    return minimum


if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요. : '))

    print(f"최댓값은 {maximum(x)}입니다.")