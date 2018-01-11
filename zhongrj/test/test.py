import numpy as np
from functools import reduce
import zhongrj.utils.math_util as math_util

a = [1, 2, 3]

print(math_util.reduce_product(a))

print(np.random.choice(100, 10))

print(len(np.array([[1, 2]])))

print(np.array(a)[::-1])

print(np.array(a)[:, np.newaxis])

print(np.sum(np.array([[1, 2, 3], [2, 3, 4]]), axis=1))

print(8 / 2 ** 2)

for i in reversed(range(1, 10)):
    print(i)

print(np.random.normal(0, 1, size=(50, 100)).astype(np.float32))

# print(np.array([-1e1000]) + np.array([1e1000]))

print(np.NaN == np.NaN)

for i in range(1, 1):
    print("1231231234134")

b = object()
c = {b: 1}
print(c[b])

for i, j in enumerate(reversed([10, 20, 30])):
    print(i, ' --- ', j)

print('{}'.format(123))

print([1, 2, 3, 4][:-1])

print([1, 2] + list())

lambda_test = lambda o, **kwargs: o
print(lambda_test(123, test=1123, test1=123))

print(np.concatenate([np.array(a), np.array(a)]))

# 修改文件名
# import os
# import sys
#
# path = "D:\study\generate_anime_face"
# for (path, dirs, files) in os.walk(path):
#     for filename in files:
#         if filename.find('00.') != -1 or filename.find('25.') != -1 or filename.find('50.') != -1 or filename.find(
#                 '75.') != -1:
#             # print(filename)
#             os.rename(path + "\\" + filename, path + "\\" + filename.replace('sample', 'aaaaaa'))
