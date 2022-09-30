N = open('NuMBeRS', 'r')
List = N.readline()
List_1 = List.split(' ')
print(List_1)
for i in range(0, len(List_1) - 1):
    if List_1[i + 1] <= List_1[i]:
        for k in range(i, -1, -1):
            if List_1[k + 1] <= List_1[k]:
                t = List_1[k + 1]
                List_1[k + 1] = List_1[k]
                List_1[k] = t
print(List_1)
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