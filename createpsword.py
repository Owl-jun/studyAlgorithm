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
