t = int(input())
for i in range(t):
    n = int(input())
    cnt, ans = 1, 0
    while cnt ** 2 <= n:
        if cnt ** 2 <= n:
            ans += 1
        if cnt != 1 and (cnt * cnt * cnt) <= n:
            if (cnt * cnt * cnt)**0.5 != int((cnt * cnt * cnt)**0.5):
                ans += 1
        cnt += 1
    print(ans)