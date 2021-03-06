#在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
for (i=0; i<list.length; i++) {
    n = list[i];
}

#Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。
#因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
#注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
#1. 有序集合：list，tuple，str和unicode；
#2. 无序集合：set
#3. 无序集合并且具有 key-value 对：dict
#而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。
#迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。

#用for循环迭代数列 1-100 并打印出7的倍数。
for i in range(1,101):
    if i % 7 == 0:
        print(i)

#索引迭代
#Python中，迭代永远是取出元素本身，而非元素的索引。
#对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？
#方法是使用 enumerate() 函数：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(index, '-', name)
#0 - Adam
#1 - Lisa
#2 - Bart
#3 - Paul

#使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。
#但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：['Adam', 'Lisa', 'Bart', 'Paul']
#变成了类似：[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
#因此，迭代的每一个元素实际上是一个tuple：
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print(index, '-', name)
#0 - Adam
#1 - Lisa
#2 - Bart
#3 - Paul

#以下三行代码会报错
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in L:
    print(index, '-', name)

#可见，索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，
#再迭代，就同时获得了索引和元素本身。

#zip()函数可以把两个 list 变成一个 list：
print(list(zip([10, 20, 30], ['A', 'B', 'C'])))  #[(10, 'A'), (20, 'B'), (30, 'C')]
print(dict(zip([10, 20, 30], ['A', 'B', 'C'])))  #{10: 'A', 20: 'B', 30: 'C'}

#在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如何打印出名次 - 名字（名次从1开始)
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(str(index+1)+'-'+name)
#1-Adam
#2-Lisa
#3-Bart
#4-Paul

#或者
L = ['Adam', 'Lisa', 'Bart', 'Paul']
N = range(1, len(L)+1)  #len(L)=4

print(list(zip(N,L)))

for index, name in zip(N, L):
    print(str(index)+'-'+name)

#迭代dict的value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print(list(d.values()))
#[95, 85, 59]

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for v in d.values():
    print(v)
#95
#85
#59

#values() 方法实际上把一个 dict 转换成了包含 value 的list。
#python 3 中取消了dict 的itervalues()方法

L = [('a','b'),('c','d')]
d = dict(L)
print(d)  #{'a': 'b', 'c': 'd'}

L = ['a','b','c','d']
d = dict(L)  #报错

#在Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，
#任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。
#如果一个对象说自己可迭代，那我们就直接用 for 循环去迭代它，
#可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求。

#给定一个dict，请计算所有同学的平均分。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
print(d)
if len(d) == 0 or d is None:
    print(0)
else:
    print(sum(d.values())/len(d))

#或者
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for x in d.values():
    sum = sum + x 

if len(d) == 0 or d is None:
    print(0)
else:
    print(sum/len(d))

#迭代dict的key和value
#dict 对象的 items() 方法
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

print(list(d.items()))  #[('Adam', 95), ('Lisa', 85), ('Bart', 59)]
print(d.items())  #dict_items([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

for v in d.items():
    print(v)  #('Adam', 95)
              #('Lisa', 85)
              #('Bart', 59)
for name, score in d.items():
    print(name+str(score))  #Adam95
                            #Lisa85
                            #Bart59

#python 3 中取消了dict的iteritems()方法

#打印出 name : score，最后再打印出平均分 average : score。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.items():
    sum = sum + v
    print(k, ':', v)
if len(d) == 0 or d is None:
    print('average', ':', 0)
else:
    print('average', ':', sum/len(d))
#Adam : 95
#Lisa : 85
#Bart : 59
#Paul : 74
#average : 78.25
