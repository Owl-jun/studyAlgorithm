# 2자리 양수(10-99) 입력 받기

def tenTohun():
    while True:
        result = int(input('2자리 수의 양수만 입력 : '))
        # if result >= 10 and result <=99: 
        # if 10 <= result <= 99: 간결한 if문
        if not(result < 10 or result > 99):  #드모르간의 법칙 (부호를 반대로 바꾸고 and 를 or로 바꾼다, 그다음 not 으로 전부 반대로)      
            return result
            
        

print(tenTohun())