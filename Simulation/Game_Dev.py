#교재 118
----------------------------------
#[내 풀이] (반복문이 무한이 돌아가서 틀림)
----------------------------------
n, m = map(int, input().split())
x, y, d = map(int, input().split())

arr = []

for i in range(n):
  arr.append(list(map(int, input().split())))



#시작점 1로 만들기
arr[x][y] = 1

#결과값
count = 0

while True:
  print(1)
  #앞으로 가능 경우
  #북쪽볼때
  if d == 0:  
    if arr[x][y-1] != 1:
      arr[x][y-1] = 1
      count += 1
      x, y = x, y-1
      d = 3
    else:
      d = 3

  #서쪽볼때
  if d == 3: 
    if arr[x+1][y] != 1:
      arr[x+1][y] = 1
      count += 1
      x, y = x+1, y
      d = 2
    else:
      d = 2

  #남쪽볼때
  if d == 2: 
    if arr[x][y+1] != 1:
      arr[x][y+1] = 1
      count += 1
      x, y = x, y+1
      d = 1
    else:
      d = 1

  #동쪽볼때
  if d == 1: 
    if arr[x-1][y] != 1:
      arr[x-1][y] = 1
      count += 1
      x, y = x-1, y
      d = 0
    else:
      d = 0

  # 다막혔고 뒤로갈때 
  if arr[x][y-1] == 1  and arr[x+1][y] == 1 and arr[x][y+1] == 1 and arr[x-1][y] != 1:
    break

print(count)

----------------------------------
#[교재풀이]
----------------------------------
#N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

#방문한 위치를 저장하기위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
#현재 캐릭터의 X좌표 Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

#전체 맵 정보를 입력받기 
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

#북, 동, 남, 서 방향 정의 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0 
    continue
  #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  #네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    #뒤로 갈 수 있다면 이동하기 
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

#정답 출력
print(count)


arr = []

for i in range(n):
  arr.append(list(map(int, input().split())))



#시작점 1로 만들기
arr[x][y] = 1

#결과값
count = 0

while True:
  #앞으로 가능 경우
  #북쪽볼때
  if d == 0:  
    if arr[x][y-1] != 1:
      arr[x][y-1] = 1
      count += 1
      x, y = x, y-1
      d = 3
    else:
      d = 3

  #서쪽볼때
  if d == 3: 
    if arr[x+1][y] != 1:
      arr[x+1][y] = 1
      count += 1
      x, y = x+1, y
      d = 2
    else:
      d = 2

  #남쪽볼때
  if d == 2: 
    if arr[x][y+1] != 1:
      arr[x][y+1] = 1
      count += 1
      x, y = x, y+1
      d = 1
    else:
      d = 1

  #동쪽볼때
  if d == 1: 
    if arr[x-1][y] != 1:
      arr[x-1][y] = 1
      count += 1
      x, y = x-1, y
      d = 0
    else:
      d = 0

  # 다막혔고 뒤로갈때 
  if arr[x][y-1] == 1  and arr[x+1][y] == 1 and arr[x][y+1] == 1 and arr[x-1][y] != 1:
    break

print(count)

----------------------------------
#[내가 부족한점]
----------------------------------
1. 지나갔던 경로랑 전체 맵 경로를 따로 저장해서 활용하면 쉬웠음
2. dx, dy리스트를 이용해서 풀면 쉬웠음
3. 왼쪽으로 회전하는 함수를 따로 만드는것을 생각을 못함
4. 4번돌아도 갈곳이 없는거 설계(turn_time +=1)가 이렇게 가능한지 생각을 못함 




