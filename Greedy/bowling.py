#교재 315
----------------------------------
#[내 풀이]
----------------------------------
n, m = map(int, input().split())
k = list(map(int, input().split()))

k.sort()
a = 0
count = 0

for i in k:
  a += 1
  if a == n:
    break

  for j in range(a, n):
    if i != k[j]:
      count += 1

print(count)
----------------------------------
#[교재풀이]
----------------------------------
n, m = map(int, input().split())
k = list(map(int, input().split()))

#각 무게별 빈 공간 준비
a = [0] * 11 

#각 무게별 볼링공 갯수 리스트 
for i in k:
  a[i] += 1

result = 0

#조합 구하기
for j in range(1, m+1):
  n -= a[j] #무게가 i인 볼링공의 개수 제외
  result += n*a[j] #B가 선택하는 경우의 수와 곱하기

print(result)
----------------------------------
#[내가 부족한점]
----------------------------------
볼링공 리스트를 설정해서 무게별로 선별해놓는 사고
작은 것부터 순서대로 조합을 구해나가면 중복되는건 자동으로 제외되는 
