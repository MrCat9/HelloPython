#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)：
print(list(range(1, 11)))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1,11):
    L.append(x**2)
print(L)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L = [x * x for x in range(1, 11)]
print(L)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。
#写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来

#range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
print(list(range(1, 10, 2)))  #[1, 3, 5, 7, 9]

#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([x*(x+1) for x in range(1, 101, 2)])  #[2, 12, 30, 56, 90, 132, 182, 240, 306, 380,……

#或者
print([x*y for x,y in zip(range(1,101,2),range(2,101,2))])

#使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
#假设有如下的dict，完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.items()]  #list
#注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。
print("<table border='1'>")
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))    #字符串的join()方法可以把一个 list 拼接成一个字符串。
print('</table>')
#<table border='1'>
#<tr><th>Name</th><th>Score</th><tr>
#<tr><td>Adam</td><td>95</td></tr>
#<tr><td>Lisa</td><td>85</td></tr>
#<tr><td>Bart</td><td>59</td></tr>
#</table>

#tr代表一行 以<tr>开始，</tr>结束
#td代表一格 以<td>开始，</td>介绍 中间的style就是颜色了
#<tr><td>%s</td><td style="color:red">%s</td></tr>就代表有一行，有2个格子，第二个格子用红色显示！

#在生成的表格中，对于没有及格的同学，请把分数标记为红色。
#提示：红色可以用 <td style="color:red"> 实现。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')
#<table border="1">
#<tr><th>Name</th><th>Score</th><tr>
#<tr><td>Adam</td><td>95</td></tr>
#<tr><td>Lisa</td><td>85</td></tr>
#<tr><td>Bart</td><td style="color:red">59</td></tr>
#</table>

#条件过滤
#列表生成式的 for 循环后面还可以加上 if 判断。例如：
print([x * x for x in range(1, 11)])  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：
print([x * x for x in range(1, 11) if x % 2 == 0])  #[4, 16, 36, 64, 100]
#有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。

print(isinstance('asdf', str))  #True  isinstance(x, str) 可以判断变量 x 是否是字符串
print(isinstance(122, int))  #True
print(isinstance(12.2, float))  #True

print('asdf'.upper())  #ASDF  字符串的 upper() 方法可以返回大写的字母。
print('ASDF'.lower())  #asdf

#编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]

print(toUppers(['Hello', 'world', 101]))  #['HELLO', 'WORLD']

#或者
def toUppers(L):
    return [x.upper() for x in L if type(x) == str]

print(toUppers(['Hello', 'world', 101]))  #['HELLO', 'WORLD']

#多层表达式
#for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。
#对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
print([m + n for m in 'ABC' for n in '123'])  #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

#翻译成循环代码就像下面这样：
L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)

print(L)  #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
print([100 * x + 10 * y + z for x in range(1, 10) for y in range(10) for z in range(10) if x == z])
#或者
print([x for x in range(100, 1000) if str(x)[0] == str(x)[2]])
