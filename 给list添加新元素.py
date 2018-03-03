#用 list 的 append() 方法，把新同学追加到 list 的末尾：
L = ['Adam', 'Lisa', 'Bart']
L.append('Paul')
print(L)
#['Adam', 'Lisa', 'Bart', 'Paul']

#用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：
L = ['Adam', 'Lisa', 'Bart']
L.insert(0, 'Paul')
print(L)
#['Paul', 'Adam', 'Lisa', 'Bart']
#L.insert(0, 'Paul') 的意思是，'Paul'将被添加到索引为 0 的位置上（也就是第一个），而原来索引为 0 的Adam同学，以及后面的所有同学，都自动向后移动一位。

L = ['Adam', 'Lisa', 'Bart']
L.insert(2, 'Paul')
print(L)
#['Adam', 'Lisa', 'Paul', 'Bart']
