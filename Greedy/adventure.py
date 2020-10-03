#교재 311
----------------------------------
#[내 풀이] 못풀엇음
----------------------------------
n = int(input())
a = list(map(int, input().split()))


people_left = n
coward = max(a)
count = 0 


#가장 겁쟁이 기준 그룹 1개 생성
for i in range(people_left):
  a.remove(coward)
  coward = max(a)
  people_left -= 1
count += 1




print(count)

----------------------------------
#[교재풀이]
----------------------------------
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모헙가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인하며
  count += 1 #현재 그룹에 해당 모험가를 포함 시키기
  if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
    result += 1 # 총 그룹의 수 증가 시키기
    count = 0 #현재 그룹에 포함된 모험가의 수 초기화 

print(result) #총 그룹의 수 출력

----------------------------------
#[내가 부족한점]
----------------------------------
오름차순으로 정렬한후 팀을 맺어가기 시작하면 된다는 걸 생각을 못함. 
