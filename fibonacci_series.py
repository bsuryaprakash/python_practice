# Fibonacci series

num = 10
first,second = 0,1
fib_list = []

for i in range(0,num,1):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    fib_list.append(result)




print(f' Fibonacci series: {fib_list}')