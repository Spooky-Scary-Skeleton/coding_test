#교재 312
----------------------------------
#[내 풀이]
----------------------------------
array = list(map(int, input()))

result = 0

i = 0

if array[i] + array[i+1] < array[i] * array[i+1]:
  result = array[i] * array[i+1]
else:
  result = array[i] + array[i+1]

for k in range(2, len(array)):
  if result + array[k] < result * array[k]:
    result = result * array[k]
  else:
    result = result + array[k]


print(result)
----------------------------------
#[교재풀이]
----------------------------------
data = input()

#첫문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  #두개의 숫자중 하나라도 0,1이면 덧셈 실행
  num = int(data[i])
  if result <= 1 or num <= 1:
    result += num
  else:
    result *= num

print(result)

----------------------------------
#[내가 부족한점]
----------------------------------
1. 첫번째 변수를 더 간단하게 처리 할 생각을 못함
2. 0, 1 이 아니면 곱하는게 무조건 크다는 방식으로 생각을 못함. 

