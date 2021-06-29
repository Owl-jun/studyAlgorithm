# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기.

def squareInc(area):
    for i in range(1,area+1):
        if i * i > area: break # i * i 가 area보다 커지게 되면 i가 가장 긴 변의 길이가 되기 때문에 사각형이 아니게 된다.
        if area % i: continue # 넓이(area) 에 i를 나누어 떨어지지 않으면 사각형 변의 길이가 될 수 없다.
        print(f'{i} * {area//i}') # 작은 변 부터 출력.

squareInc(32)