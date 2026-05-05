from collections import deque

def solution(maps):
    return bfs(maps,[0,0,1])
    
def bfs(maps, start):
    n,m = len(maps), len(maps[0])
    q = deque([start])
    visited = [[False] * m for i in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x,y, dist=q.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if visited[nx][ny] == False:
                    q.append((nx,ny,dist +1))
                    visited[nx][ny] = True
                    
                    
    return -1

                
    