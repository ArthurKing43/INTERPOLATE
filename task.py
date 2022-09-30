n = input("сколько:")
list_1 = []
for q in range(0, int(n)):
    x = input()
    List.append(x)
print(List)
for i in range(0, len(List)-1):
    if List[i+1] <= List[i]:
        for k in range(i, -1, -1):
            if List[k+1] <= List[k]:
                t = List[k+1]
                List[k+1] = List[k]
                List[k] = t
print(List)
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