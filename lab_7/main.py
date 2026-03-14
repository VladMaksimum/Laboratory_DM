import numpy as np

def generate(n, m):

    graph = np.zeros((n, n), dtype=np.bool)
    # graph = [[False for _ in range(n)] for _ in range(n)]

    for i in range(4):
        for j in range(i+1, 5):
            graph[i][j] = True
            graph[j][i] = True
    
    graph[4][5] = True
    graph[5][4] = True
    graph[6][5] = True
    graph[5][6] = True

    for i in range(6, 9):
        for j in range(9, 14):
            graph[i][j] = True
            graph[j][i] = True
    
    graph[13][14] = True
    graph[14][13] = True

    for i in range(14, n-1):
        graph[i][i+1] = True
        graph[i+1][i] = True
    

    for k in range(1, m+1):
        r = np.random.random_sample()

        N = int(n**2 * r) + 1
        i = int(N / n) + 1
        j = N - (i-1) * n

        if not graph[i-1][j-1] and i != j:
            graph[i-1][j-1] = True
            graph[j-1][i-1] = True
        else:
            k -= 1
    return graph

def average_degree(graph, n):
    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j]:
                cnt += 1
    
    return cnt / (n)

n = 500
graph = generate(n, int(n**(3/2)))

