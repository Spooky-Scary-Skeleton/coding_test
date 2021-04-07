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
#[내풀이] 1118 자기자신으로 가는번호를 0으로 초기화 하는것은 내가푸는방법이 더 좋은거같음
#------------------
  
#무한 설정
INF = int(1e9)
#회사갯수, 간선갯수 입력받기
n, m = map(int, input().split())

#그래프정보 저장 리스트
graph = [[INF] * (n + 1) for i in range(n + 1)]

#자기자신으로가는 거리 0으로 초기화
for i in range(n + 1):
  graph[i][i] = 0

#그래프 정보 입력받기
for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

#방문할 회사입력받기
x, k = map(int, input().split())

#플로이드 워셜 알고리즘 실행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#결과 출력
result = graph[1][k] + graph[k][x]

if result >= INF:
  print(-1)
else:
  print(result) 


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
"""
자기자신으로 가는 번호를 0으로 가는 과정을 빼먹음
"""

#------------------
#[부족한점] 1118
#------------------
"""
깃허브와서 그때 풀었었는지 확인했는데 그거 보는게 오히려 힌트가 되서 쉽게 푼거 같음. 
"""
#------------------
#[부족한점] 210321
#------------------
"""
플로이드워셜은 확실히 동작방법만 알면 별다른 문제가 없다.
다익스트라가 너무 어려워서 문제지
"""

"""
문제입력

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5


4 2
1 3
2 4
3 4
"""
