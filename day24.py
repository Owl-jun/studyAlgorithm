import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하시면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s.lower() == 'end':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값을 입력하세요.: '))

idx = seq_search.seq_search(x, ky)
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')


t = (4,7,45,2)
s = 'string'
a = ['BTS','BLACKPINK',"AESPA"]

print(f'{t}에서 45의 인덱스는 {seq_search.seq_search(t,45)}입니다.')
print(f'{s}에서 n의 인덱스는 {seq_search.seq_search(s,"n")}입니다.')
print(f'{a}에서 AESPA의 인덱스는 {seq_search.seq_search(a,"AESPA")}입니다.')