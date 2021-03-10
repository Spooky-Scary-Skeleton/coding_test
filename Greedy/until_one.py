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

# ----------------------------------
# #[내 풀이] 210310
# ----------------------------------

n, k = map(int, input().split(' '))

count = 0

while n > 1:  
  if n % k == 0:
    n /= k
    count += 1
  else:
    n -= 1
    count += 1

print(count)

# ----------------------------------
#교재 풀이 
#아직 102페이지 교재풀이 이해안됨 (1103)
# ----------------------------------

n, k = map(int, input().split())

result = 0

while True:
  # n이 k로 나누어질수 있도록 한번에 빼버리기
  target = (n // k) * k
  result += (n-target)

  #뺄샘후 숫자.
  n = target

  #뺄샘후 n이 k보다 작다면 탈출
  if(n < k):
    break
  #k로 나누어진다면 나누기
  n = n // k
  result += 1

#남은수는 뺄샘만 하면 된다.
result += (n - 1)

print(result)


# ----------------------------------
# #[내가 부족한점]
# ----------------------------------

"""
똑같은 발상에 똑같은 접근법으로 풀었다. 
교재102페이지의 풀이가 이제는 이해가 어느정도 가는데 아니 저런 생각을 대체 어떻게 하는건지 참 신기하다. 
"""
