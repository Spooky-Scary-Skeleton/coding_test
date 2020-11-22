#---------------
#[내풀이] 못풀음
#---------------

#---------------
#[내풀이] 1122 못풀음
#---------------


from collections import deque

#선수과목 시간 계산
def pre_time(indegree, x):
  if indegree[x] != 0:

n = int(input())


#선수과목 갯수 
indegree = [0] * (n+1)

#과목정보 담는 리스트 
subject = [0] * (n+1)

#각 과목당 수강에 걸리는 시간리스트 
course_time = [0] * (n+1)



#과목정보 담기
for i in range(1, n+1):
  a = list(map(int, input().split()))
  indegree[i] = len(a)-2
  a.pop()
  subject[i] = a

#과목수강에 걸리는 시간 담기
k = 1
for i in subject[1:]: 
  course_time[k] = i[0]
  k += 1
  

print(indegree)
print(subject)
print(course_time)

#---------------
#[교제풀이] 
#---------------
from collections import deque
import copy

#노드의 개수 입력받기
v = int(input())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
#각 강의 시간 0으로 초기화
time = [0] * (v+1)

#방향 그래프의 모든 간선정보를 입력받기
for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] #첫번쨰 수는 시간 정보
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

#위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time) #알고리즘 수행결과를 담을 리스트
  q = deque()

  #처음 시작할때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  #큐가 빌때까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    #해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      #새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  #위상정렬 수행결과 출력
  for i in range(1, v+1):
    print(result[i])


topology_sort()
#---------------
#[내가 부족한점] 
#---------------
copy에 대한 설명
https://www.programiz.com/python-programming/methods/list/copy
https://docs.python.org/3/library/copy.html
https://www.geeksforgeeks.org/id-function-python/

result 테이블과 time 테이블을 따로두는데는 이유가 있다. 
아직까지 잘 이해가 안된다 반복이 많이 필요.

#---------------
#[내가 부족한점] 1122
#---------------

이제 그나마 약간 이해가 되는것 같다. 
여전히 풀지는 못했음. 



