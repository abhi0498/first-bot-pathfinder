def checkP(item):
    for i in range(m):
        for j in range(m):
            if item in grid[i][j]:
                return [i, j]


def displayPathtoPrincess(n, grid):
    # print all the moves here
    p = checkP('p')
    b = checkP('m')
    while True:
        if b[0] == p[0] and b[1] == p[1]:
            exit()
        if b[0] < p[0]:
            b[0] += 1
            print("DOWN")
        elif b[0] > p[0]:
            b[0] -= 1
            print("UP")
        elif b[1] > p[1]:
            b[1] -= 1
            print("LEFT")
        elif b[1] < p[1]:
            b[1] += 1
            print("RIGHT")


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
