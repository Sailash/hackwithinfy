t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sort = sorted(set(arr))
    maximum = 0
    for i in sort:
        count = 0
        idx = 0
        while idx<n:
            if i == arr[idx]:
                count = count + 1
                idx = idx + 1
            idx = idx + 1
        if count>maximum:
            maximum = count
            a = i
    print(a)

