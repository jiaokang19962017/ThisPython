# 迭代器
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))

# for循环遍历迭代器

for i in it:
    print(i, end=' ')
