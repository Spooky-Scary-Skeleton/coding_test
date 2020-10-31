import math

n = 1000 #2부터 1000까지의 모든 수에대해 소수판별
array = [True for i in range(n+1)] #처음에는 모두가 소수로 초기화(0, 1 제외)

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1): #2부터 n의 제곱근까지의 모든 수를 확인하며 
  if array[i] == True: #i가 소수인경우(남은 수인 경우)
    #i를 제외한 i의 모든 배수를 지우기
    j = 2
    while i*j <= n:
      array[i*j] = False
      j += 1

#모든 소수 출력 
for i in range(2, n+1):
  if array[i]:
    print(i, end=' ')
    
