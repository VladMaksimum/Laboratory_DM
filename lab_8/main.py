from collections import deque
import numpy as np

INF = 2**31

def dfs(u, t, f, c, n, c_min, visited):
    if u == t:
        return c_min
    
    visited[u] = True
    for v in range(n):
        if not visited[v] and f[u][v] < c[u][v]:
            delta = dfs(v, t, f, c, n, min(c_min, c[u][v] - f[u][v]), visited)

            if delta > 0:
                f[u][v] += delta
                f[v][u] -= delta
                return delta
    return 0


def ford_fulkerson(s: int, t: int, c: list[list[int]], n: int):
    flow = 0
    f = [[0 for _ in range(n)] for _ in range(n)]
    
    while True:
        visited = [False for _ in range(n)]
        d = dfs(s, t, f, c, n, INF, visited)

        if not d:
            break

        flow += d
    
    return flow, f

def min_cut(s, t, c, n, f):
    A = set()
    B = set()

    visited = [False for _ in range(n)]
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        u = q.popleft()

        for v in range(n):
            if c[u][v] > 0 and f[u][v] == 0 and not visited[v]:
                visited[v] = True
                q.append(v)

    A = [i for i in range(n) if visited[i]]
    B = [i for i in range(n) if not visited[i]]

    cut = []
    for u in A:
        for v in B:
            if f[u][v] != 0:
                cut.append((u, v))
    
    return cut


c = [
    [0, 5, 9, 0, 0, 0, 0, 0, 4],
    [0, 0, 2, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 2, 7, 7, 0, 0, 0, 0],
    [0, 0, 7, 3, 3, 3, 0, 0, 0],
    [0, 0, 7, 0, 0, 7, 7, 0, 0],
    [0, 0, 4, 0, 0, 0, 2, 7, 0]
]

s = 0
t = 2
n = 9

c1 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if c[i][j] != 0:
            c1[i][j] = np.random.randint(100, 1000)

print("First network")
max_flow, f = ford_fulkerson(s, t, c, n)
print(f'{max_flow=}')
cut = min_cut(s, t, c, n, f)
print(f'{cut=}')

print("==========")

print("Random network")
for row in  c1:
    print(row)

max_flow, f = ford_fulkerson(s, t, c1, n)
print(f'{max_flow=}')
cut = min_cut(s, t, c1, n, f)
print(f'{cut=}')

