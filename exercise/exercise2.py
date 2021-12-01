#연습문제

#1
score = [80, 75, 55]
sum = 0
avg = 0.0

for i in score:
    sum += i

avg = sum / len(score)
print("평균 : ", avg)

#2


#3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#4
pin = "881120-1068234"
print(pin[-7])

#5
replace = "a#b#c#d"
a = "a:b:c:d"
b = replace
print(b)