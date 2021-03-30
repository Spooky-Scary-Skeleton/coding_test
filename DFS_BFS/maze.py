# #교재 152
# ----------------------------------
# #[내 풀이] 못풀었음
# ----------------------------------

# ----------------------------------
# #[내 풀이] 못풀었음 1111
# ----------------------------------

# ----------------------------------
# #[내 풀이] 못풀었음 210312
# ----------------------------------

# ----------------------------------
# #[내 풀이] 드디어 풀었음 210330
# ----------------------------------
from collections import deque

n, m = map(int, input().split())

#미로입력
maze = []
for i in range(n):
  maze.append(list(map(int, input())))

#0,0 부터 시작한다고 생각

#상하좌우 움직임
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


#bFS
def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m and maze[nx][ny] == 1:
        maze[nx][ny] += maze[x][y]
        q.append((nx, ny))

bfs(0, 0)

print(maze[n-1][m-1])


# ----------------------------------
# #[교재풀이]
# ----------------------------------

from collections import deque

n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#이동할 네방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1,]

#BFS 구현
def bfs(x, y):
  #deque라이브러리 사용
  queue = deque()
  queue.append((x,y))
  #큐가 빌때 까지 반복
  while queue:    
    x, y = queue.popleft()
    #현재위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      #벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  #가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

#BFS를 수행한 결과 출력
print(bfs(0, 0))

# ----------------------------------
# #[내가 부족한점]
# ----------------------------------
"""
아직도 솔직히 이게 왜 BFS랑 관련있는지 잘 이해가 안됨. 
그냥 상하좌우 다 움직여봐서 계속 갈수있는 곳으로 거리를 더해가면서 가는건데.....
"""


# ----------------------------------
# #[내가 부족한점] 
# ----------------------------------
"""
이제는 BFS랑 관련 있는것이 어느정도 이해가 됨. 
그러나 문제는 이번에도 핵심 아이디어는 못떠올림. 
"""

# ----------------------------------
# #[내가 부족한점] 210312
# ----------------------------------
"""
BFS랑 관련이 있다는건 어느정도 느낌이 오는데 
여전히 이런 풀이를 어떻게 떠올리는건지 신기하다 나는 고민해도 생각을 못떠올렸는데.....
"""
"""
문제 입력
5 6
101010
111111
000001
111111
111111
"""
