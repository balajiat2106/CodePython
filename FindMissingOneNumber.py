def solution(A):
    actual_sum=0
    for i in A:
        actual_sum+=i
    max_number=len(A)+1
    expected_sum=(max_number*(max_number+1)//2)
    return expected_sum-actual_sum

tempList=[2,3,4,6]
print(solution(tempList))