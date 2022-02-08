import math
def solution(A,B):
    count=0
    for i in range(A,B+1):
        sqrt=(int)(math.sqrt(i))
        if sqrt*(sqrt+1)==i:
            count+=1
    return count


print(solution(21,29))