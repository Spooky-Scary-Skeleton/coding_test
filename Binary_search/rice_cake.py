------------------------------------------
#[내가한풀이] 아마도 시간초과로 탈락했을듯
------------------------------------------
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

------------------------------------------
#[내가한풀이] 1114 못품, 일단 시간 복잡도 측면에서 일일히 칼길이를 1씩 줄여 나가는것은 무의미 
------------------------------------------


------------------------------------------
#교재풀이
------------------------------------------
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
시간 복잡도를 고려하지않고 코드를 구성함. 
이진 탐색이 적용가능하다고 발상을 못떠올림

------------------------------------------
#내가 부족한점 1114
------------------------------------------
이진 탐색이 적용 가능하다고 생각은 했으나 구현을 못함
재귀적으로만 이진 탐색을 구현을 하려다 보니 문제를 못풀었음. 




