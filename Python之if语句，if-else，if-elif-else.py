age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
print('END')
#your age is 20
#adult
#END
#注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。
#注意: if 语句后接表达式，然后用:表示代码块开始。
#如果 if 语句判断为 True，就会执行这个代码块。
#缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。

age = 2
#age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')
#利用 if ... else ... 语句，我们可以根据条件表达式的值为 True 或者 False ，分别执行 if 代码块或者 else 代码块。
#注意: else 后面有个“:”。

age = 2
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age >= 3:
    print('kid')
else:
    print('baby')
#baby
#特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。
