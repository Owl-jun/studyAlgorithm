# 검색 알고리즘

# 선형 검색
# 직선모양 (선형) 으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘

def seq_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    num = int(input('원소의 개수를 입력하시오. : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('찾는 값을 입력하세요. (정수형) : '))


    idx = seq_search(x,ky)

    if idx == -1 :
        print('그런 값은 존재하지 않습니다.')
    else :
        print(f'검색결과 : x[{idx}]')