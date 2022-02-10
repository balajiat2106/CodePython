def solution(A):
    tempList=[]*3
    resProduct=0
    for i in range(3):
        tempList.append(max(A))
        tempList[i]*=max(A)
        print(tempList)
        A.remove(max(A))
        print(A)
    

    return resProduct
print(solution([-3,1,2,-2,5,6]))