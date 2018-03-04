#dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。
#有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。
#set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
#创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
s = set(['A', 'B', 'C'])
print(s)  #{'A', 'B', 'C'}
#请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，
#打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

#因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list时，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。
s = set(['A', 'B', 'C', 'C'])
print(s)  #{'B', 'A', 'C'}
print(len(s))  #3

#由于set存储的是无序集合，所以我们没法通过索引来访问。
#访问 set中的某个元素实际上就是判断一个元素是否在set中。
#例如，存储了班里同学名字的set：
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print('Bart' in s)  #True
print('bart' in s)  #False  区分大小写，'Bart' 和 'bart'被认为是两个不同的元素。
print('Bill' in s)  #False

#lower()
print('AABB'.lower())  #aabb

#改进set，使得 'adam' 和 'bart'都能返回True。
s = set(name.lower() for name in ['Adam', 'Lisa', 'Bart', 'Paul'])
print(s)  #{'adam', 'paul', 'lisa', 'bart'}
print('adam' in s)  #True
print('bart' in s)  #True

#set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
#set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
#set存储的元素也是没有顺序的。
#set 的应用
#星期一到星期日可以用字符串'MON', 'TUE', ... 'SUN'表示。
#假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？
#可以用 if 语句判断，但这样做非常繁琐
#如果事先创建好一个set，包含'MON' ~ 'SUN'：
#再判断输入是否有效，只需要判断该字符串是否在set中：
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
print(weekdays)  {'FRI', 'TUE', 'WED', 'THU', 'SAT', 'MON', 'SUN'}
x = input("input:")
if x in weekdays:
    print('input ok')
else:
    print('input error')

#请设计一个set并判断用户输入的月份是否有效。
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'  #输入1
x2 = 'Sun'  #输入2

if x1 in months:
    print('x1: ok')
else:
    print('x1: error')

if x2 in months:
    print('x2: ok')
else:
    print('x2: error')
#x1: ok
#x2: error

#由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。
#直接使用 for 循环可以遍历 set 的元素：
s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print(name)
#Lisa
#Adam
#Bart

#注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。

#请用 for 循环遍历如下的set，打印出 name: score 来。
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x[0]+': '+str(x[1]))

#或者
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for name,score in s:
    print(name+': '+str(score))

#由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：
#一是把新的元素添加到set中，二是把已有元素从set中删除。
#添加元素时，用set的add()方法：
s = set([1, 2, 3])
print(s)  #{1, 2, 3}
s.add(4)
print(s)  #{1, 2, 3, 4}

#如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：
s = set([1, 2, 3])
print(s)  #{1, 2, 3}
s.add(3)
print(s)  #{1, 2, 3}

#删除set中的元素时，用set的remove()方法：
s = set([1, 2, 3, 4])
print(s)  #{1, 2, 3, 4}
s.remove(4)
print(s)  #{1, 2, 3}
#如果删除的元素不存在set中，remove()会报错

#所以用add()可以直接添加，而remove()前需要判断。

#针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print(s)  #{'Bart'}

#或者
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
t = set(L)
for a in s:
    t.remove(a)
print(t)  #{'Bart'}
