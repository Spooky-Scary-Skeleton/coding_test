#-----------------
#[내풀이]
#-----------------

#루트 노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#합연산
def union(parent,a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[a] = b
  else:
    parent[b] = a

#마을과 길갯수 입력
n, m = map(int, input().split())

#부모테이블
parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i

#길정보 담아두기 리스트
operation = []
#총 길의 유지비
total = []

#마을과 길정보 입력
for i in range(m):
  a, b, route = map(int, input().split())
  operation.append((route, a, b))

operation.sort()

#짧은 거리부터 연산 시행
for i in operation:
  if find_parent(parent, i[1]) != find_parent(parent, i[2]):
    union(parent, i[1], i[2])
    total.append(i[0])

total.pop()

print(sum(total))





#-----------------
#[교재풀이]
#-----------------
#루트 노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#합연산
def union(parent,a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[a] = b
  else:
    parent[b] = a

#마을과 길갯수 입력
n, m = map(int, input().split())

#부모테이블
parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i

#길정보 담아두기 리스트
edges = []
#총 길의 유지비
total = 0

#마을과 길정보 입력
for i in range(m):
  a, b, route = map(int, input().split())
  edges.append((route, a, b))

edges.sort()

#짧은 거리부터 연산 시행
for i in edges:
  cost, a, b = i
  if find_parent(parent, a) != find_parent(parent, b):
    union(parent, a, b)
    total += cost
    last = cost

print(total - last)

#-----------------
#[부족한점]
#-----------------
"""
발상 까지는 좋았다. 다만 길정보 담아두는 리스트를 edges라고 명칭하는게 좋을거 같고 
총길의 유지비도 굳이 max, pop쓸 필요 없이 맨 마지막에 추가된놈만 last 변수로 저장 해뒀다가 빼주면 됬음
"""

#-----------------
#[부족한점] 210323
#-----------------
"""
최댓값 간선을 구핼때 생각했어야하는거는 어차피 sort가 되어있는 상태기 떄문에 마지막에 더한 간선의 길이가 최대라는 점이다.
"""


