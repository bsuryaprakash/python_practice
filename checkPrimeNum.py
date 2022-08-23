#Check prime num!!

#n=num = int(input(f'enter the number: '))

list_of_prime = []
range_start = int(input(f'enter the range_start number: '))
range_end = int(input(f'enter the range_end number: '))

for x in range(range_start,range_end,1):
    n = num = x
    n = n // 2
    flag=0
    while n>2:
        n = n - 1
        if (num%n==0):
            flag=1
    if(flag!=1):
        list_of_prime.append(x)



print(f'List of prime numbers between {range_start} and {range_end} : {list_of_prime}')