def fib(n):
    arr = [1, 1]
    if(n <= 2 and n >=0):
        return arr[0:n:];
    elif(n > 2):
        for i in range(n - 2):
            arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
        return arr
    else:
        raise ValueError