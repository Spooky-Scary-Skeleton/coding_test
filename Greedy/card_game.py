# #교재 98
# ----------------------------------
# #[내 풀이] 
# ----------------------------------

#배열 초기화
n, m = map(int, input().split())
array = [[0 for i in range(m)] for i in range(n)]

#입력된 카드로 배열 바꾸기
for i in range(n):
  array[i] = list(map(int, input().split()))



minnum = []

#각 원소 리스트의 최소값 비교
for i in range(n):
  minnum.append(min(array[i]))

print(max(minnum))

# ----------------------------------
# #[내 풀이] 210310
# ----------------------------------

n, m = map(int, input().split(' '))

arr = [list(map(int, input().split(' '))) for i in range(n)]

max_num = 0

for i in range(n):
  row_min = min(arr[i])
  if row_min > max_num:
    max_num = row_min

print(max_num)


# ----------------------------------
# #[교재풀이1]
# ----------------------------------

#배열 초기화
n, m = map(int, input().split())

result = 0
#한줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  #현재줄에서 가장 작은 수 찾기
  min_value = min(data)
  #가장 작은 수 들 중에서 가장 큰수 찾기
  result = max(result, min_value)

print(result) 

# ----------------------------------
# #[교재풀이2]
# ----------------------------------
# #배열 초기화
n, m = map(int, input().split())

result = 0
#한줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  #현재줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  #가장 작은 수 들 중에서 가장 큰수 찾기
  result = max(result, min_value)

print(result) 

# ----------------------------------
# #[내가 부족한점]
# ----------------------------------
"""
굳이 기본 이차원 배열을 설정할 필요는 없음.
단순하게 각 행을 리스트로 읽어 들이고 최소값 취합후 최대값으로 비교하면 됨.
교재 풀이대로 하면 최소값을 따로 저장해두는 리스트를 만들지 않아도 풀수 있음
"""

# ----------------------------------
# #[내가 부족한점] 201103
# ----------------------------------
"""
이번에도 2차원 배열로 입력을 받아들이려함. 
이번 문제에서 굳이 2차원 배열로 입력을 받을 필요는 없음. 
"""

# ----------------------------------
# #[내가 부족한점] 210310
# ----------------------------------
"""
여전히 2차원 배열로 받아들이려고 하는데 굳이 그럴 필요가 없는 문제임
"""

