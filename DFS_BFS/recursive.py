#기본예시
 
def recursive_function(i):
  #100번째 출력했을 때 종료되도록 총료 조건 명시
  if i == 100:
    return
  print(i, '번째 재귀 함수에서', i+1, '번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i, "번째 재귀 함수를 종료합니다.")

recursive_function(1)
-------------------------------
#팩토리얼예시

#반복적으로 구현
def factorial_iterative(n):
  result = 1
  #1부터 n까지의 수를 차례대로 곱하기 
  for i in range(1,n+1):
    result *= i
  return result

#재귀적으로 구현
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)
  
print('반복적으로 구현:', factorial_iterative(5))

print('재귀적으로 구현:', factorial_recursive(5))

