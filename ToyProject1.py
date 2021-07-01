# 기본 프로그램

scoredic = {}
i = 1
while True :
    score = int(input('{0}번 학생의 점수를 입력하세요. (101 입력시 프로그램 종료) : '.format(i)))
    if score == 101:
        break
    scoredic[f'{i}번 학생 점수'] = score
    i = i + 1

with open('score.txt', 'w') as f :
    for cnt in scoredic.keys():
        f.write(cnt+' : '+str(scoredic[cnt]))
        f.write('\n')

# 삭제 기능

import re
try:
    delNum = int(input('몇번 학생의 기록을 삭제할까요? (없을시 엔터) : '))
    scoreLst = []
    with open('score.txt', 'r') as d :
        p = re.compile(f'[{delNum}][번]')
        lines = d.readlines()
        for j in lines:
            line = j.strip()
            m = p.search(line)
            if m: continue
            else: scoreLst.append(line)

    with open('score.txt', 'w') as _ :
        pass
    with open('score.txt', 'a') as a :
        for k in scoreLst:
            a.write(k)
            a.write('\n')
except: pass

# 추가/수정 기능 (특정 번호 추가, 정렬기능포함)

while True:
    try:
        StuNum = int(input('수정 or 추가하려는 학생의 번호를 입력하세요 (없을시 엔터): '))
        StuScore = int(input('점수를 입력하세요 : '))
        scoredic[f'{StuNum}번 학생 점수'] = StuScore
        cont = input('계속하시겠습니까? Y/N')
        if cont == 'N': break
    except: break

with open('score.txt', 'w') as f2:
    for cnt in sorted(scoredic.keys()):
        f2.write(cnt+' : '+str(scoredic[cnt]))
        f2.write('\n')



# 특정 학생의 시험점수 확인하기.

while True:
    FindScore = input('점수 확인할 학생의 번호만 입력하세요. (없을시 엔터)')
    Check = FindScore +'번 학생 점수'
    try:
        print(f'{FindScore}학생의 점수는 {scoredic[Check]}점 입니다.')
    except:
        print('해당 번호의 학생의 데이터가 존재하지 않습니다.')
    Uexit = input('계속 진행하시겠습니까? Y/N')
    if Uexit == 'N':
        break

# 점수들 최고점과, 최저점, 학생점수 총합과 평균 출력하기

maximum = max(scoredic.values())
for key, value in scoredic.items():
    if value == maximum:
        maximumNum = value
        maximumMan = key    
        print(f'반 내 최고점 {maximumMan} {maximumNum}점.')

minimum2 = min(scoredic.values())

for key2, value2 in scoredic.items():
    if value2 == minimum2:
        minimumNum = value2
        minimumMan = key2
        print(f'반 내 최저점 {minimumMan} {minimumNum}점.')

total = sum(scoredic.values())
print(f'반 점수 총합 {total}점, 평균 {total/len(scoredic.values())}점')