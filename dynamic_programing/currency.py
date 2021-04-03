#------------------
#[내풀이] 못풀음
#------------------

#------------------
#[내풀이] 210316 못풀음
#------------------

#------------------
#[내풀이] 210403 어떻게 풀어내긴했음. 그러나 교재보다 지저분함. 
#------------------

#입력받기
n, m = map(int, input().split())
coin = []
for i in range(n):
  coin.append(int(input()))

#불가능한 조합은 무한으로 표현
max_num = int(1e9)

#화폐별 조합가능 최소의 수
combination = [max_num] * (m + 1)

#특정동전 1종류만 썻을때의 최소조합의 수
for i in coin:
  k = 1
  while i * k <= m:
    combination[i * k] = min(k, combination[i * k]) 
    k += 1

#동전끼리 조합해서 만들었을때 최소조합의 수
for i in range(1, m + 1):
  for j in coin:
    if i - j > 0 and combination[i-j] != max_num:
      combination[i] = min(combination[i-j] + 1, combination[i])

print(combination)


if combination[m] != max_num:
  print(combination[m])
else:
  print(-1)



#------------------
#[교재풀이] 사실 아직도 이런 발상을 어떻게 다이나믹이랑 연관지어서 떠올리는 건지 이해가 안됨. 
#------------------

n, m = map(int, input().split())

#n개의 화폐단위 정보를 입력 받기
array = []
for i in range(n):
  array.append(int(input()))

#한번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)

#다이나믹진행(보텀업) 

d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] != 10001: #(i-k)원을 만드는 방법이 존재할 경우
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
  
  
  
  
  
#------------------
#[부족한점] 210316
#------------------
"""
저런 발상을 대체 어떻게 하는건지 잘 이해가 안됨....
그리고 풀이내용을 봐도 아직 잘 이해가 안간다 ㅜㅜ;;;;
"""
  
#------------------
#[부족한점] 210403
#------------------
"""
풀어내긴 했지만 시간이 너무 오래걸렸고 교재보다는 더 지저분하다
"""

