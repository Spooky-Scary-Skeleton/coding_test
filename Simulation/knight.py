# #교재 115
# ----------------------------------
# #[내 풀이]
# ----------------------------------
a = input()
num = ['a','b','c','d','e','f','g','h']

x = int(a[1])
y = num.index(a[0]) + 1

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

count = 0

x += dx[0]
y += dy[0]
x += dx[0]
y += dy[0]
x += dx[2]
y += dy[2]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[0]
y += dy[0]
x += dx[0]
y += dy[0]
x += dx[3]
y += dy[3]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[1]
y += dy[1]
x += dx[1]
y += dy[1]
x += dx[2]
y += dy[2]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[1]
y += dy[1]
x += dx[1]
y += dy[1]
x += dx[3]
y += dy[3]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[2]
y += dy[2]
x += dx[2]
y += dy[2]
x += dx[0]
y += dy[0]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[2]
y += dy[2]
x += dx[2]
y += dy[2]
x += dx[1]
y += dy[1]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[3]
y += dy[3]
x += dx[3]
y += dy[3]
x += dx[0]
y += dy[0]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1

x += dx[3]
y += dy[3]
x += dx[3]
y += dy[3]
x += dx[1]
y += dy[1]

if x < 1 or y < 1 or x > 8 or y > 8:
  x, y = int(a[1]), num.index(a[0]) + 1
else:
  count += 1
  x, y = int(a[1]), num.index(a[0]) + 1



print(count)


# ----------------------------------
# #[내 풀이] 1105
# ----------------------------------
now = input()

#현재위치
dx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dy = range(8)

x = dx.index(now[0])
y = dy[int(now[1])-1]

#움직일수 있는 위치
dx1 = [2, 2, -2, -2, -1, 1, -1, 1]
dy1 = [-1, 1, -1, 1, 2, 2, -2, -2]

count = 0

for i in range(8):
  nx = x + dx1[i]
  ny = y + dy1[i]
  if nx < 0 or nx > 7 or ny < 0 or ny > 7:
    pass
  else:
    count += 1

print(count)


# ----------------------------------
# #[내 풀이] 210311
# ----------------------------------

n = input()

x, y = int(n[1]), ord(n[0]) - 96

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

count = 0

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
    count += 1

print(count)


----------------------------------
#[교재풀이]
----------------------------------
#현재 나이트의 위치 입력
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) +1


#나이트가 이동할수 있는 8가지 방법:
steps = [(-2,-1), (-2,1), (2,-1), (2,1),(-1,-2),(-1,2),(1,-2), (1,2)]

#8가지 방향에 대해 각위치로 이동이 가능한지 확인
next_row = 0
next_column = 0
count = 0 

for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row > 0 and next_column > 0 and next_row <= 8 and next_column <= 8:
    count += 1
    

print(count)
----------------------------------
#[내가 부족한점]
----------------------------------
"""
나이트가 이동 완료한 위치 8개만 원위치에서 더하고 빼면 되는거였는데...그생각을 못했음 
그리고 ord함수를 이용해서 hex값으로 문자를 숫자로 변경하는 법도 있다는 것을 기억해두자. 
"""
----------------------------------
#[내가 부족한점] 1105
----------------------------------
"""
핵심아이디어는(8개위치로만 움직일수 있다는 것) 잘 떠올림
튜플로 구현한 방식은 나랑 차이가 난다. 
"""
----------------------------------
#[내가 부족한점] 210311
----------------------------------
"""
이번에도 핵심아이디어는 잘떠올림(8개위치로 이동가능) 다만 구현방법에서ord()를 몰라서 시간이 오래걸렸고
이전장에서 배웠던 내용을 그대로 써먹음. 
"""
