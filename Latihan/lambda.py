import math
def a(x):
    return x**2
print(f'hasil dari 2 pangkat 2 adalah {a(2)}')

# lambda
pangkat = lambda x : x**2
print(f'hasil dari 2 pangkat 2 adalah {pangkat(2)}')

def b(x, y):
    return math.sqrt(x**2 + y**2)
print(f'hasilnya adalah {b(2,3)}')

# lambda
b = lambda x,y : math.sqrt(x**2 + y**2)
print(f'hasilnya adalah {b(2,3)}')


def c(*args):
    return sum(args)/len(args)
print(c(2,4,6,8,10)) 

# Lambda
c = lambda *args: sum(args) / len(args)
print(f'hasilnya adalah: {c(2, 4, 6, 8, 10)}')

def d(s):
    return "".join(set(s))
print(d("hello"))

# Lambda
data = [1,2,3,4,5]
d = lambda s: "".join(set(s))
print(d("hello"))