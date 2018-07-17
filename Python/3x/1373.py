while True:
    k = int(input())
    if (k == 0): break

    a = input()
    b = input()

    s1 = " " + a
    s2 = " " + b

    M = [[0 for x in range(len(s1))] for y in range(len(s2))]

    for Y in range(1,len(s1)):
        for X in range(1,len(s2)):
            if(s1[Y] == s2[X]):
                M[Y][X] = 1 + M[Y-1][X-1]
            else:
                M[Y][X] = max(M[Y][X - 1],M[Y - 1][X])


    print(M[len(a)][len(b)])
