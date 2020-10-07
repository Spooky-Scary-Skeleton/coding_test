#교재 115
----------------------------------
#[내 풀이]
----------------------------------
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
나이트가 이동 완료한 위치 8개만 원위치에서 더하고 빼면 되는거였는데...그생각을 못했음 
그리고 ord함수를 이용해서 hex값으로 문자를 숫자로 변경하는 법도 있다는 것을 기억해두자. 
