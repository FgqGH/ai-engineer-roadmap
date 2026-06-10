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

name = input("你的名字：")
age_str = input("你的年龄：")
city = input("你的城市：")

age = int(age_str)
future_age = age + 101


print("=" * 6)
print(f"你的名字：{name}")
print(f"你的年龄：{age}")
print(f"你的城市：{city}")
print("=" * 6)
print(f"我叫{name}，{age}岁，来自{city}。")
print(f"10 年后我将 {future_age} 岁。")