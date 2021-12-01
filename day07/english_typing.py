#영어 타자 게임
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree',
        'strawberry', 'grape', 'garlic', 'onion', 'potato']
#r = random.choice(word)

n = 1   #문제 번호
input("[타자게임] 준비되면 엔터! ")
start = time.time()
while n < 11:
        print("-문제", n)
        question = random.choice(word)   #문제 단어 출제
        print(question)
        answer = input()        #사용자가 답을 입력
        #통과 아니면 오타 코드 작성
        if answer == question:
                print("통과!")
                n += 1          #다음 문제 출제
        else:
                print("오타!")

end = time.time()
print("게임 소요 시간 : %.2f" % (end-start))

