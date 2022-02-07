def solution(A):
    suffixSums=[0]*(len(A)+1)
    for i in range(len(A)-1,-1,-1):
        suffixSums[i]=A[i]+suffixSums[i+1]

    count=0
    for i in range(len(A)):
        if(A[i]==0):
            count+=suffixSums[i]
        if count>1000000000:
            return -1
    return count

print(solution([0,1,0,1,1]))