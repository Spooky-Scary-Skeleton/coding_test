----------------------------------
#[내 풀이] 너무 복잡하게 딕셔너리 사용함
----------------------------------
n = int(input())

dic = dict(input().split() for i in range(n))

for key in dic:
  dic[key] = int(dic[key])

ndic = sorted(dic.items(), key = lambda x : x[1])

for i in ndic:
  print(i[0], end=" ")
  
----------------------------------
#[교재풀이]
----------------------------------
n = int(input())

ar =[]

for i in range(n):
  input_data = input().split()
  ar.append((input_data[0], int(input_data[1])))

ar = sorted(ar, key = lambda x : x[1])

for i in ar:
  print(i[0], end=" ")
 
----------------------------------
#[내가 부족한점]
----------------------------------
튜플로 자료형 입력시키는게 익숙하지가 않음.그리고 sorted 함수의 사용법에 익숙하지 않음 
