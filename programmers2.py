def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

participant = ['a','b','c']
completion = ['b','c']

participant2 = ['a','b','b','c']
completion2 = ['a','b','c']

print(solution(participant, completion))
print(solution(participant2, completion2))


