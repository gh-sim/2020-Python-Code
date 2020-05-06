#0에서 9까지의 수 중에서 7이 나오면 반복 종료

from random import randint
LUCKY = 7

while True:
    n = randint(0,9)
    if n == LUCKY:
        print('드디어 %d, 종료!' %n)
        break
    else:
        print('%d,%d 나올 때까지 계속!' %(n,LUCKY))

else:
    print('여기는 실행 되지 않습니다.')
