n_comp = int(input())
road = int(input())

input_edges = []
for j in range(road):
    a, b, weight = map(int, input().split())
    input_edges.append((weight, a, b))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, rank, a,b):
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        if rank[a]< rank[b]:
            parent[a] = b
        elif rank[a]> rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1

def kruskal(v, edges):
    #v = 노드 수, edges = 입력 받은 간선 간의 연결 및 가중치
    mst_weight = 0
    mst_edges = 0
    parent = [i for i in range(v+1)]
    rank = [0 for _ in range(v+1)]

    edges.sort()

    for weight, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank,a,b)
            mst_weight += weight
            mst_edges += 1

            if mst_edges == v-1:
                break
    if mst_edges <v-1:
        mst_weight =-1
    return mst_weight

print(kruskal(n_comp, input_edges))