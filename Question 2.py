for _ in range(int(input())):
    a,b,c,x,y = map(int,input().split())
    if(a+b+c == x+y):
        if((x>=a or x>=b or x>=c)and(y>=a or y>=b or y>=c)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
