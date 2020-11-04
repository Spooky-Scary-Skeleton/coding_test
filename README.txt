#파이썬 시간 복잡도 측정 코드

import time
start_time = time.time() #측정시작

#프로그램 소스코드
end_time = time.time() #측정 종료
print("time:", end_time - start_time) #수행시간 출력

#파이썬으로 풀때 제약사항 기억
#코드가 1초에 2,000만번 연산을 수행하면 크게 무리가 없음
