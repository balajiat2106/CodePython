def solution(N, A):
    resultArray=[0]*(N)
    for i in range(0,len(A)):
        print("index",i)
        if A[i]>N:
            maxValue=max(resultArray)
            resultArray=[maxValue]*N
        else:
            print(A[i])
            resultArray[A[i]-1]+=1
        print(resultArray)
    return resultArray

print(solution(5,[3,4,4,6,1,4,4]))