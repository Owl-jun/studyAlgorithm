# cnt = 몇개 출력? / brcnt = 몇개마다 줄바꿈?
def printAndBr(cnt, brcnt):
    for i in range(cnt // brcnt):
        print('*' * brcnt)
    if cnt % brcnt:
        print('*' * (cnt%brcnt))
printAndBr(14,5)