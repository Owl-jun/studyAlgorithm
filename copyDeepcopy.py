# 리스트 원소와 복사

# copy() 함수는 조심해서 사용해야합니다. 리스트를 복사한 후 원소값을 변경하면, 복사된 원솟값 까지 변경이 됩니다.
# 이를 얕은 복사 라고 하는데, 이는 모든 원소가 참조하는 곳 까지 복사가 됩니다. 그리하여 복사된 값과 원본 중 하나라도 변경사항이 있으면 같이 변경이 됩니다.

# 이러한 문제를 해결하기 위하여 깊은 복사를 사용하게 되는데, copy 모듈 안의 deepcopy() 함수로 수행하게 됩니다.
# 이는 두 개 중 하나만 변경해도 두가지 모두가 변경되지 않습니다.