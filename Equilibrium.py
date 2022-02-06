"""For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7"""

def solution(A):
    if(len(A)==2):
        return abs(A[0]-A[1])
    
    firstCutSum=A[0]
    secondCutSum=sum(A)-A[0]
    lowestDifference=abs(firstCutSum-secondCutSum)
    
    for i in range(1,len(A)-1):
        firstCutSum+=A[i]
        secondCutSum-=A[i]

        difference=abs(firstCutSum-secondCutSum)
        if(lowestDifference>difference):
            lowestDifference=difference
    return lowestDifference

print(solution([3,1]))