import numpy as np
inp=[1,2,3,10,9,5,7,11]
print(len(inp))
sortedInp=np.sort(inp)
print(sortedInp)
for i in range(1,len(inp)+1):
    if(i not in inp):
        print(i)

