# 소수 구하기
counter = 0 # 나눗셈 횟수
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수 저장 배열

prime[ptr] = 2 # 2는 소수의 초기값으로 지정
ptr += 1

prime[ptr] = 3 # 3은 소수
ptr += 1
 
for n in range(5,1001,2): # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n: # 이미 찾은 소수로 나눔
        counter += 2
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
             break
        i += 1
    else:
        prime[ptr] = n # 소수를 배열에 등록
        ptr += 1
        counter += 1

for k in range(ptr): # ptr의 소수를 출력
    print(prime[k])

print(f'{counter}회 반복')