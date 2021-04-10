"""
예제입력

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""


#---------------
#[내풀이]
#---------------

#부모찾기
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#합집합 수행
def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


#학생정보,연산횟수 입력
n, m = map(int, input().split())

#부모 테이블 설정
parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i

operation = []
for i in range(m):
  operation.append(list(map(int, input().split())))

for i in operation:
  if i[0] == 0:
    union(parent, i[1], i[2])
  else:
    if find_parent(parent, i[1]) == find_parent(parent, i[2]):
      print("YES")
    else:
      print("NO")


#---------------
#[교재풀이]
#---------------

#부모찾기
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#합집합 수행
def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


#학생정보,연산횟수 입력
n, m = map(int, input().split())

#부모 테이블 설정
parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i


for i in range(m):
  oper, a, b = map(int, input().split())
  if oper == 0:
    union(parent, i[1], i[2])
  else:
    if find_parent(parent, i[1]) == find_parent(parent, i[2]):
      print("YES")
    else:
      print("NO")
      
#--------------------
#[부족한점]
#--------------------
"""
oper, a, b로 바로 받고 반복문을 돌릴수 있게 코드를 더 깔끔하게 작성 가능했음. 
"""

#--------------------
#[부족한점] 1122
#--------------------
"""
이번엔 제대로 
"""

#--------------------
#[부족한점] 210323
#--------------------
"""
이번에도 이론부분읽고 별 문제 없었다.  
"""

