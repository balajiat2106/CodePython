def solution(A):
    resultArray=[]
    tempString=""
    print(A)
    for i in range(1,len(A)):
        if(i<len(A)):
            left=str(A[i-1])
            right=str(A[i])
            if left==right:
                print("if",tempString,left,right)
                tempString+=left
                print(resultArray)
                
            else:
                print("else",tempString,left,right)
                tempString+=left
                resultArray.append(tempString)
                
                tempString=""
                if(i==int(len(A)-1)):
                    print(i,len(A)-1,right)
                    tempString+=right
                    resultArray.append(tempString)
                print(resultArray)

    return len(resultArray)

print(solution("babaa"))

