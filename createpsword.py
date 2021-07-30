# 무작위 비밀번호 생성기

import random
def createpsword(passlen):
    s = 'abcdefghijklmnopqrstuvwxyz01234567889ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$.?'
    password = []
    for i in range(3):
        p = "".join(random.sample(s, passlen))
        password.append(p)
    return password

print(f'추천 비밀번호 : {createpsword(8)}')


while True:
    i1 = int(input('마음에 안드시나요? (다시뽑으려면 0, 종료하려면 1 입력) :'))
    if i1 == 0:
        print(f'추천 비밀번호 : {createpsword(8)}')
    else:
        print('프로그램을 종료합니다.')
        break