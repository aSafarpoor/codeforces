''' https://codeforces.com/problemset/problem/1686/B '''

n = int(input())
for _ in range(n):
    m = input()
    a = list(map(int,input().split(' ')))
    c = 0
    if len(a)==1:
        print(0)
        continue

    max_ = a[0]
    for i in a[1:]:
        if i<max_:
            c +=1
            max_ = -1
        elif i>max_:
            max_ = i

    print(c)
