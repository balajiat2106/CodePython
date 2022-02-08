def solution(A,B,P):
    temp=[]
    for i in range(len(B)):
        if((B[i].find((str)(P)))!=-1):
            temp.append(A[i])
    return min(temp,key=len)

print(solution(["sander", "amy", "ann", "michael"],["123456789", "34567890", "789134156", "123123123"],2))