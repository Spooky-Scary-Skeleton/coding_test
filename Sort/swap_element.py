# ----------------------------------
# #[내 풀이] (정확성 검사에서 틀릴수 있음)
# ----------------------------------
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
  a[i] = b[n-1-i]

print(sum(a))

# ----------------------------------
# #[내 풀이] 1114 이번에도 숫자 비교 검사 조건문을 안넣음
# ----------------------------------

#n,k 입력
n, k = map(int, input().split())

#저장소
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

#a 오름차순 정렬, b 내림차순 정렬
array_a.sort()
array_b.sort(reverse = True)

#원소바꾸기 실행
for i in range(k):
  if array_a[i] < array_b[i]:
    array_a[i] = array_b[i]
  else:
    break

#원소합 출력
print(sum(array_a))



# ----------------------------------
# #[내 풀이] 210313 이번에도 숫자 비교 검사 조건문을 안넣음
# ----------------------------------

n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
  a[i] = b[i]

print(sum(a))



# ----------------------------------
# #[교재풀이]
# ----------------------------------
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else: #A가 B보다 클때는 반복문 탈출
    break

print(sum(a))
# ----------------------------------
# #[내가 부족한점]
# ----------------------------------
"""
a와 b 비교해서 작을때만 스왑 실시하고 아닐때는 빠져 나오면 된다는 생각을 못함. 
"""

# ----------------------------------
# #[내가 부족한점] 1114
# ----------------------------------
"""
이번에도 숫자 비교 검사 조건문을 안넣음
"""

# ----------------------------------
# #[내가 부족한점] 210313
# ----------------------------------
"""
숫자 비교 검사에대한 생각을 못함
"""
