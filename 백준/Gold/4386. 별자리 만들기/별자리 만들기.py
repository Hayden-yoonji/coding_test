import math 
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
    rank = [0 for r in range(v+1)]

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


n = int(input())

star_edges = []   #별의 위치 좌표
add_weight_star = []    #가중치가 포함된 버전

for _ in range(n):
    a, b = map(float, input().split())
    star_edges.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        dist = math.sqrt((star_edges[i][0] - star_edges[j][0])**2 + (star_edges[i][1] - star_edges[j][1])**2)
        add_weight_star.append((dist, i + 1, j + 1))
        
print(round(kruskal(n, add_weight_star),2))