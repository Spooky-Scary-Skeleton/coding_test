----------------------------------
#[내 풀이] (정확성 검사에서 틀릴수 있음)
----------------------------------
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
  a[i] = b[n-1-i]

print(sum(a))

----------------------------------
#[교재풀이]
----------------------------------
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
----------------------------------
#[내가 부족한점]
----------------------------------
a와 b 비교해서 작을때만 스왑 실시하고 아닐때는 빠져 나오면 된다는 생각을 못함. 



