# 1. 定义变量
age = 25
height = 1.78
name = "张三"
is_student = True

# 2. 用 f-string 输出
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}米")
print(f"是否是学生：{is_student}")

# 3. 看类型
print(f"name 的类型是 {type(name)}")
print(f"age 的类型是 {type(age)}")

# 4. 类型转换
a = "100"
b = int(a)        # 字符串"100" → 整数100
print(f"{a} + 50 = {b + 50}")