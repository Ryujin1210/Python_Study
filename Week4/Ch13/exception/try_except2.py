# print문이 실행되면 예외, 안되면 문법 오류

print("try_exccept2")

path = r"./myfile.txt"
# mode 기본 값은 'r'

# f = open(path)
# s = f.readline()
# i = int(s.strip())

try:
    # f = open(path, "w")
    # f.write("hello")
    f = open(path)
    s = f.readline()
    i = int(s.strip())   # Value Error => "1"
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다.", e)
except ValueError as e:
    print("정수형으로 변환 할 수 없습니다", e)
except Exception as err:
    print("에측 되지 않은 에러", err)
finally:
    f.close()
print("프로그램 종료")
    