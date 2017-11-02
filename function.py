# 无参数函数
def show():
    print("hello,world")


show()  # 调用函数,类似js直接调用


# 有参数函数
def area(width, height):
    return width * height


wid = int(input()) # 接收控制台输入的,并进行类型转化
hei = int(input())
print(area(wid, hei))
