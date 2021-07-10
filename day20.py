# 리스틍에서 임의의 원소값을 업데이트하기

def change(lst, idx, val):
    """ lst[idx] 값을 val 로 변경하기"""
    lst[idx] = val

x = [11, 22, 33, 44 ,55]
print('x =', x)

index = int(input("업데이트할 인덱스값을 입력하세요. : "))
value = int(input("새로운 값을 입력하세요. : "))
change(x,index,value)
print(f'x = {x}')