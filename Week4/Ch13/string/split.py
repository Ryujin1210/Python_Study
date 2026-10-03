# 함수 사용 시 확인할 내용 
# 1. 기능/동작
# 2. 매개 변수
# 3. 반환 값

# split(구분자) -> 리스트 반환

my_string = "Python is a popular programming language" 
split_list = my_string.split()
print(split_list)

###################

# srtip(양 끝 공백 제거) - \t, \n, space ... 

m_string = "    python is awesome!!!!    "
strip_m = m_string.strip()
print(m_string)
print(strip_m)

###################

# 구분자.join(리스트)

# my_list = ["apple", "banana", 123] - 문자열이 아닌 값이 섞이면 에러
my_list = ["apple", "banana", "cherry"]
joined_string = "-".join(my_list)
print(joined_string)
