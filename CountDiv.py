from math import ceil,floor
def solution(A,B,K):
    
    start=ceil(A/K)
    end=floor(B/K)
    return end-start+1

print(solution(0, 1, 11))

    