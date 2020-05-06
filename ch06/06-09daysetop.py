#요일 문자열 원소로 구성된 집합 연산 수행

daysA = {'월','화','수','목'}
daysB = set(['수','목','금','토','일'])
weekends = set(('토','일'))

alldays = daysA | daysB
print(alldays)

workdays = alldays - weekends
print(workdays)

print(daysA & daysB)
print(daysA.symmetric_difference(daysB))
             
