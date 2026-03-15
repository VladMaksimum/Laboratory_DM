import numpy as np
from numba import jit, prange

INF = 2**31

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

        if not graph[i-1][j-1] and i != j and not (i < 15 or j < 15):
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

def save(graph, file):
    with open(file, 'w') as f:
        for i, v in enumerate(graph):
            adjs = []
            for j in range(len(v)):
                if v[j]:
                    adjs.append(j)

            f.write(f'{i}: {adjs}\n')

def read(n, file):
    graph = np.zeros((n, n), dtype=np.bool)
    w = np.array([[INF for j in range(n)] for i in range(n)])

    with open(file) as f:
        line = f.readline()

        while line:
            v, adjs = line.split(":")

            adjs = adjs.split(',')
            adjs[0] = adjs[0][2::]
            adjs[-1] = adjs[-1][:-2:]
            v = int(v)

            for j in range(len(adjs)):
                graph[v][int(adjs[j])] = True
                graph[int(adjs[j])][v] = True

                w[v][int(adjs[j])] = 1
                w[int(adjs[j])][v] = 1
            
            line = f.readline()
    
    return graph, w

@jit(nopython=True, parallel=True, cache=True)
def floyd(graph, n, w):
    d = w
    next = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                next[i][j] = j
            else:
                next[i][j] = INF

    for i in prange(n):
        for u in prange(n):
            if d[u][i] == INF:
                continue

            for v in prange(n):
                if d[i][v] == INF:
                    continue
                
                if d[u][v] > d[u][i] + d[i][v] and u != v:
                    d[u][v] = d[u][i] + d[i][v]
                    next[u][v] = next[u][i]

    print("well done")
    return d, next

def save_dists(d, n):
    # print("and now here")
    with open(f'lab_7/distances/distance{n}.txt', 'w') as file:
        for i in range(n):
            for j in range(n):
                if d[i][j] == 2**31:
                    file.write('None ')
                else:
                    file.write(f'{d[i][j]} ')

            file.write('\n')

def find_way(d, next, u, v, file):
    if d[u][v] == INF:
        print('No path')

    c = int(u)
    with open(file, 'w') as f:
        while c != v:
            f.write(f'{c} ')
            c = int(next[c][v])
        
        f.write(f'{v}')

def dijkstra(s, graph, n):
    d = np.zeros(n)
    used = np.zeros(n)
    next = np.zeros(n)

    for v in range(n):
        d[v] = INF
        used[v] = False
        next[v] = INF
    
    d[s] = 0
    for i in range(n):
        v = None
        for j in range(n):
            if not used[j] and (v == None or d[j] < d[v]):
                v = j
        
        if d[v] == INF:
            break

        used[v] = True
        for e in range(n):
            if graph[v][e]:
                if d[v] + 1 < d[e]:
                    d[e] = d[v] + 1
                    next[e] = v
    
    with open(f'lab_7/distances/d_distance{n}.txt', 'w') as file:
            for i in range(n):
                if d[i] == 2**31:
                    file.write('None\n')
                else:
                    file.write(f'{d[i]}\n')

            file.write('\n')
    
    return d, next

def find_dijkstra_way(next, d, s, v, file):
    if d[v] == INF:
        print('No path')

    c = v
    with open(file, 'w') as f:
        while c != s:
            f.write(f'{c} ')
            c = int(next[c])
        
        f.write(f'{s}')


n = 31000
# graph = generate(n, int(n**(3/2)))
folder = 'lab_7/graphs/graph'
graph, w = read(n, f'{folder}{n}.txt')
d, next = dijkstra(0, graph, n)
find_dijkstra_way(next, d, 0, n-1, f'lab_7/paths/d_path{n}.txt')

