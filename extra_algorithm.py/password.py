#--------------
#[내풀이] 못풀음
#--------------

import itertools

l, c = map(int, input().split())
alphabet = list(input().split())

vowel = ['a', 'e', 'i', 'o', 'u']

vowel_lst = []
consonant_lst = []

for i in alphabet:
  if i in vowel:
    vowel_lst.append(i)
  else:
    consonant_lst.append(i)

vowel_lst.sort()
consonant_lst.sort()

print(vowel_lst)
print(consonant_lst)

#password구하기

j = 1
while (l-j) >= 2:  
  for i in itertools.combinations(vowel_lst, j):
    v_pass = list(i)
    for i in itertools.combinations(consonant_lst, l-j):
      c_pass = list(i)
      print(sorted(v_pass+c_pass))
  
  if j < len(vowel_lst):
    j += 1

#--------------
#[내풀이] 못풀음
#--------------
    
l, c = map(int, input().split())

vowels = []
consonants = []

for i in list(input().split()):
  if i == 'i' or i == 'a' or i == 'e' or i == 'u':
    vowels.append(i)
  else:
    consonants.append(i)

vowels.sort()
consonants.sort()

print(vowels)
print(consonants)

for i  

#--------------
#[내풀이] 풀긴했는데 너무 하드코딩 같음. 
#--------------

import itertools


#암호길이 문자종휴 입력
l, c = map(int, input().split())
#알파벳 종류 입력
alphabet = input().split()
#모음선별기준
vowel = ['a', 'i', 'e', 'o', 'u' ]

#모음 자음 저장용 리스트
selected_vowel = []
selected_consonant = []

#암호조합 저장용 리스트
password = []

for i in alphabet:
  if i in vowel:
    selected_vowel.append(ord(i))
  else:
    selected_consonant.append(ord(i))

#자음갯수 최소 2개 부터 시작
for i in range(2, l):
  pw_c = list(map(list, itertools.combinations(selected_consonant, i)))
  pw_v = list(map(list, itertools.combinations(selected_vowel, l-i)))

  #암호조합 저장.
  for j in pw_c:
    for k in pw_v:
      pw = sorted(j+k)
      password.append(pw)

password.sort()

for i in password:
  for j in i:
    print(chr(j), end='');
  print()

  
#--------------
#[교재풀이] 
#--------------

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u') #5개의 모음 정의
l, c = map(int, input().split(' '))

#가능한 암호를 사전식으로 출력해야하므로 입력 이후에 정렬 수행
array = input().split(' ')
array.sort()

#길이가 l인 모든 암호조합 확인
for password in combinations(array, l):
  #패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
  count = 0
  for i in password:
    if i in vowels:
      count += 1
  #최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
  if count >= 1 and count <= l-2:
    print(''.join(password))
    
#--------------
#[부족한점] 
#--------------
"""
join사용방법모름
그리고 너무 어렵게 생각해서 모음 자음 따로 분리해서 리스트만들고 그걸로 재조합 하려고함
단순하게 모든 길이의 조합 다 가져오고 모음 갯수랑 자음 갯수만 체크해서 출력하면 되는 거였음. 
"""


#--------------
#[부족한점] 
#--------------
"""
join사용방법모름2
너무 어렵게 생각해서 모음 자음 따로 분리해서 리스트만들고 그걸로 재조합 하려고함2
combinations에 들어갈 자료가 이미 사전식으로 정렬되어있다면 출력할때도 사전식으로 출력됨. 
"""

#--------------
#[부족한점] 
#--------------
"""
여전히 모음자음 그대로 따로 뽑고 하려고 함....
그나마 어떻게든 하드코딩해서 풀기는했음....
"""
