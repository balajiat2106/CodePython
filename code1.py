import math

def sumNumbers(tempItem):
    tempsum=0
    while tempItem:
        tempsum+=(tempItem%10)
        tempItem=math.floor(tempItem/10)
    return tempsum

def solution(A):
    permMax=-1
    refList=[]

    #Loop thru array    
    for index in range(len(A)):
        permSum=sumNumbers(A[index])
        
    
        if(permSum in refList):
            tempMax=A[index]+refList[permSum]
            #Check the max value
            if(tempMax>permMax):
                permMax=tempMax
        else:
            print(permSum,index)
            refList[permSum]=A[index]
    return permMax
print(solution([51,71,17,42]))