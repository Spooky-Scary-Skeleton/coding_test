#-----------------
#[내방법] 다익스트라 아직 손에 익질 않아서 책보면서 따라함
#-----------------

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#도시갯수, 통로갯수, 시작도시 입력
n, m, c = map(int, input().split())
#각 도시 통로정보 리스트
graph = [[] for i in range(n+1)]
#최단거리 테이블 모두 무한으로 초기화 
distance = [INF] * (n+1)

#통로정보 입력
for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(c):
  q = []
  #시작도시로가는 경로는 0으로 큐에 삽입
  heapq.heappush(q, (0, c))
  distance[c] = 0
  while q:
    #최단거리 도시 정보 꺼내기
    dist, now = heapq.heappop(q)
    #현재 도시가 이미 처리된 적이 있다면 무시
    if distance[now] <dist:
      continue
    #현재 도시와 연결된 다른 도시 확인
    for i in graph[c]:
      cost = dist + i[1]
      #현재 도시를 거쳐서, 다른 도시로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#다익스트라 실행
dijkstra(c)

k = 0
j = 0 

print(distance)

#못가는 도시 제외
for i in range(n+1):
  if distance[i] == INF:
    distance[i] = -1
print(distance)

#갈수있는 도시갯수
for i in range(1, n+1):
  if distance[i] != -1 and distance[i] != 0:
    k += 1

#가장 거리가 먼 도시
j = max(distance)

print(k, j)

#-----------------
#[교재방법] 다익스트라 아직 손에 익질 않아서 책보면서 따라함
#-----------------

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#도시갯수, 통로갯수, 시작도시 입력
n, m, c = map(int, input().split())
#각 도시 통로정보 리스트
graph = [[] for i in range(n+1)]
#최단거리 테이블 모두 무한으로 초기화 
distance = [INF] * (n+1)

#통로정보 입력
for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(c):
  q = []
  #시작도시로가는 경로는 0으로 큐에 삽입
  heapq.heappush(q, (0, c))
  distance[c] = 0
  while q:
    #최단거리 도시 정보 꺼내기
    dist, now = heapq.heappop(q)
    #현재 도시가 이미 처리된 적이 있다면 무시
    if distance[now] <dist:
      continue
    #현재 도시와 연결된 다른 도시 확인
    for i in graph[c]:
      cost = dist + i[1]
      #현재 도시를 거쳐서, 다른 도시로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#다익스트라 실행
dijkstra(c)

#도달 가능도시의 수
count = 0
#도달 가능 도시중 가장 멀리있는 도시와의 최단 거라
max_distance = 0
for d in distance:
  #도달 가능 도시의 경우
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

#시작도시 제외하니까 count-1
print(count - 1, max_distance)


#-----------------
#[부족한점]
#-----------------
"""
다익스트라가 손에 익을때까지 연습이 필요하다. 
"""

#-----------------
#[부족한점] 1118
#-----------------
"""
이제 다익스트라를 책을 보지않고 구현할수 있게 된것같다. 그래도 아직은 어려워서 시간이 좀 걸린다. 
많이 반복해서 더빠르게 구현 할수 있도록 하자. 
"""


#-----------------
#[부족한점] 210321
#-----------------
"""
다익스트라를 오랫만에보니 전혀 구현을 못했다. 
"""
