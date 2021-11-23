#중첩 for문

# 5행 5열에 문자 출력
for i in range(0, 5):   # 0, 1, 2, 3, 4
    for j in range(0, 5):
        print("$", end='')
    print()

# 직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, i+1):
        print("$", end='')
    print()
print()

# 역직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, 5-i):
        print("$", end='')
    print()
print()

# 5행 5열안에 1부터 순차적으로 증가하기 구현
for i in range(0, 5):
    for j in range(1, 6):
        num = i*5+j
        #i=0, j=5
        #i=1, j=5
        #i=2, j=5
        #i=3, j=5
        #i=4, j=5
        print(num, end=' ')
    print()
