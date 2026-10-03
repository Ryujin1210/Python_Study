import os
print(os.getcwd())

# 파일 객체 = open(경로, 모드)
# # 절대 경로
# f = open("/home/ryu/Desktop/UTM_Rokey/Week4/Ch12/file_open.py", "r")

# 파일 열기
# f = open("/home/ryu/Desktop/UTM_Rokey/Week4/Ch12/file1.txt", "w")
f = open("file2.txt", "w") # 쓰기모드의 경우 기존 내용 존재시 삭제 주의 

# 파일 닫기
f.close()

# # 상대 경로 
# f = open("file_open.py", "w")
# f = open("./file_open.py", "a")