from functools import reduce
nums = range(1, 20)
#filter()
even = list(filter(lambda x : x%2 == 0, nums))
# odd = filter(lambda x : x%2 != 0, nums)
print(even)
# print(list(odd))


def func(n):
    return n+2
doub = list(map(func, even))
#map()
doub_lam = list(map(lambda x : x+2, even))
print(doub_lam)
#reduce()
cummulative = reduce(lambda a,b : a+b, doub_lam)
print(cummulative)