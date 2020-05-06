#다양한 커피 종류가 저장된 리스트
coffee = ['에스프레소','아메리카노','카페라테','카페모카']
print(coffee)
print(type(coffee))

num = 0
for s in coffee:
    num+=1
    print('%d. %s' %(num,s))
