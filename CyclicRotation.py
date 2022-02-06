def solution(A,K):
    if(len(A)+1==K):
        return A
    else:
        resultArray=[None]*len(A)
        for i in range(len(A)):
            resultArray[(i+K)%len(A)]=A[i] # ((i+k)%size of array) for rotation
        print(resultArray)



solution([3,4,5,6,7],2)