#다중 루프 알아보기

#구구단 곱셈표 출력하기

def GuGuDan():
    print('-'*27)
    for i in range(1,10):
        for j in range(1,10):
            print(f'{i*j:3}', end='')
        print()
    print('-'*27)

GuGuDan()