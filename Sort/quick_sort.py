array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 한개인 경우 종료
    return
  pivot = start #피벗은 첫번째 원소
  left = start +1
  right = end
  while left <=right:
    #피벗보다 큰 데이터를 찾을떄 까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    #피벗보다 작은 데이터를 찾을때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: #엇갈리지 않았다면 작은데이터와 큰 데이터를 교체 
      array[left], array[right] = array[right], array[left]
  #분할이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#방법 2 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] #피벗은 첫번째 원소
  tail = array[1:] #피벗을 제외한 리스트

  left_side = [x for x in tail if x<= pivot] #분할된 왼쪽 부분
  right_side = [x for x in tail if x >pivot] #분할된 오른쪽 부분

  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반황
  return quick_sort(left_side) + [pivot] +quick_sort(right_side)
print(quick_sort(array))


-------------
[개인의견]
-------------
사실 이해가 안간다. 재귀적으로 실행할때 만약 피벗보다 작은/큰 수가 존재 하지 않는경우라던지에대한 설명이 책에 없다. 
일단은 방법 2를 외워서 쓰도록 해보자. 


-------------
[개인의견] 1112
-------------
이번에도 이해가 잘 안간다. 
2번이 역시 가장 쉽고 이해가 
