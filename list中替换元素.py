#先删除，在添加==替换
#对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。
L = ['Adam', 'Lisa', 'Bart']
print(L)  #['Adam', 'Lisa', 'Bart']
#L[2] = 'Paul'
L[-1] = 'Paul'
print(L)  #['Adam', 'Lisa', 'Paul']
