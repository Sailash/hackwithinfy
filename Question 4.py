def time_check(keys):
    time = [keyTimes[0][1]]

    for i in range(1, len(keyTimes)):
        t = keyTimes[i][1] - keyTimes[i-1][1]
        time.append(t)
    
    idx = time.index(max(time))
    return chr(keys[idx][0]+ord('a'))


if __name__ == "__main__":
    # keyTimes = [[0, 2],[1, 5],[0, 9],[2, 15]]
    keyTimes = []
    num = int(input())
    _ = int(input())
    for i in range(num):
        keyTimes.append(list(map(int, input().split())))

    c = time_check(keyTimes)
    print(c)
