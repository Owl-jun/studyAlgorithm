# 기수 변환하기 (n진수 구하기)

# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기.

def card_conv(x: int, r: int) -> str:
    """ 정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환 """

    d = '' # result
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x)) # 변환하기전 자릿수
    print(f'{r:2}|{x:{n}d}')

    while x > 0:
        print('   +' + (n+2) * '-')
        if x // r:
            print(f'{r:2} | {x:{n}d} --- {x % r}')
        else:
            print(f'     {x // r:{n}d} --- {x % r}')
        d += dchar[x % r] # 해당하는 문자열 꺼내어 d 에 저장
        x //= r # 반복 여부판단

    return d[::-1] # 역순으로 저장


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True :
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break
        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36 :
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한번 더 변환할까요? Y / N :")
        if retry in ('N','n'):
            break
