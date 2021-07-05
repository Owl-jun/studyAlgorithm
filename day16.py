# 리스트 원소 스캔
lst = ['John','George','Paul','Ringo']
#1 
for i in range(len(lst)):
    print(lst[i])

#2
for _ in lst:
    print(_)

#3
for index, name in enumerate(lst):
    print(f'{index+1}번 : {name}')

#4
for k, name2 in enumerate(lst, 1):
    print(f'{k}:{name2}')

# 튜플 원소 스캔또한 튜플 객체로 바꾼뒤 위의 방법을 사용한다.
