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
#[내 풀이] 1114 sorted 사용법 까먹어서 구글링함
----------------------------------
#학생수
n = int(input())

#저장소
array = []

#입력받기
for i in range(n):
  array.append(list(input().split()))
  array[i][1] = int(array[i][1])

def setting(data):
  return data[1]

#정렬수행
sorted_array = sorted(array, key = setting)

print(sorted_array)

for i in range(n):
  print(sorted_array[i][0], end = ' ')
  
  
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

----------------------------------
#[내가 부족한점] 1114
----------------------------------
sorted 함수 사용법을 까먹음 

