num = int(input ("Enter a 4-digit number: "))
reversed_number = 0
div = 1
mul = 1000
for n in range(0,4):
    reversed_number += int((num//div%10) * mul)
    div *= 10
    mul /= 10
print (f"The reversed number is: {reversed_number}")
num1 = num
num2 = reversed_number
div = 1
mul = 1000
for n in range(0,4):
    a = int(num1//mul%10) 
    b = int(num2//div%10)
    div *= 10
    mul /= 10
    if a==b :
        continue
    else:
        break

if n==3 :
    print ("The reversed number is correct")