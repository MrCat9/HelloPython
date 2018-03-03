#Python的 for 循环可以依次把list或tuple的每个元素迭代出来：
L = ['Adam', 'Lisa', 'Bart']
for name in L:    #注意:  name 这个变量是在 for 循环中定义的，意思是，
    print(name)   #依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。
#Adam
#Lisa
#Bart

#计算平均分
L = [75, 92, 59, 68]
sum = 0.0  #定义sum为浮点型
for score in L:
    sum = sum + score
print(sum / 4)  #73.5

#while循环每次先判断 x < N，如果为True，则执行循环体的代码块，否则，退出循环。
N = 10
x = 0
while x < N:  #while小心死循环
    print x
    x = x + 1

#利用while循环计算100以内奇数的和。
sum = 0
x = 1
while x <= 100:
    sum = sum + x
    x = x + 2
print(sum)
#2500

#用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
#比如计算1至100的整数和，我们用while来实现：
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print(sum)

#利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print(sum)
#1048575

#在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
#统计60分以上同学的平均分
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print(sum / n)
#79.0

#对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print(sum)
#2500

for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print(x + y)
#A1
#A2
#A3
#B1
#B2
#B3
#C1
#C2
#C3

for i in range(3):
    print(i)
#0
#1
#2
#range(n)  从0开始的（n-0）个数

for x in range(1, 3):
    print(x)
#1
#2
#range(m,n)  从m开始的（n-m）个数

listC = [i for i in range(1,30,3)]
print(listC)  #[1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
listC = [i+1 for i in range(1,30,3)]
print(listC)  #[2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
#range(m,n,d)  从m开始，步长为d，一直到n

test_list = [1,3,4,'abc',3,6,23,'hello',2]
for i in range(len(test_list)):
    print(test_list[i],end=',')
#1,3,4,abc,3,6,23,hello,2,

#对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in range(1, 9):
    for y in range(x + 1, 10):
        print(str(x) + str(y))
