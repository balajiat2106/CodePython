def solution(A):
    B=set(A)
    print(B)
    missingValue=0
    c=max(set(A),key=A.count)
    print(c)
    for i in range(1,len(B)+1):
        print("i",i)
        if i not in B:
            missingValue=i
            break
    if(missingValue>0):
        return missingValue
    else:
        return max(B)+1

print(solution([-1,3,5,2,0,5,-9]))
