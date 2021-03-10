#교재 92
# ----------------------------------
#[내 풀이]
# ----------------------------------

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse = True)

result = 0
a = 0

for i in range(m):
  if a != k:
    result += array[0]
    a += 1
  else:
    result +=array[1]
    a = 0

print(result)

# ----------------------------------
#[내 풀이] 0310
# ----------------------------------

n, m, k = map(int, input().split(' '))

li = list(map(int, input().split(' ')))

li.sort(reverse = True)


num_set = (li[0] * k) + li[1]

if m == k:
  print(li[0] * k)
else:
  mul = m // (k + 1)
  rest = m % (k + 1)
  print((num_set * mul) + (rest * li[0]))

# ----------------------------------
# [교재풀이1]
# ----------------------------------

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

#숫자 정렬
data.sort(reverse = True)
#가장 큰수
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k): #가장큰수 k번 더하기
    if m == 0: #m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 #더할때 미디 1씩 빼기
  if m == 0: #m이 0이라면 반복문 탈출
    break
  result += second#두번째로 큰수 한번 더하기
  m -= 1
  
print(result)

# ----------------------------------
# [교재풀이2]
# ----------------------------------

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

#숫자 정렬
data.sort(reverse = True)
#가장 큰수
first = data[n-1]
second = data[n-2]

#가장 큰수가 더해지는 횟수
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first #가장 큰수 횟수만큼 더하기
result += (m-count) * second #나머지횟수만큰 두번쨰 큰수 더하기
  
print(result)

# ----------------------------------
# [내가 부족한점]
# ----------------------------------
"""
2중 반복문 내부에서 break사용시 해당 반복문에서만 탈출 
약간의 수학적 사고로 시간을 크게  줄일수있다
"""
# ----------------------------------
# [내가 부족한점] 11-02
# ----------------------------------
"""
처음 풀때랑 거의 다름없이 품.
반복되는 수열을과 그 수열의 길이를 떠올려서 더 쉽게 풀수 있었다. 
"""
# ----------------------------------
# [내가 부족한점] 03-10
# ----------------------------------
"""
반복되는 수열을 찾아서 풀었지만 시간이 너무 오래걸렸다. 그리고 일일히 찾는 방법으로의 구현은 오히려 구현을 못했다. 
"""

