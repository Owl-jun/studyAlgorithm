# 반복하는 알고리즘

# 1부터 n까지 정수의 합 구하기.


print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))


# for 사용

# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(f'1부터 {n}까지의 합은 {sum}입니다.')


# while 사용
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
# print(f'1부터 {n}까지의 합은 {sum}입니다.')

# 마음대로 해보기
def sumNums():
    global n
    result = n*(n+1)//2
    return result

print(sumNums())