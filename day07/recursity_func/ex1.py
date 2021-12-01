#재귀 함수 - 자기가 자신을 호출하는 함수

def sos1(n):
    for i in range(n):
        print("Help me!!")

def sos2(n):
    if n <= 1:
        return ""
    else:
        print("Help me!!")
        return sos2(n-1)

#sos1(5)
sos2(5)     #Help me

