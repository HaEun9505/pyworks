#BMI 지수 계산하기
name = input("이름을 입력하세요: ")
h = float(input("키(cm)를 입력하세요: "))
h = h / 100
kg = float(input("몸무게(kg)를 입력하세요: "))

bmi = kg / (h * h)

print("{}님의 bmi는 {:.2f}입니다.".format(name, bmi))
print("%s님의 bmi는 %.2f입니다" % (name, bmi))    #변수를 묶는 괄호 필수

if bmi < 20:
    print("저체중입니다.")
elif bmi >= 21 and bmi < 24:
    print("정상입니다.")
elif bmi >= 25 and bmi < 29:
    print("과체중입니다.")
else:
    print("비만입니다.")