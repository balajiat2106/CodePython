
def DecimalToBinary(inputNumber):
    if(inputNumber>1 and inputNumber<2147483647):
        return bin(inputNumber)[2:]
    else:
        return 0

def Solution(N):
    LongestGapCount=0
    ZeroCount=0
    bNum=DecimalToBinary(N)
    if(bNum!=0):
        for x in bNum:
            if(int(x)==0):
                ZeroCount+=1
            else:
                if(LongestGapCount<ZeroCount):
                    LongestGapCount=ZeroCount
                ZeroCount=0
    
    print(LongestGapCount)



        

Solution(int(input("Enter any number: ")))