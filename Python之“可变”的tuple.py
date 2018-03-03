t = ('a', 'b', ['A', 'B'])
print(t)  #('a', 'b', ['A', 'B'])
#注意到 t 有 3 个元素：'a'，'b'和一个list：['A', 'B']。list作为一个整体是tuple的第3个元素。list对象可以通过 t[2] 拿到：
L = t[2]
print(L)  #['A', 'B']
L[0] = 'X'
L[1] = 'Y'
print(L)  #['X', 'Y']
print(t)  #('a', 'b', ['X', 'Y'])
#表面上看，tuple的元素确实变了，但其实变的不是 tuple 的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#理解了“指向不变”后，要创建一个内容也不变的tuple，就必须保证tuple的每一个元素本身也不能变。

t = ('a', 'b', ['A', 'B'])
print(t)
#若要让tuple内容不可变
t = ('a', 'b', ('A', 'B'))
print(t)
