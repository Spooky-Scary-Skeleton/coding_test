#교재 112
----------------------------------
#[내 풀이]
----------------------------------
n = int(input())
direction = input().split()

current = [1, 1]

for i in direction:
  if i == "L" and current[1] != 1:
    current[1] = current[1] - 1
  if i == "R" and current[1] != n:
    current[1] = current[1] + 1
  if i == "U" and current[0] != 1:
    current[0] = current[0] - 1
  if i == "D" and current[0] != n:
    current[0] = current[0] + 1

print(current)

----------------------------------
#[교재풀이]
----------------------------------

n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "u", "D"]

#이동 계획을 하나씩 확인하기
for plan in plans:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  #공간을 벗어나는 경우 무시
  if nx < 1 or ny <1 or nx > n or ny > n:
    continue
  #이동수행
  x, y = nx, ny

print(x, y)

----------------------------------
#[내가 부족한점]
----------------------------------
나는 단순 반복문을 여러번 써서 햇는데 교재대로 하면 조금더 구조화되어있고 사후 관리도 쉬울거 같다. 

----------------------------------
#[내가 부족한점]
----------------------------------
일단 너무 처음 풀이와 비슷하게 풀었고 리스트의 인덱스가는 실제 위치에서 -1로 생각해야 한다는 것도 까먹음
그나마 dx, dy 리스트를 따로 둘 생각은 했었음.

