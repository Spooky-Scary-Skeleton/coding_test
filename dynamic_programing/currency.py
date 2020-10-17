#------------------
#[내풀이] 못풀음
#------------------

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
  
 
