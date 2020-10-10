----------------------------------
#[내 풀이] 못품
----------------------------------


----------------------------------
#[교재풀이]
----------------------------------
n, m = map(int, input().split())

#2차원 리스트의 맵정보 입력받기
graph =[]
for i in range(n):
  graph.append(list(map(int,input())))

#DFS로 특정한 노드를 방문한뒤에 연결된 모든 노드들도 방문

def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<= -1 or x >= n or y <= -1 or y >= m:
    return False
  #현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1
    #상하좌우의 위치도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)

----------------------------------
#[내가 부족한점]
----------------------------------
아직 DFS의 개념이 익숙하지가 않다. 
문자열(STR)도 iterable이라는 것을 생각을 못했음. 
