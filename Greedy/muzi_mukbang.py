#교재 316
----------------------------------
#[내 풀이] 오답 1
----------------------------------
def solution(food_times, k):
    r = len(food_times)
    n = 0
    

    while k > n:
        for i in range(sum(food_times)):#현재 인덱스의 숫자가 0인지 확인
            t = i%r
            if food_times[t] != 0:
                food_times[t] -= 1
                n += 1
                answer = t+1 # 현재 멈춘지점 인덱스
            else: #0이라면 자신을 제외하고 그 뒤에 있는 숫자들에 대해 0이 아닌 가장 가까운 다른 숫자를 탐색
                for i in range(t+1, r):
                    if food_times[i] != 0:
                        food_times[i] -= 1
                        n += 1
                        answer = i+1 # 현재 멈춘지점 인덱스
                        break
                    elif food_times.count(0) == r: #모두 0이라면 함수중단
                        answer = -1
                        break
                    break
    
    return answer
