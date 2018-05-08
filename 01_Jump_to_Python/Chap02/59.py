# coding: cp949
a="hobby"

print("find와 index함수의 차이점 비교")

print(a.find('y'))
print("a.find('y') 수행완료")
print(a.find('c'))
print("a.find('c')) 수행완료")
print(a.index('y'))
print("a.index('y')) 수행완료")
try:
    print(a.index('c'))
    print("a.index('c')) 수행완료")
except ValueError as e:
    print("원하는 결과값이 없음")
    print(e)

print("\n 분석을 완료합니다. 프로그램정상종료")
