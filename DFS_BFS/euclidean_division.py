#유클리드 호제법: a와 b의 최대공약수는 a를b로 나눈 나머지 r 과 b의 최대 공약수와 같다. 
#https://www.youtube.com/watch?v=7C9RgOcvkvo&list=RDCMUChflhu32f5EUHlY7_SetNWw&index=2
#강의 23분경

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)

print(gcd(192, 162))
