a,b=3,3 # 변수(객체)는 자료형을 참조 하기때문에 (좌측에서는 int 3) 값이 같으면 두 객체의 id도 같다.
ast = [123] # 리스트는 리터럴(고정된 값)이 아니기 때문에 값이 같아도 서로 다른 id를 가진다.
bst = [123] 
cst = ast # 리스트 복제 (ast값 바꾸면 cst값도 바뀜)
print(a is b) # True
print(ast is bst) # False
print(ast is cst) # True

ast.append(234)
print(cst)
cst.append(345)
print(ast)