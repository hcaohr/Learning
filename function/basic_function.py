def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return -x

def power(x, n=2): #默认参数
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

def add_end(L=None): #默认参数必须指向不变对象,可以用None这个不变对象来实现
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers): #可变参数，*args是可变参数，args接收的是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum


def person(name, age, **kw): #关键字参数，**kw是关键字参数，kw接收的是一个dict
    print('name: ', name, ' age: ', age, ' other: ', kw)

#print(my_abs(2))
#print(my_abs('A'))
# print(power(5,1))
# print(add_end())
# print(add_end())
# print(calc(1,2,3))


print(person('Bob', 35, city='Beijing'))