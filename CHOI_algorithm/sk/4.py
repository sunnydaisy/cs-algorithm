import heapq

def bfs(grid, k):
    result = 0
    n = len(grid)
    m = len(grid[0])
    INF = int(1e9)
    visited = [[INF] * m for _ in range(n)]
    q = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    heapq.heappush(q, [0, k, 0, 0])
    while q:
        cost, m_left, nx, ny  = heapq.heappop(q)
        if nx == n - 1 and ny == m - 1:
            return cost
        for i in range(4):
            tx = dx[i] + nx
            ty = dy[i] + ny
            if tx < 0 or ty < 0 or tx >= n or ty >= m or m_left <= 0 or (visited[tx][ty] < cost and m_left != k):
                continue
            
            heapq.heappush(q, [cost, m_left - 1, tx, ty])
            if grid[tx][ty] == '.':
                heapq.heappush(q, [cost + 1, k, tx, ty])
                visited[nx][ny] = cost
        
            

        

def solution(grid, k):
    answer = bfs(grid, k)
    return answer

grid = ["..FF", "###F", "###."]
solution(grid, 4)
# solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)