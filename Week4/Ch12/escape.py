# "r" : read
# "w" : write
# "a" : append
# "r+" : read + write => 읽고 쓰기 (기데이터 존재)
# "w+" : write + read => 파일을 새로만들거나 지우고 쓰고 읽기 
# "a+" : append + read -> 추가하고 읽기 

# 이스케이프 코드 : 미리 정의해둔 문자 조합
# \n = new line =LF(line feed)
# \t = tab 
# \b = back space -> 하나 지울 때
# \' = 작은 따옴표 표시 할 때  Ex: '안녕 난 \'민이야\''
# \" = 큰 따옴표 표시 할 때  Ex: '안녕 난 \'민이야\''
# \\ = 역 슬래쉬를 그대로 표현하고 싶을 떄 Ex: " 3 \\ 2 는 ?"
# \r = CR(캐리지 리턴) -> 커서를 현재 줄 가장 앞으로 이동

# repr()은 객체의 값을 개발자가 확인하기 좋은 형태의 문자열로 보여주는 함수야.
# Ex: 'hello\nworld'

print("hello\t world!\n")
print("hi", end="\b")
print("kenneth \"lim\"", end="")
# 커서가 앞으로 가서 hkenne 가 thank로 변경됌
print("\rthanks")