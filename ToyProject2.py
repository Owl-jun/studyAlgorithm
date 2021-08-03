# 명언 제조기 update.
import time
import random

def TodaySay(a):
    """ a: List """
    tm = time.localtime()
    ts = time.strftime('%Y-%m-%d', tm)
    select = random.randint(0,len(a)-1)
    return f'오늘 날짜 : {ts} {a[select]} 오늘 하루도 화이팅입니다!'


with open('test.txt', 'r') as f :
    test = f.readlines()
    
if __name__ == '__main__':
    print('지금, 당신에게 필요한 명언을 하나 내어드리겠습니다.')
    print(TodaySay(test))

