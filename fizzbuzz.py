def fizzbuzz(number):
    if(number%3==0 and number%5==0):
        print("fizzbuzz")
    elif(number%5==0):
        print("buzz")
    elif(number%3==0):
        print("fizz")
    else:
        print(number)

fizzbuzz(int(input()))