def solution(A):
    lookup=[]*len(A)
    count=0
    for i in range(len(A)):
        if(A[i] not in lookup):
            if(A.count(A[i]))==A[i]:
                lookup.append(A[i])
    if(len(lookup)>0):
        return max(lookup)
    else:
        return 0


print(solution([3,8,2,3,3,2]))
print(solution([3,1,4,1,5]))

print(solution([5,5,5,5,5]))