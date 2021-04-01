# ------------------------------------------
# #[내가한풀이] 아마도 시간초과로 탈락했을듯
# ------------------------------------------
n, m = map(int, input().split())
rc = sorted(list(map(int, input().split())))

def cut(n,array, longest, target):
  cutted = [0] * n

  while True:
    for i in range(n):
      if array[i] - longest < 0:
        cutted[i] = 0
      else:
        cutted[i] = array[i] - longest
    if sum(cutted) == target:
      break
    elif sum(cutted) < target:
      longest -= 1

  return longest


print(cut(n, rc, rc[n-1], m))

# ------------------------------------------
# #[내가한풀이] 1114 못품, 일단 시간 복잡도 측면에서 일일히 칼길이를 1씩 줄여 나가는것은 무의미 
# ------------------------------------------

# ------------------------------------------
# #[내가한풀이] 210314 틀림. 이진탐색으로 구현해보려했으니 자꾸 무한 반복이 되어버림. 
# ------------------------------------------

n, m = map(int, input().split())
height = list(map(int, input().split()))

#떡 최대 최소길이
min_height = min(height)
max_height = max(height)


#이진탐색실행
start = 1
end = max_height - 1
mid =  (start + end) // 2

while start < end:  
  #잘라낸 떡길이의 총합.
  sum_height = 0

  for i in height:
    cut = i - mid
    if cut > 0:
      sum_height += cut

  if sum_height == m:
    break
  if sum_height < m:
    end = mid - 1
  if sum_height > m:
    start = mid + 1

print(mid)


# ------------------------------------------
# #[내가한풀이] 210401 틀림. 드디어 풀었다. 
# ------------------------------------------

#57
n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

#이진탐색

def binary_search(array, target, start, end):
  h = (start + end) // 2

  if start > end:
    return h

  sum_of_cut = 0

  for i in range(n):
    if rice_cake[i] - h > 0:
      sum_of_cut += rice_cake[i] - h

  #떡길이가 딱 맞을 경우 해당 높이 이상으로 못올림
  if sum_of_cut == m:
    return h #따라서 현재 높이 반환
  #떡 길이가 더 적은경우 칼날 높이를 낮춰서 더 잘라줘야함. 
  elif sum_of_cut < m:
    return binary_search(array, target, start, h - 1)
  #떡 길이가 더 많을 경우 칼을 높여 봐야함. 
  elif sum_of_cut > m:
    return binary_search(array, target, h + 1, end)
  
    

print(binary_search(rice_cake, m, 0, max(rice_cake)))

# ------------------------------------------
# #교재풀이
# ------------------------------------------
#떡 갯수와 요청항 떡길이 받기
n, m = map(int, input().split())

#각 떡의 개별 높이 정보 입력
array = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진탐색 수행
result = 0
while(start <= end):
  mid = (start + end) // 2
  total = 0
  for x in array:
    #잘랐을 떄의 떡의양 계산
    if x > mid:
      total += x - mid
  #떡의 양이 부족한 경우 더 많이 자르기(왼쪽부분탐색)
  if total < m:
    end = mid - 1
  #떡이 충분할 경우 덜자르기(오른쪽탐색)
  else:
    result = mid #최대한 덜 잘랐을떄가 정답이니까 여기서 result에 기록
    start = mid+1

print(result)
------------------------------------------
#내가 부족한점
------------------------------------------
"""
시간 복잡도를 고려하지않고 코드를 구성함. 
이진 탐색이 적용가능하다고 발상을 못떠올림
"""
------------------------------------------
#내가 부족한점 1114
------------------------------------------
"""
이진 탐색이 적용 가능하다고 생각은 했으나 구현을 못함
재귀적으로만 이진 탐색을 구현을 하려다 보니 문제를 못풀었음. 
"""
------------------------------------------
#내가 부족한점 210314
------------------------------------------
"""
핵심 아이디어는 어느정도 떠올렸는데 구현에서 잘 못했다. 또한
떡을 최대한 덜 잘라야하는데 최대한 덜 잘랐을때의 칼 길이를 어떻게 기록해둘지 떠올리지 못함
"""

------------------------------------------
#내가 부족한점 210401
------------------------------------------
"""
드디어 풀었다. 나는 제귀적으로 구현했는데 이건 교재에 나온대로 반복문으로 구현하는게 더 간결 햇을거 같다. 
"""


