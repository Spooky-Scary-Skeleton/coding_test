#교재 114
----------------------------------
#[내 풀이] 못풀엇음
----------------------------------
n = int(input())

passed = [0, 0, 0]
count = 0

if n != 0:
  for i in range(1, n+1):
    passed[0] += 1
    for j in range(0, 60):
      passed[1] += 1
      if passed[1] == 60:
          passed[0] += 1
          passed[1] = 0          
      for k in range(0,60):
        passed[2] += 1
        if passed[2] == 60:
            passed[1] += 1
            passed[2] = 0
          
        print(passed, end=" ")
        if "3" in str(passed[2]):
          count += 1
        elif "3" in str(passed[1]):
          count += 1
        elif "3" in str(passed[0]):
          count += 1
     

else:
  print(15*60, end=" ")
----------------------------------
#[교재풀이]
----------------------------------
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      #매시각 안에 3이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) +str(k):
        count += 1

print(count)
----------------------------------
#[내가 부족한점]
----------------------------------
반복문의 i,j,k도 써먹을수 있다는 점을 못떠올림. 
