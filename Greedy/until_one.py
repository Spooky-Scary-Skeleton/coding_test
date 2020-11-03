#내가 한 풀이

n, k = map(int, input().split())



count = 0

while n != 1:
  if n % k == 0:
    n = n / k
    count += 1
  else:
    n -= 1
    count += 1

print(count)

#교재 풀이 
#아직 102페이지 교재풀이 이해안됨 (1103)
