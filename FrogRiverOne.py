def solution(X, A):
    riverPositions=[False]*(X+1)
    for time in range(len(A)):
        pos=A[time]
        if not riverPositions[pos]:
            riverPositions[pos]=True
            X-=1
            if X==0:
                return time
    return -1

print(solution(5,[1,3,1,3,5,2,4,1,3]))