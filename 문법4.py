# 문자열 포맷
print("a" + "b")    #연속해서 붙음
print("a", "b")     #공백 붙음

# 방법1  %s 변수
print("나는 %d살 입니다." % 20)         # %d 정수형
print("나는 %s 입니다." % "학생")       # %s 문자열형
print("Apple 은 %c로 시작해요" % "A")   # %c 문자형

print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("빨간", "파란"))

# 방법2  {} 중괄호 변수
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아합니다." .format("파란","빨간"))    # 배열 순서 지정
print("나는 {1}색과 {0}색을 좋아합니다." .format("파란","빨간"))    # 배열 순서 바꿀 수 있음

# 방법3 내부 변수명 선언
print("나는 {age}살이고, {color}색을 좋아합니다." .format(age = 20, color = "파란"))    # 변수명 선언

# 방법4. 변수 선언 가능 (v3.6이상부터 적용 가능)
age = 45
color = "보라"
print(f"나는 {age}살이고, {color}색을 좋아한다")

# https://www.youtube.com/watch?v=kWiCuklohdY
# 강의 1:09 까지 시청