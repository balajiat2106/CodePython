from functools import reduce


def solution(A):
    tempList=[]*3
    resProduct=0

    for i in range(3):
        tempList.append(max(A))
        resProduct=tempList[i]*max(A)
        A.remove(max(A))

    
    resProduct=reduce((lambda x,y:x*y),tempList)
    return resProduct
print(solution([-3,1,2,-2,5,6]))