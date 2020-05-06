#리스트로 편의점에서 구입할 품목 만들기
goods = []
for i in range(3):
    item = input('구입할 품목은 ?')
    goods.append(item)
    print(goods)

print('길이: %d' % len(goods))    
