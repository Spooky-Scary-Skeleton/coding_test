#------------------
#[내풀이] (자기자신으로 가는 번호를 0으로 가는 과정을 빼먹음)
#------------------

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

for i in range(n+1):
  for j in range(n+1):
    for l in range(n+1):
      graph[j][l] = min(graph[j][l], graph[j][i] + graph[i][l])


if graph[1][k] == INF or graph[k][x] == INF:
  print(-1)
else:
  print(graph[1][k] + graph[k][x])
  
  
#------------------
#[교재풀이] 
#------------------

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
  for b in range(n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

for i in range(n+1):
  for j in range(n+1):
    for l in range(n+1):
      graph[j][l] = min(graph[j][l], graph[j][i] + graph[i][l])


if graph[1][k] == INF or graph[k][x] == INF:
  print(-1)
else:
  print(graph[1][k] + graph[k][x])
  
#------------------
#[부족한점] 
#------------------

자기자신으로 가는 번호를 0으로 가는 과정을 빼먹음
  
