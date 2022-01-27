print("Hello")
c=input()
print("Hello"+str(c))

temp=30
if(temp>20):
    print("hello")
elif(temp<10):
    print("Noooo")
else:
    print("nothing")

i=1
while i<=10:
    print(i*"3")
    i+=2

numbers=[1,2,3,4,5]
numbers.append(9)
numbers.insert(3, 7)
print(numbers)

print(0 in numbers)
print(3 in numbers)
print(len(numbers))

for number in range(10,25,3):
    print(number)