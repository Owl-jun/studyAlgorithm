# 세 정수를 입력받아 최대값 구하기. 내가 생각하는 최적화 버젼

#ver 1.
def maxNums(list):
    return max(list)

lst = [3,4,6]
print(maxNums(lst))

#ver 2.
def maxNums2(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(maxNums2(3,4,6))