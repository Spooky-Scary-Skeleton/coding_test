#-------------------
#[내풀이] 못풀었음
#-------------------

#-------------------
#[내풀이] 1115 못풀었음
#-------------------

#-------------------
#[내풀이] 틀리게 풀었음
#-------------------

#-------------------
#[내풀이] 210403
#-------------------

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4, n):
  dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 796796)

#-------------------
#[교재풀이] 다이나믹 이용
#-------------------

n = int(input())

#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
  d[i] = (d[i-1] + 2 * d[i-2])

print(d[n])



#-------------------
#[부족한점] 솔직히 아직도 잘 이해가 안가긴 한다. 
#-------------------

"""
저렇게 간단하게 생각해도 문제가 풀리는게 아직 이해가 잘 안간다. 
내가 경우의 수를 너무 복잡하게 생각하는거 같다. 
"""

#-------------------
#[부족한점] 1115 
#-------------------

"""
그나마 핵심 아이디어는 어느정도 떠오른다. 그런데 정확하게 못떠올리고 구현도 못함. 
"""

#-------------------
#[부족한점] 210316 
#-------------------
"""
이번에도 핵심은 떠올린거 같은데 정확하게 이해를 못했고 
"""

#-------------------
#[부족한점] 210403
#-------------------

"""
이번엔 제대로 풀었다.
"""


