#

n = 3
text = ['abc','cde','exercize','expo','origin','normal','lack','korea','abc']

def solution(n,text):
    bucket = []
    cnt = 0
    num = 0
    for i in text:
        if i in bucket:
            if len(text) % n == 0:
                num = n
            else:
                num = len(text) % n  
        bucket.append(i)
        if len(bucket)%n == 1:
            cnt += 1
    if num == 0:
        cnt = 0
        num = 0

    return [cnt,num]
    
print(solution(n,text))