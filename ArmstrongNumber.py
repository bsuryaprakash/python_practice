# This is a program to find the armstrong number between 0 to n

num = int(input('Enter the number: '))

n = num
power = len(str(num))
armstrong_num = 0

while n != 0:
    digit = n % 10 # gives the last digit of the number
    armstrong_num += digit ** power
    n //= 10 # division that discards decimal part

if armstrong_num == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")