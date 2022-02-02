# 슬라이싱  (문자열 자르기)
jumin = "780727-1683816"

print("성별 : " + jumin[7])         #문자열 0부터 시작
print("년 : " + jumin[0:2])         
print("월 : " + jumin[2:4])
print("월 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])    #처음부터 6번째 직전까지
print("뒷자리 : " + jumin[7:])      #7자리부터 끝까지
print("뒷자리(뒤에서부터) : " + jumin[-7:])      #뒤에서 7번째부터 끝까지


python = "Python is Amazing"
print(python.lower())            #소문자로
print(python.upper())            #대문자로
print(python[0].isupper())       #문자 대문자 확인
print(len(python))               #문자열 길이
print(python.replace("Python","Java"))    #문자열 대체

index = python.index("n")
print(index)                     #문자의 위치
index = python.index("n", index + 1)
print(index)                     #다음번 문자의 위치

print(python.find("Java"))      #find()에서 찾는 값이 없으면 -1 리턴, 계속 실행 됨.
#print(python.index("Java"))    #index()에서 찾는 값이 없으면 오류 발생 후 종료 됨.
print("hi")

print(python.count("n"))        #문자열 몇개인지 찾기


# https://www.youtube.com/watch?v=kWiCuklohdY
# 강의 1:00까지 시청