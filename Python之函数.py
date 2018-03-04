help(abs)
#Help on built-in function abs in module builtins:
#
#abs(x, /)
#    Return the absolute value of the argument.

print(abs(100))  #100
print(abs(-20))  #20
print(abs(-12.2))  #12.2

#python 3中，比较函数 cmp(x, y) 被取消
from _operator import lt, le, eq, ne, gt, ge
print(lt(1, 2))  #True  less than
print(le(2, 2))  #True  less than or equal to
print(eq(2, 2))  #True  equal
print(ne(1, 2))  #True  not equal to
print(gt(2, 1))  #True  greater than
print(ge(2, 2))  #True  greater than or equal to

print(int(12.2))  #12
print(str(12.2))  #12.2

#sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
L = []
n = 1
while n <= 100:
    L.append(n*n)
    n = n + 1
print(sum(L))  #338350

#或者
print(sum([n*n for n in range(1, 101)]))

#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，
#然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
#自定义一个求绝对值的 my_abs 函数：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。
#return None可以简写为return。

#定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
def square_of_sum(L):
    sum = 0
    for num in L:
        sum = sum + num*num
    return sum

print(square_of_sum([1, 2, 3, 4, 5]))  #55
print(square_of_sum([-5, 0, 5, 15, 25]))  #900

#或者
def square_of_sum(L):
    return sum(num**2 for num in L)

print(square_of_sum([1, 2, 3, 4, 5]))  #55
print(square_of_sum([-5, 0, 5, 15, 25]))  #900

#函数返回多值
#math包提供了sin()和 cos()函数
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(0, 0, 60, math.pi / 6)
print(x, y)  #51.96152422706632 29.999999999999996
#其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(0, 0, 60, math.pi / 6)
print(r)  #(51.96152422706632, 29.999999999999996)
#返回值其实是一个tuple
#但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

#Python的math包提供了sqrt()函数用于计算平方根。
from math import sqrt
print(sqrt(4))  #2.0  求平方根

#一元二次方程的定义是：ax² + bx + c = 0 请编写一个函数，返回一元二次方程的两个解。
import math
from math import sqrt


def quadratic_equation(a, b, c):
    de = b ** 2 - 4 * a * c
    if de > 0 :
        x1 = (-b + sqrt(de)) / (2 * a)
        x2 = (-b - sqrt(de)) / (2 * a)
        return x1, x2
    elif de == 0 :
        x12 = -b / (2 * a)
        return x12
    else:
        return 'wujie'


print(quadratic_equation(1, -6, 5))  #(5.0, 1.0)
print(quadratic_equation(1, 2, 1))   #-1.0
print(quadratic_equation(2, 3, 10))  #wujie

#递归函数
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#举个例子，我们来计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示，可以看出：
#fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
#所以，fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。
#于是，fact(n)用递归的方式写出来就是：
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))  #1
print(fact(5))  #120
print(fact(100))  #93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试计算 fact(10000)。
#fact(998)可以    fact(999)不行

#汉诺塔的移动也可以看做是递归函数。
#我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
#如果a只有一个圆盘，可以直接移动到c；
#如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，
#首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
#请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
#例如，输入 move(2, 'A', 'B', 'C')，打印出：
#A --> B
#A --> C
#B --> C          #n个需要移动[(2^n)-1]次

def move(n, a, b, c):   #函数 move(n, a, b, c) 的定义是将 n 个圆盘从 a 借助 b 移动到 c。
    if n == 1:
            print(a, '-->', c)  #这其实是只有一个圆盘需要从A到C的情况。所有递归，最终都是走到这一步。
            return  #这是结束递归，省略了None。没有这句的话，递归没办法结束。
    move(n - 1, a, c, b)  #将A柱的n-1个盘移到B柱，注意形参顺序变化了。
    print(a, '-->', c)   #这句话是打印第一个柱子的第n个圆盘移动到目标柱子。
    move(n - 1, b, a, c)  #过渡柱子B上（n-1）个圆盘B递归移动到目标柱子C

move(4, 'A', 'B', 'C')

#定义默认参数
#定义函数的时候，还可以有默认参数。
#例如Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：
#int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。
print(int('123'))     #123
print(int('123', 8))  #83

#可见，函数的默认参数的作用是简化调用，你只需要把必须的参数传进去。
#但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。

#定义一个计算 x 的N次方的函数:
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, 2))  #4

#假设计算平方的次数最多，我们就可以把 n 的默认值设定为 2：
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#这样一来，计算平方就不需要传入两个参数了：
print(power(3))  #9

#由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面

#定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
def greet(name='world'):
    print('Hello, %s.' %name)

greet()  #Hello, world.
greet('Bart')  #Hello, Bart.

#定义可变参数
#





