#n=num = int(input(f'Enter the number: '))


for x in range(0,20000):
    n = num = x
    power = (len(str(n)))
    n_num = armstrong_num = 0
    while n != 0:
        n_num = n % 10
        armstrong_num = armstrong_num + pow(n_num, power)
        #print(f'cube number {n_num} = {(pow(n_num, power))} and Armstrong number:{armstrong_num}')
        n = n // 10

    if (armstrong_num == num): print(f'input: {num} and output: {armstrong_num} => Amstrong number -> {armstrong_num == num}')
print(f'last value of x {x}')