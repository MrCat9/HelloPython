#对list进行切片
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)  #['Adam', 'Lisa', 'Bart']

#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。

#对应上面的问题，取前3个元素，用一行代码就可以完成切片：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print(L[0:3])  #['Adam', 'Lisa', 'Bart']          #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[:3])   #['Adam', 'Lisa', 'Bart']          #如果第一个索引是0，还可以省略
print(L[1:3])  #['Lisa', 'Bart']                  #也可以从索引1开始，取出2个元素出来
print(L[:])    #['Adam', 'Lisa', 'Bart', 'Paul']  #只用一个 : ，表示从头到尾  #因此，L[:]实际上复制出了一个新list。
print(L[::2])  #['Adam', 'Bart']                  #切片操作还可以指定第三个参数，第三个参数表示每N个取一个，
                                                  #上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L[1:6:3])  #['b', 'e']
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L[1:6:1])  #['b', 'c', 'd', 'e', 'f']

#把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple。

#range()函数可以创建一个数列  range(m,n)-->从m开始的(n-m)个数   从m开始，到n-1

#请利用切片，取出：
#1. 前10个数；
#2. 3的倍数；
#3. 不大于50的5的倍数。
L = []
for x in range(1, 101):
    L.append(x)

print(L[:10])
print(L[2::3])
print(L[4:50:5])

#对于list，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print(L[-2:])      #['Bart', 'Paul']
print(L[:-2])      #['Adam', 'Lisa']
print(L[-3:-1])    #['Lisa', 'Bart']
print(L[-4:-1:2])  #['Adam', 'Bart']

#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
#倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。

#利用倒序切片对 1 - 100 的数列取出：
#最后10个数；
#最后10个5的倍数。
L = []
for x in range(1, 101):
    L.append(x)

print(L[-10:])  #[91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print((L[4::5])[-10:])  #[55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

#字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])   #ABC
print('ABCDEFG'[-3:])  #EFG
print('ABCDEFG'[::2])  #ACEG

#字符串有个方法 upper() 可以把字符变成大写字母：
print('abc'.upper())  #ABC
print('ABC'.lower())  #abc

#设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
def firstCharUpper(s = ''):
    #return s[:1].upper()+s[1:]
    #return s[0].upper()+s[1:]
    return s.title()

print(firstCharUpper('hello'))  #Hello
print(firstCharUpper('sunday'))  #Sunday
print(firstCharUpper('september'))  #September
print(firstCharUpper('a'))  #A
print(firstCharUpper('B'))  #B

#以下三行代码不会报错
s = ''
print(s[:1])      # 
print(s[1:1111])  # 
