# 배열 두개의 합을 구하여 저장하기

# 배열안의 원소의 길이와 배열의 길이는 항상 같음.
arr1 = [[1,4],[3,6],[3,4]]
arr2 = [[2,2],[4,5],[1,4]]

def solution(arr1,arr2):
    answer = []
    mr = []
    for i1, i2 in zip(arr1, arr2):
        for idx in range(0,len(i1)):
            result = i1[idx] + i2[idx]
            mr.append(result)
        answer.append(list(mr))
        mr = []
    return answer
    
print(solution(arr1,arr2))