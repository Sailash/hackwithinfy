def outer_function(x):
    list1 = []
    def inner_func(n):
        if n in list1:
            return 
        list1.append(n)
        n=n+1
        n=str(n).strip('0')
        n=int(n)
        inner_func(n)

    inner_func(n)
    return len(list1)

n=int(input())
count = outer_function(n)
print(count)
