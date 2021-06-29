# + 와 - 를 번갈아 출력하기

def printTwoChar(a,b, cnt):
    for _ in range(cnt // 2): # 인덱싱이 필요없을시 버리는 변수로 언더스코어 '_' 사용가능
        print(a+b, end='')
    if cnt % 2:
        print(a, end='')


printTwoChar('-','+',13)