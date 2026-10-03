print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

student = { "학번":21012345, "이름":"김세종", "학과":"컴퓨터공학과" }
print(student["학번"] == 21012345 and student["이름"] == "김세종" and student["학과"] == "컴퓨터공학과")
print(student["이름"])

print(type(student))
print(student.values())