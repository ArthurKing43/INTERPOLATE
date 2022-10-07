N = open('NuMBeRS', 'r')
S = N.readline()
S_1 = S.split(' ')
S_2 = []
for j in S_1:
     x = int(j)
     S_2.append(x)
for i in range(0, len(S_2) - 1):
    if S_2[i + 1] <= S_2[i]:
        for k in range(i, -1, -1):
            if S_2[k + 1] <= S_2[k]:
                t = S_2[k + 1]
                S_2[k + 1] = S_2[k]
                S_2[k] = t
print(S_2)
'''3/ 8 2 1 4 i=0

3 8/ 2 1 4 i=1

3 8 2/ 1 4 i=1 k=1
3 2/ 8 1 4 k=0
2/ 3 8 1 4 k=0

2 3 8 1/ 4 i=2 k=2
2 3 1/ 8 4
2 1/ 3 8 4
1/ 2 3 8 4

1 2 3 8 4/
1 2 3 4/ 8
1 2 3 4 8'''