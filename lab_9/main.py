import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

INF = 2**31

def dfs(u, t, f, c, n, c_min, visited):
    #print(u)
    if u == t:
        #print(u, c_min)
        return c_min
    
    visited[u] = True
    for v in range(n+1):
        if not visited[v] and f[u][v] < c[u][v]:
            delta = dfs(v, t, f, c, n, min(c_min, c[u][v] - f[u][v]), visited)

            if delta > 0:
                #print(u, v)
                f[u][v] += delta
                f[v][u] -= delta
                return delta
    return 0

def is_bigraph(graph: nx.Graph):
    q: deque = deque()
    nodes = list(graph.nodes.items())
    q.append(nodes[0][0])

    visited = [False for _ in range(max(graph.nodes))]
    colors = [0 for _ in range(max(graph.nodes))]
    
    colors[nodes[0][0] - 1] = 1

    while q:
        v = q.popleft()
        visited[v-1] = True

        for u in graph.adj[v]:
            if colors[u-1] > 0:
                continue

            q.append(u)
            
            if colors[v-1] == 1:
                if colors[u-1] == 1:
                    return False
                elif colors[u-1] == 0:
                    colors[u-1] = 2
            elif colors[v-1] == 2:
                if colors[u-1] == 2:
                    return False
                elif colors[u-1] == 0:
                    colors[u-1] = 1
    return True, colors

def ford_fulkerson(graph: nx.Graph, colors: list[int]):
    n = max(graph.nodes)
    graph.add_node(n+1)
    graph.add_node(n+2)

    c = [[0 for i in range(n+3)] for j in range(n+3)]
    f = [[0 for i in range(n+3)] for j in range(n+3)]

    for i in range(2, n+1):
        if colors[i-1] == 1:
            graph.add_edge(n+1, i)

            c[n+1][i] = 1
            for u in graph.adj[i].keys():
                c[i][u] = 1
        else:
            graph.add_edge(n+2, i)

            c[i][n+2] = 1
    
    flow = 0
    while True:
        visited = [False for _ in range(n+3)]
        d = dfs(n+1, n+2, f, c, n+2, INF, visited)

        if not d:
            break

        flow += d
    
    cut = set()
    for i in range(len(f)):
        for j in range(len(f)):
            if f[n+1][i] == 1 and f[n+2][j] == -1 and f[i][j] == 1:
                cut.add((i, j))

    return flow, cut

def dfs_chain(v, f, visited, graph: nx.Graph, colors):
    if visited[v]:
        return False
    
    visited[v] = True
    for u in graph.adj[v].keys():
        if colors[u-1] != 2:
            continue
        #print(v, u, f[u], f)
        if (f[u] == -1 or dfs_chain(f[u], f, visited, graph, colors)):
            f[u] = v
            return True
    return False


def growing_chains(graph: nx.Graph, colors: list[int]):
    f = [-1 for _ in range(graph.number_of_nodes() + 2)]

    for i in range(2, graph.number_of_nodes() + 2):
        #print("current", i)
        if colors[i-1] == 1:
            visited = [False for _ in range(graph.number_of_nodes() + 2)]
            dfs_chain(i, f, visited, graph, colors)

    cut = []
    for j in range(2, graph.number_of_nodes() + 2):
        if f[j] != -1 and colors[j-1] == 2:
            cut.append((j, f[j]))
    
    return cut
    



graph: nx.Graph = nx.Graph()
n = 16

#graph.add_nodes_from(range(1,17))
edges = [(9,12), (5,14), (11,14), (4,13), (4,7), (11,12),
         (9,14), (14,16), (5,12), (2,8), (8,10), (10,12),
         (2,12), (7,12), (4,9), (3,4), (8,9), (12,13), (7,14),
         (14,15), (8,15), (6,12), (6,8), (4,6), (2,4), (12,15),
         (5,8), (6,14), (8,13), (4,5), (2,14), (8,11), (8,16),
         (4,15), (3,12)]

graph.add_edges_from(edges)

flag, colors = is_bigraph(graph)
print(f"Is bipartite graph? {flag}")

pos = {}

for v in range(2, max(graph.nodes) + 1):
    if colors[v-1] == 1:
        pos[v] = [-0.36363636, v]
    else:
        pos[v] = [1, v]

flow, cut = ford_fulkerson(graph, colors)

print(flow)
print(cut)

graph.remove_node(n+1)
graph.remove_node(n+2)

ax = plt.subplot()
ax.set_title("Ford-Fulkerson")
nx.draw(graph, pos, with_labels=True)
nx.draw_networkx_edges(nx.Graph(cut), pos=pos, edge_color='red')
plt.show()

cut1 = growing_chains(graph, colors)
comb = len(cut1)

print(comb)
print(cut1)

ax1 = plt.subplot()
ax1.set_title("Magnifying chains")
nx.draw(graph, pos, with_labels=True)
nx.draw_networkx_edges(nx.Graph(cut1), pos=pos, edge_color='red')
plt.show()