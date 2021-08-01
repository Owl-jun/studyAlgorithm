# 라이어 게임

import random

data = ['안경','짐바브웨','한국','축구','양말','콘크리트','건축물','그림','힙합','물','워터파크']
liar = ['도둑','면봉','북한','농구','아프리카','스펀지','마트','예술','음료']
choice = []
rank = []

i1 = int(input('라이어 게임을 시작합니다 참가인원을 입력해주세요 (2~6) : '))
while True:
    liarman = random.randint(1,i1)
    random.shuffle(data)
    random.shuffle(liar)
    for i in range(1,i1+1):
        enter = input('차례 넘기기 1 입력 : ')    
        if enter == '1':
            if i == liarman:
                print(f'제시어는 {liar[i]} 당신은 라이어 입니다.')
            else:
                print(f'제시어는 {data[0]}')
    for _ in range(1,i1+1):
        schoice = int(input('라이어는 누구? 번호만 입력 : '))
        choice.append(schoice)
    for c in choice:
        if (f'{c}번 : {choice.count(c)}') not in rank:
            rank.append(f'{c}번 : {choice.count(c)}')
    print(f'투표 결과 : {rank} 라이어는 {liarman}번 이었습니다.')
    conti = input("계속 하시겠습니까? Y/N")
    choice = []
    rank = []
    if conti.upper() == 'N':
        break