#-------------------------
#[내풀이] 못풀었음
#-------------------------

#-------------------------
#[내풀이] 1115 못풀었음
#-------------------------

#-------------------------
#[내풀이] 210316 드디어 한번 떠올려서 풀 수 있었다. 
#-------------------------

n = int(input())
storage = list(map(int, input().split()))

d = [0] * 101

#창고는 적어도 3개
#3개 이하일때 최댓값.
d[2] = max(storage[1], storage[0])
d[3] = max(storage[1], storage[0] + storage[2])


for i in range(3, n + 1):
  d[i] = max(d[i-1], d[i-2] + storage[i-1])


print(d[n])

#-------------------------
#[내풀이] 210403 이문제는 이제 확실히 감이 잡힌거 같다.  
#-------------------------

#입력받기
n = int(input())
k = list(map(int, input().split()))

#창고길이별 최대 약탈가능 갯수 기록
arr = [0] * 1000
arr[0] = k[0]
arr[1] = max(k[0], k[1])

for i in range(2, n):
  arr[i] = max(arr[i-1], k[i] + arr[i-2])


print(arr[n-1])


#-------------------------
#[교재풀이] 자신을 포함하고 더하는경우와 아닌경우만 생각하면됨
#-------------------------

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100 #창고길이별 최적의 해

d[1] = array[0]
d[2] = max(array[0], array[1])

for i in range(3, n+1):
  d[i] = max(d[i-1], d[i-2] + array[i-1])

print(d[n])

#-------------------------
#[부족한점]
#-------------------------
""""
최대값을 어떻게 간단하게 구현할 수 있는지 생각을 못했음. 

다이나믹으로 생각을 해서 풀수있다는 사실을 처음 알게됨. 

유튜브강의 35분경: https://www.youtube.com/watch?v=5Lu34WIx2Us&t=2652s
"""

#-------------------------
#[부족한점] 1115
#-------------------------
"""
다이나믹인건 알았는데 구현을 못함...
"""

