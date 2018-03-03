#用list的pop()方法删除最后一个：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
L.pop()
print(L)
#['Adam', 'Lisa', 'Bart']

#Paul的索引是2，用 pop(2)把Paul删掉：
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
print(L)
#['Adam', 'Lisa', 'Bart']

#如果我们要把Paul和Bart都删掉
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print(L)
#['Adam', 'Lisa']
