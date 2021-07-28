# 가위 바위 보!
# 컴퓨터와 가위바위보 게임 후 3점 획득시 게임 승리

import random

sel = ['가위', '바위', '보']
result = {0: '승리했습니다.', 1: '패배했습니다.', 2: '비겼습니다.'}
score =0

def checkWin(user, com):

    if not user in sel:
       print('잘못입력하였습니다. 다시 입력하세요')
       return 2

    print(f'사용자 ( {user} vs {com} ) 컴퓨터')
    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])
    return state


print('\n-------------------------------------------')
while True:
    user = input("가위, 바위, 보 : ")
    com = sel[random.randint(0, 2)]
    if checkWin(user, com) == 0:
        score += 1
        print(f'현재 점수 : {score}')
    else: print(f'현재 점수 : {score}')
    if score == 3:
        print('축하드립니다 3점을 모두 획득하셨습니다. 게임을 종료합니다.')
        break
print('-------------------------------------------\n')

