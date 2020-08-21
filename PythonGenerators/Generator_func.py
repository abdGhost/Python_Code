# def gen_fibon(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
#
#
# for num in gen_fibon(10):
#     print(num)


# def simple_range():
#     for x in range(3):
#         yield x
#
#
# g = simple_range()
# print(next(g))

# def gensqurae(n):
#     for x in range(n):
#         yield x**2
#
#
# for num in gensqurae(10):
#     print(num)

# import random
#
#
# def rand_num(low,high,n):
#     for i in range(n):
#         yield random.randint(low,high)
#
#
# for num in rand_num(1,10,12):
#     print(num)


# s = 'hello'
# str_iter = iter(s)
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))







