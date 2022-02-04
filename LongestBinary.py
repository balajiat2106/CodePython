def DecimalToBinary(inputNumber):
    if(inputNumber>1 and inputNumber<2147483647):
        return bin(inputNumber).replace("0b", "")
    else:
        return 0

def Solution(bNum):
    LongestGapCount=0
    ZeroCount=0
    if(bNum!=0):
        listNum=list(map(int,str(bNum)))
        print(listNum)
        for x in range(0,len(listNum)):
            if(listNum[x]==0):
                ZeroCount+=1
            else:
                if(LongestGapCount<ZeroCount):
                    LongestGapCount=ZeroCount
                ZeroCount=0
        print(ZeroCount,LongestGapCount)



        

Solution(DecimalToBinary(int(input("Enter any number: "))))