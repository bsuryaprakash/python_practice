# input the number

n = int(input("Enter a number: "))
print(f'Entered number is:  {n} of type {type(n)}')
reverse=0
while n!=0:
    reverse = reverse*10 + n%10
    print(f'n --> value {n} and reverse {reverse}')
    n = (n//10)

print(f'Reversed number is {reverse}')

