#tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
#创建tuple和创建list唯一不同之处是用( )替代了[ ]。
t = ('Adam', 'Lisa', 'Bart')

#获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素
t = ('Adam', 'Lisa', 'Bart')
print(t)  #('Adam', 'Lisa', 'Bart')
print(t[1])  #Lisa
